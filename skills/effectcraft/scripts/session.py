#!/usr/bin/env python3
"""Run a JSON array of MCP tool calls in one EffectCraft session."""
import argparse, json, pathlib, selectors, subprocess, sys

def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('plan', type=pathlib.Path, help='JSON array: [{tool, arguments}]')
    p.add_argument('--bridge', type=int)
    p.add_argument('--timeout', type=float, default=60)
    a = p.parse_args()
    steps = json.loads(a.plan.read_text())
    if not isinstance(steps, list):
        p.error('plan must be an array')
    cli = pathlib.Path.home()/'.local/bin/effectcraft-cli'
    cmd = [str(cli), 'mcp']
    if a.bridge:
        cmd += ['--bridge', str(a.bridge)]
    proc = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
    sel = selectors.DefaultSelector()
    sel.register(proc.stdout, selectors.EVENT_READ)
    counter = 0
    def request(method, params):
        nonlocal counter
        counter += 1
        proc.stdin.write(json.dumps({'jsonrpc':'2.0','id':counter,'method':method,'params':params})+'\n')
        proc.stdin.flush()
        while True:
            if not sel.select(a.timeout):
                raise TimeoutError('Unknown outcome: inspect state before retrying mutations')
            line = proc.stdout.readline()
            if not line:
                raise RuntimeError('MCP server closed its output')
            reply = json.loads(line)
            if reply.get('id') == counter:
                if 'error' in reply:
                    raise RuntimeError(json.dumps(reply['error']))
                return reply.get('result')
    try:
        request('initialize', {'protocolVersion':'2025-03-26','capabilities':{},'clientInfo':{'name':'effectcraft-skill','version':'1.0'}})
        proc.stdin.write(json.dumps({'jsonrpc':'2.0','method':'notifications/initialized'})+'\n')
        proc.stdin.flush()
        for step in steps:
            if step['tool'] == '__list_tools__':
                result = request('tools/list', {})
            else:
                result = request('tools/call', {'name':step['tool'],'arguments':step.get('arguments',{})})
            print(json.dumps({'tool':step['tool'],'result':result}, ensure_ascii=False), flush=True)
            if isinstance(result, dict) and result.get('isError'):
                raise RuntimeError('Tool failed; remaining steps were not executed')
    finally:
        sel.close()
        proc.stdin.close()
        try:
            proc.wait(timeout=5)
        except subprocess.TimeoutExpired:
            proc.terminate()
            proc.wait(timeout=5)
if __name__ == '__main__':
    main()
