---
title: "Validació: mesurar allò que realment volem predir"
description: "Fonaments, exemples reproduïbles i pràctica progressiva: validació: mesurar allò que realment volem predir."
tags: [IABD, dades, formació]
icon: material/book-open-page-variant
status: ampliada
---

# 07 · Validació: mesurar allò que realment volem predir

[← Índex de les píndoles](../index.md)

!!! abstract "Què aprendràs"
    - Seleccionar particions segons temps, grups o independència.
    - Evitar informació futura en retards i transformacions.
    - Interpretar mètriques globals i per grup.

**Coneixements previs:** Pipeline supervisat i càlcul de MAE.

**Dedicació orientativa:** 4–5 h per a lectura i laboratori guiat; les extensions i els exercicis autònoms requerixen temps addicional.

!!! tip "Dos recorreguts possibles"
    **Essencial:** llig els fonaments, executa el laboratori i completa la pràctica inicial. **Aprofundiment:** continua amb les pràctiques intermèdia i avançada i els exercicis. El professorat pot seleccionar-les segons els coneixements previs; no són totes obligatòries dins del projecte.

## Mapa de la unitat

Validar és simular una situació futura → Tres famílies de separació → Fuga d’informació → Retards i finestres → Backtesting i panells → Errors en unitats i en proporció → Sobreajust, selecció i incertesa → Lectura del laboratori

## 1. Validar és simular una situació futura

La validació pregunta com es comportarà el procediment davant de dades que no ha utilitzat per aprendre ni per triar decisions. La dificultat principal és definir què significa «nou»: una altra fila, una altra persona, un altre centre o un moment posterior.

Si entrenem amb lectures d’una màquina i provem amb lectures quasi idèntiques de la mateixa màquina, estem mesurant una capacitat distinta de la que necessitaríem en una màquina desconeguda. La partició forma part de la definició del problema.

Entrenament ajusta; validació selecciona; prova estima el resultat final. En conjunts petits, la validació creuada aprofita diverses particions, però no autoritza a ignorar temps, grups o disponibilitat de variables.

## 2. Tres famílies de separació

| Disseny | Quan té sentit | Risc si s’aplica fora de context |
|---|---|---|
| Aleatori | Observacions aproximadament independents i mateixa població d’ús | Mesclar informació de la mateixa entitat o del futur |
| Per grups | Pacients, persones, centres o dispositius que no han de compartir-se | Mesurar memorització d’entitats conegudes |
| Temporal | Predir períodes posteriors amb informació anterior | Ajustar amb futur i provar amb passat |

Una estratificació manté proporcions de classes, però no elimina dependència entre observacions. Si una persona apareix moltes vegades, separar per classe no impedix que la mateixa persona estiga en entrenament i prova.

La validació creuada anidada separa selecció de paràmetres i estimació de rendiment, però també ha d’adaptar el disseny intern i extern a la dependència de les dades. No és un remei automàtic per a un dataset mal definit.

## 3. Fuga d’informació

La fuga apareix quan el model o el procés de selecció accedix a informació que no estaria disponible en l’ús previst. Pot ser directa, com un import calculat a partir de la resposta, o subtil, com escalar amb el conjunt de prova.

Exemples: predir cancel·lació amb la data de cancel·lació; predir demora amb el temps final de resolució; seleccionar variables amb correlacions calculades sobre la prova; usar una mitjana mòbil que inclou el mateix valor que es vol anticipar.

Per cada predictor, anota el moment en què es coneix. Una columna present en un extracte actual no era necessàriament coneguda al començament de cada període històric. El contracte temporal ha de ser explícit.

## 4. Retards i finestres

Un retard d’una fila només equival a un retard d’un període si la sèrie està ordenada i no falten períodes. En un panell amb moltes entitats, el desplaçament s’ha de calcular dins de cada grup.

```python title="Un retard que no travessa edificis"
import pandas as pd

df = pd.DataFrame({"edifici":["A","A","B","B"],
                   "mes":[1,2,1,2],"consum":[100,120,80,90]})
df = df.sort_values(["edifici","mes"])
df["lag1"] = df.groupby("edifici")["consum"].shift(1)
print(df)
```

En predicció d’un mes vista, el valor real del mes anterior es pot incorporar quan ja ha sigut observat. En una predicció de sis mesos feta hui, els valors reals dels cinc mesos intermedis encara no existeixen: cal un esquema recursiu, directe o un altre disseny justificat.

Per això un bon resultat en avaluació mensual successiva no es pot presentar com una validació de sis mesos a l’avançada.

## 5. Backtesting i panells

