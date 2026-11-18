#!/usr/bin/env python3
"""Amostra temporal nominal de vídeo para inspeção; requer ffmpeg e Pillow."""
import argparse
from pathlib import Path
import subprocess
import tempfile
from PIL import Image, ImageDraw

parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('video',type=Path)
parser.add_argument('--start',type=float,default=0)
parser.add_argument('--duration',type=float,default=3)
parser.add_argument('--fps',type=float,default=6)
parser.add_argument('--cols',type=int,default=6)
parser.add_argument('--width',type=int,default=216)
parser.add_argument('--output',required=True,type=Path)
a=parser.parse_args()
if not a.video.is_file(): parser.error('Vídeo não encontrado.')
if a.start<0 or a.duration<=0 or a.fps<=0 or a.cols<1 or a.width<32:
    parser.error('Use início >= 0, duração/fps positivos, colunas >= 1 e largura >= 32.')
if a.duration*a.fps>180: parser.error('Limite cada folha a 180 amostras para manter a inspeção legível.')
with tempfile.TemporaryDirectory(prefix='motion-editorial-') as tmp:
    subprocess.run(['ffmpeg','-v','error','-ss',str(a.start),'-i',str(a.video),'-t',str(a.duration),'-vf',f'fps={a.fps},scale={a.width}:-2','-frames:v',str(int(a.duration*a.fps)),str(Path(tmp)/'%05d.png')],check=True)
    files=sorted(Path(tmp).glob('*.png'))
    if not files: parser.error('Nenhum quadro no intervalo solicitado.')
    with Image.open(files[0]) as first: w,h=first.size
    rows=(len(files)+a.cols-1)//a.cols
    sheet=Image.new('RGB',(a.cols*w,rows*(h+25)),(28,31,25));draw=ImageDraw.Draw(sheet)
    for i,p in enumerate(files):
        x=(i%a.cols)*w;y=(i//a.cols)*(h+25)
        with Image.open(p) as im: sheet.paste(im.convert('RGB'),(x,y))
        draw.text((x+7,y+h+5),f't ~ {a.start+i/a.fps:.3f}s',fill=(239,242,224))
    a.output.parent.mkdir(parents=True,exist_ok=True)
    sheet.save(a.output)
print(f'{len(files)} amostras nominais: {a.output}')
