#!/usr/bin/env python3
"""Check repository structure, the shared learning map, links, and text integrity.

This is not a mathematical proof checker or a hosted renderer.
"""
from __future__ import annotations
import argparse
import importlib.util
import json
import re
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def anchors(text: str) -> set[str]:
    result = set(re.findall(r'<a\s+id="([^"]+)"', text))
    counts: dict[str, int] = {}
    for heading in re.findall(r'^#{1,6}\s+(.+)$', text, re.M):
        slug = re.sub(r'[^\w\- ]', '', heading.lower()).replace(' ', '-')
        count = counts.get(slug, 0)
        counts[slug] = count + 1
        result.add(slug if not count else f'{slug}-{count}')
    return result


def run() -> dict:
    pages = sorted(p for p in ROOT.rglob('*.md') if '.git' not in p.parts)
    require(bool(pages), 'No Markdown pages')
    sources = {p.resolve(): p.read_text(encoding='utf-8') for p in pages}
    spec = importlib.util.spec_from_file_location('math_scan', ROOT/'verification/hosted/check_rendered_math.py')
    require(spec is not None and spec.loader is not None, 'Missing math scanner')
    scanner = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(scanner)
    links = expressions = 0
    for p, text in sources.items():
        require(not any(ord(c)<32 and c not in '\n\r\t' for c in text), f'Control character in {p}')
        expressions += len(scanner.expressions(text))
        for match in re.finditer(r'\[[^\]\n]+\]\(([^\s)]+)\)', text):
            href = match.group(1)
            parsed = urlsplit(href)
            if parsed.scheme or parsed.netloc:
                continue
            target = (p.parent / unquote(parsed.path)).resolve() if parsed.path else p
            require(target.is_relative_to(ROOT.resolve()), f'Link escapes repository: {href}')
            require(target.exists(), f'Missing link from {p.relative_to(ROOT)}: {href}')
            if parsed.fragment and target.suffix == '.md':
                require(unquote(parsed.fragment) in anchors(target.read_text(encoding='utf-8')),
                        f'Missing anchor from {p.relative_to(ROOT)}: {href}')
            links += 1
    text = sources[(ROOT/'learning/MILESTONES.md').resolve()]
    matches = list(re.finditer(r'^### (M\d{2}) — (.+)$', text, re.M))
    require([m.group(1) for m in matches] == [f'M{i:02d}' for i in range(1,31)], 'Need exactly M01--M30')
    split = text.index('## Narrative and innovation')
    require(sum(m.start()<split for m in matches)==12, 'The phase allocation must be 12/18')
    for i,m in enumerate(matches,1):
        stop = matches[i].start() if i<len(matches) else len(text)
        block = text[m.end():stop]
        for field in ['Question','Target','Dependencies','Connection and role','Sources']:
            require(f'**{field}:**' in block, f'{m.group(1)} missing {field}')
        dep = block.split('**Dependencies:**',1)[1].split('**Connection',1)[0]
        for prior in re.findall(r'M(\d{2})',dep):
            require(1<=int(prior)<i, f'{m.group(1)} has non-earlier dependency {prior}')
    for path in ['README.md','llms.txt','learning/README.md','learning/WATROUS_BRIDGE.md']:
        s = (ROOT/path).read_text(encoding='utf-8')
        require('Watrous' in s, f'Anchor missing in {path}')
    return {'status':'pass','markdown_pages':len(pages),'local_links':links,
            'math_expressions':expressions,'milestones':30,'phase_allocation':[12,18],
            'scope':'Source integrity, local navigation, and milestone structure; no proof or hosted-rendering certification.'}


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path)
    args=parser.parse_args()
    if args.output and args.output.exists():
        parser.error('Use a new output path.')
    result=run()
    message=json.dumps(result,indent=2)+'\n'
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(message,encoding='utf-8')
    print(message,end='')
