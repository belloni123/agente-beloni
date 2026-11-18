#!/usr/bin/env python3
"""Start a controlled app only if no EffectCraft desktop process is running."""
import pathlib, socket, subprocess, time
port = 9877
with socket.socket() as s:
    if s.connect_ex(('127.0.0.1', port)) == 0:
        raise SystemExit('Port 9877 already occupied; inspect the listener before connecting.')
r = subprocess.run(['pgrep','-x','EffectCraft'], capture_output=True, text=True)
if r.returncode == 0:
    raise SystemExit('EffectCraft is open without this bridge. Save your project and quit normally, then rerun. No process was stopped.')
log = pathlib.Path.home()/'.codex/skills/effectcraft/bridge.log'
with log.open('ab') as out:
    p = subprocess.Popen(['/Applications/EffectCraft.app/Contents/MacOS/EffectCraft','--control',str(port)], stdout=out, stderr=out, start_new_session=True)
for _ in range(100):
    with socket.socket() as s:
        if s.connect_ex(('127.0.0.1',port)) == 0:
            print(f'EffectCraft PID {p.pid}: control available on 127.0.0.1:{port}')
            break
    if p.poll() is not None:
        raise SystemExit(f'App exited: inspect {log}')
    time.sleep(.1)
else:
    raise SystemExit(f'No control response yet; inspect {log} before retrying.')