El *backtesting* repetix l’ajust amb diversos punts de tall històrics. Una finestra expansiva incorpora tot el passat disponible; una finestra lliscant conserva només un tram recent. La primera aprofita més observacions; la segona pot adaptar-se a canvis, a costa de menys dades.

En un panell mensual, totes les files d’un mes han d’anar al mateix bloc si la pregunta és anticipar un mes complet. Aplicar directament un separador sobre índexs de files pot dividir un mateix mes entre entrenament i validació. La documentació de [TimeSeriesSplit](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.TimeSeriesSplit.html) descriu el separador; el nostre laboratori construïx els talls per dates per respectar el panell.

Un interval de separació pot ser necessari si les etiquetes arriben amb retard o les finestres de característiques se solapen. La seua longitud ha de respondre al procés, no a una regla decorativa.

## 6. Errors en unitats i en proporció

MAE és la mitjana de `|real − predicció|`. WAPE dividix l’error absolut total pel total absolut observat. MAE manté unitats; WAPE permet una lectura relativa del volum conjunt, però dóna més pes als grups grans.

```python title="Mètriques amb casos concrets"
import numpy as np

real = np.array([10., 20., 0.])
pred = np.array([12., 18., 1.])
mae = np.abs(real-pred).mean()
wape = 100*np.abs(real-pred).sum()/np.abs(real).sum()
print(mae, wape)  # 1.666... i 16.666...%
```

Si el denominador global és zero, WAPE no està definit. MAPE té problemes quan hi ha valors reals zero o molt menuts. No amagues estos casos afegint una constant arbitrària sense explicar com canvia la mètrica.

A més de la mitjana global, revisa grups, quantils d’error i casos de fallada. Un model acceptable en conjunt pot ser poc útil per a un producte minoritari.

## 7. Sobreajust, selecció i incertesa

Un resultat excel·lent en entrenament i pitjor en validació pot indicar sobreajust, però també canvi de distribució o errors en el preprocessament. Diagnostica abans d’ajustar paràmetres.

Provar moltes alternatives i quedar-se amb la millor mètrica de validació introduïx optimisme en la selecció. Reserva una prova final i documenta quantes decisions s’han comparat. La variabilitat entre folds aporta informació, però no és automàticament un interval de confiança de qualsevol ús futur.

En sèries dependents, un bootstrap de files independents pot trencar l’estructura temporal. Si es vol estimar incertesa amb remostreig, s’ha de justificar la unitat de mostreig i la dependència conservada.

## 8. Lectura del laboratori

L’exemple conté 48 mesos de dos edificis. El primer any prepara un retard anual; dos talls de 2025 servixen per observar estabilitat i 2026 queda reservat. El model usa retards, una tendència i l’edifici, amb paràmetres fixats abans de la prova.

Les comprovacions asseguren que cap data d’entrenament apareix en validació. Això no demostra per si sol absència de totes les fugues: també cal revisar com s’han generat les variables. El propòsit és convertir el disseny experimental en una part visible del codi.

## Laboratori complet i reproduïble

**Context:** treballarem amb dades sintètiques creades pel mateix programa. No cal descarregar datasets ni usar els CSV de BiciTierra. Els valors servixen per aprendre i comprovar procediments; no descriuen una població real.

**Materials:** Python 3.10 o superior, un entorn virtual i els [requisits de la unitat](requirements.txt). Consulta la [preparació comuna](../index.md) abans d’instal·lar-los.

Des de la carpeta d’esta píndola, amb l’entorn activat:

```bash
python -m pip install -r requirements.txt
python codi/exemple.py
```

El programa crea `codi/eixides/`. Pots examinar les eixides sense modificar el codi original. Per resoldre les variants, treballa sobre una còpia i actualitza les comprovacions quan canvies deliberadament les dades.

### Exemple comentat

[Obri o descarrega el programa complet](codi/exemple.py){ download="exemple.py" }. Cada comprovació `assert` expressa una propietat esperada de les dades de demostració; si falla, investiga la causa abans d’eliminar-la.

