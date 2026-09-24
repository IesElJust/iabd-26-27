"""Exemple autònom: validar lectures i escriure un informe. Python 3.10+."""
from pathlib import Path
import csv, json, sys

def valida_lectura(text):
    """Retorna (valor, error); zero és una lectura vàlida, no una absència."""
    if text is None or str(text).strip() == '':
        return (None, 'absent')
    try:
        valor = float(text)
    except (ValueError, TypeError):
        return (None, 'format')
    if not -40 <= valor <= 80:
        return (None, 'rang')
    return (valor, None)

def main():
    # Entrades deliberadament heterogènies per comprovar el contracte.
    lectures = ['21.5', '', 'error', '0', '95', '18.0', 'nan']
    resultat = []
    for (posicio, lectura) in enumerate(lectures, start=1):
        (valor, error) = valida_lectura(lectura)
        resultat.append({'id': posicio, 'original': lectura, 'valor': valor, 'error': error})
    # Només les lectures acceptades entren en el resum.
    bons = [r['valor'] for r in resultat if r['error'] is None]
    resum = {'valides': len(bons), 'rebutjades': len(resultat) - len(bons), 'mitjana': sum(bons) / len(bons)}
    desti = Path(__file__).resolve().parent / 'eixides'
    desti.mkdir(exist_ok=True)
    # CSV conserva l’original i el motiu de rebuig per poder auditar.
    with (desti / 'lectures.csv').open('w', encoding='utf-8', newline='') as f:
        w = csv.DictWriter(f, fieldnames=list(resultat[0]))
        w.writeheader()
        w.writerows(resultat)
    (desti / 'resum.json').write_text(json.dumps(resum, indent=2), encoding='utf-8')
    assert valida_lectura('0') == (0.0, None)
    assert resum['valides'] == 3 and resum['rebutjades'] == 4
    print('Intèrpret:', sys.executable)
    print(resum)
if __name__ == '__main__':
    main()
