"""Cerca lèxica extractiva docent: no és RAG generatiu ni verifica resposta."""
from pathlib import Path
from collections import Counter
import math
import re
import unicodedata

ROOT = Path(__file__).resolve().parents[3]
EMPRESA = ROOT / 'MATERIALS_PRACTICS' / 'empresa'
FILES = ['02_politica_contrasenyes.md', '03_manual_vpn.md', '04_procediment_correu.md']


def termes(text):
    text = ''.join(c for c in unicodedata.normalize('NFD', text.lower())
                   if unicodedata.category(c) != 'Mn')
    return Counter(re.findall(r'[^\W_]{3,}', text, re.UNICODE))


def cosinus(a, b):
    den = math.sqrt(sum(v*v for v in a.values()) * sum(v*v for v in b.values()))
    return sum(v*b.get(k, 0) for k, v in a.items()) / den if den else 0.0


def consultar(pregunta, llindar=0.12):
    if not isinstance(pregunta, str) or not pregunta.strip() or len(pregunta) > 1000:
        raise ValueError('La pregunta ha de tindre entre 1 i 1000 caracters no buits.')
    corpus = []
    for name in FILES:
        text = (EMPRESA / name).read_text(encoding='utf-8')
        corpus.append((cosinus(termes(pregunta), termes(text)), name, text))
    score, name, text = max(corpus, key=lambda row: row[0])
    if score < llindar:
        return {'estat': 'derivar', 'resposta': 'No hi ha prou coincidencia documental.',
                'fonts': [], 'puntuacio': round(score, 4)}
    return {'estat': 'fragment_recuperat', 'resposta': text,
            'fonts': [{'document_id': name, 'fragment_id': name + ':complet',
                       'versio': 'aula-v1'}], 'puntuacio': round(score, 4)}


if __name__ == '__main__':
    for pregunta in ['VPN error de certificat', 'xyzzy qqqvv', 'Telefon suport VPN error certificat']:
        print(pregunta, consultar(pregunta))
