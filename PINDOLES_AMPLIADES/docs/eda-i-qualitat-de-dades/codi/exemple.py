"""Auditoria d'una taula de sensors: no corregix silenciosament els extrems."""
from pathlib import Path
import pandas as pd

def main():
    raw = pd.DataFrame({'id': [1, 2, 2, 3, 4, 5, 6], 'sala': [' A ', 'a', 'a', 'B', 'B', 'C', 'C'], 'temperatura': ['20', '21', '21', None, '999', '23', 'error']})
    # Treballem sobre una còpia i conservem els valors originals.
    df = raw.copy()
    df['sala'] = df.sala.str.strip().str.upper()
    df['valor'] = pd.to_numeric(df.temperatura, errors='coerce')
    df['absent_origen'] = df.temperatura.isna()
    df['error_parseig'] = df.valor.isna() & ~df.absent_origen
    df['fora_rang'] = df.valor.notna() & ~df.valor.between(-20, 60)
    df['duplicat_excedent'] = df.duplicated('id', keep='first')
    # El cas conegut repetit és exacte; els conflictes exigirien una altra política.
    usable = df.loc[~df.duplicat_excedent & ~df.fora_rang & df.valor.notna()].copy()
    assert len(usable) == 3 and set(usable.id) == {1, 2, 5}
    report = {'files': len(df), 'absents': int(df.absent_origen.sum()), 'parseig': int(df.error_parseig.sum()), 'fora_rang': int(df.fora_rang.sum()), 'duplicats_excedents': int(df.duplicat_excedent.sum())}
    out = Path(__file__).resolve().parent / 'eixides'
    out.mkdir(exist_ok=True)
    df.to_csv(out / 'auditoria.csv', index=False)
    usable.to_csv(out / 'lectures-valides.csv', index=False)
    print(report)
    print('Files vàlides sense duplicar:', len(usable))
if __name__ == '__main__':
    main()
