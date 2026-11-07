#!/usr/bin/env python3
"""Bind selected headline expressions to required visible text before capture."""
from __future__ import annotations
import argparse
import json
import subprocess
from pathlib import Path
from check_rendered_math import make_inventory

parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--root',type=Path,required=True)
parser.add_argument('--repository',required=True)
parser.add_argument('--revision',required=True)
parser.add_argument('--output',type=Path,required=True)
a=parser.parse_args()
if a.output.exists():
    parser.error('Use a new contract path.')
sources={p:subprocess.check_output(['git','show',f'{a.revision}:{p}'],cwd=a.root).decode()
         for p in ['README.md','science/noise.md']}
inv=make_inventory(a.repository,a.revision,sources)
rules=[]
for p in inv['pages']:
    for e in p['expressions']:
        required=None
        if p['path']=='README.md' and r'\boxed{n\geq3t+1.' in e['tex']:
            required=['n≥3t+1']
        elif p['path']=='README.md' and r'12(n+1)B^n' in e['tex']:
            required=['πmin','12(n+1)Bn','Pn','δ']
        elif p['path']=='science/noise.md' and r'\text{(N3)}' in e['tex']:
            required=['(N3)','πmin','12(n+1)Bn']
        elif p['path']=='science/noise.md' and r'\text{(N5)}' in e['tex']:
            required=['(N5)','logB','δ']
        if required:
            rules.append({'path':p['path'],'index':e['index'],'source_sha256':e['source_sha256'],
                          'required_text':required})
if len(rules)!=4:
    raise RuntimeError('The four headline contracts no longer match source; inspect the changes.')
a.output.parent.mkdir(parents=True,exist_ok=True)
a.output.write_text(json.dumps({'schema_version':1,'expressions':rules},indent=2)+'\n')