```python title="codi/exemple.py" linenums="1"
"""Backtesting per dates completes d'un panell de dos edificis."""
from pathlib import Path
import numpy as np
import pandas as pd
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_absolute_error

def main():
    rng = np.random.default_rng(7)
    dates = pd.date_range('2023-01-01', periods=48, freq='MS')
    rows = []
    for (building, offset) in [('A', 0), ('B', 30)]:
        for (i, date) in enumerate(dates):
            rows.append({'data': date, 'edifici': building, 't': i, 'consum': 100 + offset + i * 0.8 + 12 * np.sin(2 * np.pi * i / 12) + rng.normal(0, 3)})
    df = pd.DataFrame(rows).sort_values(['edifici', 'data'])
    # Retards dins de cada edifici; les sèries són mensuals completes.
    df['lag1'] = df.groupby('edifici').consum.shift(1)
    df['lag12'] = df.groupby('edifici').consum.shift(12)
    df = df.dropna().copy()
    df['b'] = (df.edifici == 'B').astype(int)
    # lag1 pressuposa predicció successiva d’un mes, no sis mesos de colp.
    features = ['lag1', 'lag12', 't', 'b']
    # Els talls són per mesos complets, no per posició de fila.
    folds = [('2024-12-01', '2025-01-01', '2025-06-01'), ('2025-06-01', '2025-07-01', '2025-12-01')]
    results = []
    for (end, start, stop) in folds:
        tr = df[df.data <= end]
        va = df[df.data.between(start, stop)]
        assert tr.data.max() < va.data.min() and set(tr.data).isdisjoint(set(va.data))
        model = Ridge(alpha=1).fit(tr[features], tr.consum)
        results.append({'train_end': end, 'valid_start': start, 'files': len(va), 'mae_model': mean_absolute_error(va.consum, model.predict(va[features])), 'mae_lag12': mean_absolute_error(va.consum, va.lag12)})
    print(pd.DataFrame(results).round(3).to_string(index=False))
    # 2026 queda reservat: alpha s’ha fixat abans d’esta avaluació.
    train = df[df.data < '2026-01-01']
    test = df[df.data >= '2026-01-01']
    model = Ridge(alpha=1).fit(train[features], train.consum)
    pred = model.predict(test[features])
    mae = mean_absolute_error(test.consum, pred)
    wape = 100 * np.abs(test.consum - pred).sum() / np.abs(test.consum).sum()
    print(f'Test: MAE={mae:.3f}; WAPE={wape:.3f}%')
    out = Path(__file__).resolve().parent / 'eixides'
    out.mkdir(exist_ok=True)
    pd.DataFrame(results).to_csv(out / 'backtesting.csv', index=False)
    assert len(test) == 24 and len(results) == 2
if __name__ == '__main__':
    main()
```

## Pràctiques guiades

Cada pràctica deixa una evidència petita: una eixida comprovada i una explicació de la decisió. Els temps són orientatius i no inclouen instal·lació.

### Pràctica 1 · Dibuixar les particions

**Nivell i temps:** Inicial · 20–30 min.

**Objectiu:** Verificar que una pregunta temporal es traduïx en talls per dates.

**Materials:** exemple comentat d’esta unitat, les seues eixides i una còpia de treball per a les modificacions.

**Procediment:**

1. Executa el laboratori i obri `backtesting.csv`.
2. Representa en una línia temporal entrenament i validació dels dos folds, més la prova de 2026.
3. Comprova que cada mes aporta dues files i que no es dividix entre blocs.
4. Anota quantes files queden després de crear el retard anual i per què es perd el primer any.

!!! success "Comprovació i evidència esperada"
    Queden 72 files amb retards; cada validació semestral té 12 files i la prova anual en té 24.

**Preguntes de reflexió:**

- Per què 24 files de prova no equivalen a 24 mesos?
- Què canviaria si faltara un mes en un edifici?
- Per què no s’han de barrejar aleatòriament estes files?

**Ampliació opcional:** Afig una comprovació de periodicitat per edifici abans de calcular `shift`.

### Pràctica 2 · Comparar una referència temporal

**Nivell i temps:** Intermèdia · 30–45 min.

**Objectiu:** Valorar un model contra una regla disponible en el moment de predir.

**Materials:** exemple comentat d’esta unitat, les seues eixides i una còpia de treball per a les modificacions.

**Procediment:**

1. Compara el MAE de Ridge i del retard anual en cada fold.
2. Calcula l’error absolut per fila i resumix-lo per edifici.
3. Identifica si una millora global amaga un grup amb pitjor resultat.
4. Redacta un criteri de selecció que combine mitjana, estabilitat i ús previst, sense consultar noves alternatives sobre 2026.

!!! success "Comprovació i evidència esperada"
    La comparació inclou la regla estacional i mostra resultats per tall i per grup.

**Preguntes de reflexió:**

- Per què un model sofisticat pot perdre davant d’una regla estacional?
- Com influïx la tendència en una predicció basada en l’any anterior?
- Quina mètrica complementaria MAE si els volums foren molt diferents?

**Ampliació opcional:** Afig com a tercera referència el mes anterior, mantenint exactament les mateixes files d’avaluació.

### Pràctica 3 · Canviar l’horitzó canvia l’experiment

**Nivell i temps:** Avançada · 45–60 min.

