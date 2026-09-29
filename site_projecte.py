"""Prepara i comprova el site sense modificar els materials docents originals."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
import argparse
import os
import re
import shutil
import subprocess
import sys
import zipfile

ROOT = Path(__file__).resolve().parent
DOCS = ROOT / 'web_docs'
SITE = ROOT / 'site'
DOWNLOADS = {'.csv', '.ipynb', '.py', '.zip'}
ALLOWED = {'.md', '.csv', '.ipynb', '.py', '.png', '.svg', '.jpg', '.jpeg', '.webp', '.txt'}
IGNORED = {'site', '.venv', '__pycache__', 'eixides', '.ipynb_checkpoints', '.git'}


def markdown(text):
    """Els canvis són només per a la còpia web, mai per als originals."""
    text = re.sub(r'(?<=/)DOCUMENT_DE_TREBALL\.md|(?<=\()DOCUMENT_DE_TREBALL\.md', 'index.md', text)
    # Atribut HTML natiu: funciona sense JavaScript sobre el mateix origen.
    pattern = r'(\[[^\]\n]+\]\(([^\s)]+\.(?:csv|ipynb|py|zip))\))(?!\{)'
    text = re.sub(pattern, lambda m: m[1] + '{ download="' + Path(m[2]).name + '" }', text)
    return text


def prepare():
    if DOCS.exists():
        shutil.rmtree(DOCS)  # Només la carpeta generada amb nom fix.
    DOCS.mkdir()
    for folder in ['MATERIALS_PRACTICS', 'PINDOLES', 'PINDOLES_AMPLIADES']:
        for source in sorted((ROOT / folder).rglob('*')):
            relative = source.relative_to(ROOT)
            if not source.is_file() or any(p in IGNORED for p in relative.parts):
                continue
            if source.suffix.lower() not in ALLOWED:
                continue
            target = DOCS / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            if source.suffix == '.md':
                text = source.read_text(encoding='utf-8')
                if folder == 'PINDOLES':
                    companion = f'../PINDOLES_AMPLIADES/docs/{source.stem}/index.md'
                    text += f'\n\n## Per aprofundir\n\n[Obri la píndola ampliada, amb pràctiques i exercicis]({companion}).\n'
                target.write_text(markdown(text), encoding='utf-8')
            else:
                shutil.copy2(source, target)
    home = (ROOT / 'DOCUMENT_DE_TREBALL.md').read_text(encoding='utf-8')
    first, rest = home.split('\n', 1)
    shortcuts = '''

[Descàrregues](DESCARREGUES.md){ .md-button }
[Píndoles ampliades](PINDOLES_AMPLIADES/docs/index.md){ .md-button }
[Glossari](glossari_terms.md){ .md-button }

'''
    (DOCS / 'index.md').write_text(markdown(first + shortcuts + rest), encoding='utf-8')
    # Paquet amb estructura conservada: els notebooks troben ../dades/.
    with zipfile.ZipFile(DOCS / 'materials-practics.zip', 'w', zipfile.ZIP_DEFLATED) as bundle:
        for source in sorted((ROOT / 'MATERIALS_PRACTICS').rglob('*')):
            if source.is_file() and source.suffix.lower() in ALLOWED and not any(p in IGNORED for p in source.parts):
                bundle.write(source, source.relative_to(ROOT).as_posix())
    page = '''# Descàrregues del projecte

Els enllaços guarden el fitxer al teu ordinador. Els notebooks s’obrin amb Jupyter després de descarregar-los; els programes Python s’executen en l’entorn indicat per cada píndola.

[Descarrega tots els materials pràctics](materials-practics.zip){ download="materials-practics.zip" .md-button .md-button--primary }

Descomprimix el paquet conservant les carpetes: els notebooks busquen les dades en `../dades/`. Respecta els apartats de cada setmana i la reserva de la prova final descrita en el [document de treball](index.md).

'''
    for title, extension in [('Dades CSV', '.csv'), ('Notebooks', '.ipynb'), ('Exemples Python de les píndoles', '.py')]:
        page += f'## {title}\n\n'
        for path in sorted(DOCS.rglob('*' + extension)):
            rel = path.relative_to(DOCS).as_posix()
            label = path.name if extension != '.py' else path.parent.parent.name + ' · ' + path.name
            page += f'- [{label}]({rel}){{ download="{path.name}" }}\n'
        page += '\n'
    (DOCS / 'DESCARREGUES.md').write_text(page, encoding='utf-8')
    assets = ROOT / 'web_assets'
    if assets.exists():
        shutil.copytree(assets, DOCS / 'assets-projecte')
    print('Preparat: portada des de DOCUMENT_DE_TREBALL.md i materials d’ALUMNAT.', flush=True)


class Page(HTMLParser):
    def __init__(self, text):
        super().__init__()
        self.links = []
        self.ids = set()
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if 'id' in a:
            self.ids.add(a['id'])
        if tag == 'a' and a.get('href'):
            self.links.append(a)


def verify():
    pages = {p.resolve(): Page(p.read_text(encoding='utf-8')) for p in SITE.rglob('*.html')}
    errors = []
    downloads = 0
    for path, page in pages.items():
        for link in page.links:
            url = urlsplit(link['href'])
            if url.scheme or url.netloc or url.path.startswith('/'):
                continue
            dest = (path.parent / unquote(url.path)).resolve() if url.path else path
            if dest.is_dir():
                dest /= 'index.html'
            if not dest.is_relative_to(SITE.resolve()) or not dest.exists():
                errors.append(f'{path.relative_to(SITE)}: destí absent {link["href"]}')
                continue
            if dest.suffix in DOWNLOADS:
                downloads += 1
                if 'download' not in link:
                    errors.append(f'{path.relative_to(SITE)}: falta download a {link["href"]}')
            # L’àncora interna del tema no existix en la seua pàgina 404.
            if path.name == '404.html' and url.fragment == '__skip':
                continue
            if url.fragment and dest in pages and unquote(url.fragment) not in pages[dest].ids:
                errors.append(f'{path.relative_to(SITE)}: àncora absent {link["href"]}')
    for source in DOCS.rglob('*'):
        if source.is_file() and source.suffix in DOWNLOADS:
            published = SITE / source.relative_to(DOCS)
            if not published.is_file() or source.read_bytes() != published.read_bytes():
                errors.append(f'Descàrrega absent o alterada: {source.relative_to(DOCS)}')
    if errors:
        raise SystemExit('\n'.join(sorted(set(errors))))
    print(f'Comprovació correcta: {len(pages)} pàgines, {downloads} enllaços de descàrrega, fitxers idèntics i àncores vàlides.')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action', choices=['prepare', 'build', 'serve', 'check'], nargs='?', default='build')
    args = parser.parse_args()
    if args.action == 'check':
        verify()
        return
    prepare()
    if args.action == 'prepare':
        return
    command = [sys.executable, '-m', 'zensical', 'build', '--clean', '--strict']
    subprocess.run(command, cwd=ROOT, check=True)
    verify()
    if args.action == 'serve':
        # Servim el site ja comprovat; torna a construir després d’editar Markdown.
        subprocess.run([sys.executable, '-m', 'http.server', '8000', '--bind', '127.0.0.1', '--directory', str(SITE)], check=True)


if __name__ == '__main__':
    main()