**Objectiu:** Distingir prediccions successives d’un mes i una predicció conjunta de sis mesos.

**Materials:** exemple comentat d’esta unitat, les seues eixides i una còpia de treball per a les modificacions.

**Procediment:**

1. Tria el tall de desembre de 2024 i enumera la informació disponible en eixe instant.
2. Marca quins valors de `lag1` de febrer a juny de 2025 encara no es coneixen en eixe tall.
3. Explica per què l’avaluació del laboratori és d’un mes vista amb observacions successives, encara que use un bloc semestral.
4. Dissenya en pseudocodi una alternativa recursiva o directa per a sis mesos i declara com s’obtindrien els predictors.

!!! success "Comprovació i evidència esperada"
    La proposta no reutilitza valors reals intermedis com si foren coneguts al desembre.

**Preguntes de reflexió:**

- Quina fuga apareix si entreguem els sis mesos com una previsió feta al mateix temps?
- Com es poden acumular errors en un esquema recursiu?
- Quines variables futures podrien conéixer-se per calendari?

**Ampliació opcional:** Implementa dos passos recursius i compara’ls amb dos passos successius; etiqueta els resultats com a experiments diferents.

## Exercicis autònoms

Intenta resoldre cada repte abans de desplegar l’orientació. Es valora el raonament i les comprovacions, no només obtindre una xifra.

### Repte 1 · Quin separador?

Tria disseny per a lectures futures d’una màquina, nous pacients i habitatges independents.

??? example "Solució orientativa i criteri de revisió"
    Temporal per al futur de la màquina; per grup de pacient quan hi ha visites repetides; aleatori si els habitatges són realment independents i representen la població d’ús. Justifica possibles dependències addicionals.

### Repte 2 · Errors amb zeros

Calcula MAE i WAPE per a reals [0, 0] i prediccions [1, 2].

??? example "Solució orientativa i criteri de revisió"
    MAE és 1,5. WAPE no està definit perquè el denominador és zero. Informa del cas i no substituïsques el resultat per zero ni per un percentatge arbitrari.

### Repte 3 · Calendari incomplet

Explica què passa amb shift(12) si falta un mes dins d’una sèrie.

??? example "Solució orientativa i criteri de revisió"
    Desplaça dotze files, no necessàriament dotze mesos. Reindexa amb un calendari complet per entitat, conserva absències i decidix com gestionar-les abans de crear retards.

## Errors habituals i diagnòstic

| Símptoma | Causa que convé investigar | Comprovació o correcció |
|---|---|---|
| Resultat massa bo en futur | Retards o agregats amb dades encara desconegudes. | Anota disponibilitat de cada predictor al moment de tall. |
| Un mes apareix en dos blocs | Separació per files en un panell. | Construïx els blocs per dates completes. |
| Percentatge infinit o absent | Denominador zero en mètrica relativa. | Informa del cas i complementa amb errors absoluts. |

## Autoavaluació i evidències

Abans de donar la unitat per treballada, comprova estos punts i escriu una frase d’evidència per a cadascun:

- [ ] Puc seleccionar particions segons temps, grups o independència.
- [ ] Puc evitar informació futura en retards i transformacions.
- [ ] Puc interpretar mètriques globals i per grup.
- [ ] He executat el laboratori i he contrastat almenys un resultat independentment.
- [ ] Puc explicar una limitació i un cas en què el procediment requeriria canvis.

**Lliurable de la píndola:** còpia de treball reproduïble, resultats de la pràctica seleccionada i un text breu que indique pregunta, decisió, comprovació i limitació. Si s’usa dins de BiciTierra Market, integra esta evidència en el lliurable setmanal corresponent; no cal crear una entrega duplicada.

## Fonts per aprofundir

- [Documentació oficial de referència](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.TimeSeriesSplit.html). Consulta especialment els conceptes i els supòsits descrits en la unitat.

Les versions executades i els límits de la comprovació estan en el [registre de validació](../VALIDACIO.md). Els exemples són originals i les dades són sintètiques.

## Aplicació final a BiciTierra Market

**Moment orientatiu:** setmana 2, 3 i 5. Esta correspondència ajuda a triar materials i no substituïx el document de treball de l’alumnat.

Separa mesos complets de sales_history.csv i reserva un tram final abans de seleccionar models. Declara l’horitzó i comprova disponibilitat de retards per combinació. sales_forecast_input.csv és entrada per a una previsió futura, no una prova amb resultats reals coneguts.

**Transferència:** identifica quin concepte acabes de practicar, quina dada del projecte l’exigix i què has de canviar respecte del laboratori. Justifica eixa adaptació abans de copiar codi.
