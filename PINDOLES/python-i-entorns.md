---
title: Python I Entorns
---

# Python I Entorns

## Per què cal explicitar esta base

En este curs fem moltes coses amb `Python`, pero no convé suposar que tot l'alumnat arriba amb el mateix automatisme.

La idea d'esta píndola no és tornar a fer un curs sencer de programació general, sino assegurar una base comuna per a poder:

- llegir i escriure scripts simples
- treballar amb notebooks sense dependre sempre d'exemples copiats
- preparar dades i fer proves de modelatge
- construir APIs o demos d'IA sense bloquejos bàsics

## El nucli que sí hem de dominar

- variables i tipus habituals
- llistes, diccionaris, tuples i conjunts
- condicionals i bucles
- funcions
- imports
- lectura i escriptura de fitxers
- errors habituals i com llegir un traceback

No tots estos blocs tenen el mateix pes teòric, però tots tenen molt pes operatiu. En este curs, un alumne no es bloqueja tant per no saber una teoria molt abstracta com per no saber llegir una estructura de dades, separar una regla en una funció o entendre per què un script trenca en executar-se.

## Què significa realment "dominar la base"

No significa saber de memòria totes les instruccions del llenguatge.

Significa sobretot ser capaç de:

- llegir codi ja escrit i entendre què fa
- modificar una regla simple sense trencar el conjunt
- passar d'una idea verbal a una funció menuda
- detectar si un error és de dades, de sintaxi o de dependències

Dit d'una altra manera: volem autonomia funcional, no exhibició de llenguatge.

## Estructures que apareixen constantment al curs

### Llistes

```python
temperatures = [19.2, 20.1, 18.7]
```

Van bé quan l'ordre importa i volem recórrer elements.

### Diccionaris

```python
ticket = {
    "id": "T-014",
    "canal": "web",
    "prioritat": "alta"
}
```

Són especialment útils quan representem registres, respostes JSON o configuracions.

### Per què això és tan important en IA i dades

Una gran part del curs no tracta objectes "purs" de programació clàssica, sinó:

- registres de datasets
- missatges de sensors
- payloads d'API
- configuracions de model o d'escenari

Per això les llistes i els diccionaris no són només una base generalista. Són la forma concreta en què l'alumnat es trobarà la major part de les dades en treball real.

## Funcions: punt clau de maduresa

Quan una seqüència de passos comença a repetir-se, cal extraure-la a una funció.

```python
def classifica_risc(valor, llindar):
    if valor >= llindar:
        return "alerta"
    return "normal"
```

Ací el valor no és només que el codi quede més curt. El valor és que la regla es torna explícita, reutilitzable i fàcil de provar.

També hi ha una idea pedagògica important: quan l'alumnat escriu tota la lògica seguida, encara no està separant bé problema i solució. Quan comença a encapsular regles en funcions, normalment ja està pensant amb més estructura.

## Variables, tipus i conversions

En cursos com este, moltes errades no venen d'algorismes difícils, sinó de confondre tipus.

Exemples molt habituals:

- un nombre llegit com a text
- un camp buit que provoca error al convertir a `float`
- comparar una cadena amb un enter sense adonar-se'n

Exemple:

```python
valor = "18.5"
humitat = float(valor)
```

Si l'alumnat no entén esta conversió simple, després li costarà molt interpretar per què fallen els càlculs, els llindars o el preprocessament.

## Condicionals i bucles com a base de regla operativa

En projectes de dades i IA hi ha molt model, però també molta regla.

Per exemple:

- si la humitat baixa d'un llindar, genera alerta
- si el text d'un ticket conté cert patró, revisa'l
- si una fila té camps crítics buits, exclou-la o marca-la

Estos casos no demanen teoria sofisticada. Demanen bon ús de condicionals, bucles i estructura clara.

## Entorns de treball

En este curs treballarem sobretot amb:

- `Jupyter Notebook` per a exploració i proves
- `VS Code` per a scripts, APIs i projectes més estables
- entorns virtuals per a separar dependències

Exemple mínim:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install pandas scikit-learn matplotlib seaborn
```

La idea important no és el comandament en si, sinó què resol:

- separar dependències d'un projecte respecte a un altre
- evitar que una instal·lació "trenque" un entorn que ja funcionava
- poder explicar amb més claredat què necessita un notebook o una demo per executar-se

## Com llegir un error sense entrar en pànic

Quan un script falla, no convé llegir el terminal com si tot tinguera el mateix pes.

Sovint la part important és:

- l'últim missatge d'error
- la línia on ha fallat
- el tipus d'error: `NameError`, `KeyError`, `ValueError`, `ModuleNotFoundError`

Exemple mental:

- `ModuleNotFoundError`: falta una dependència o l'entorn no és el correcte
- `KeyError`: el camp o la clau no existix
- `ValueError`: el valor no té el format que esperàvem

Si l'alumnat aprén esta lectura mínima, guanya molta autonomia amb molt poca teoria extra.

## Error habitual

Instal·lar paquets de manera desordenada i no saber després en quin entorn funcionava cada cosa.

## Exemple guiat de classe

Situació:

en `Predicció Comercial`, volem llegir un CSV i marcar si una fila mereix revisió.

```python
def necessita_revisio(import_total, descompte):
    return import_total < 0 or descompte > 0.6
```

Encara no hi ha model ni dashboard. Però si esta base falla, després tot el pipeline es fa fràgil.

Podem ampliar la lectura així:

1. llegir la fila
2. decidir si hi ha incoherència
3. marcar-la per revisió
4. després, només després, pensar si això entra a model o a panell

El missatge docent és clar: abans d'usar ferramentes avançades, cal saber expressar una regla simple de negoci o qualitat.

## Pràctica guiada suggerida

Situació:

teniu un fitxer amb incidents de terminal o lectures de sensors i voleu marcar registres sospitosos.

Pas 1:

definiu una funció que revise una sola fila.

Pas 2:

recorreu una llista o conjunt de registres i guardeu els casos sospitosos.

Pas 3:

expliqueu per escrit:

- quina regla heu aplicat
- quins casos esteu marcant
- quins encara no sabeu resoldre amb una regla simple

Esta pràctica és molt millor que un exercici abstracte perquè connecta directament amb el tipus de lògica que apareix després a BiciTierra Market, P3 i P5.

## Mini pràctica

Pregunta:

quina estructura encaixa millor per a representar un ticket amb camps com `id`, `estat` i `canal`?

## Solució orientativa

Un diccionari, perquè volem accedir per nom de camp i la forma s'assembla molt a un registre JSON.

## Resum final

La base de `Python` no és un tràmit. És la capa que permet que la resta del curs siga realment operativa.

Si esta base és feble, qualsevol llibreria més avançada pareixerà màgia o bloqueig. Si esta base és suficient, la resta del curs es torna molt més explicable i manipulable.

## Com usar-la en estos projectes

- BiciTierra Market: abans d'entrar en `Pandas`, neteja i funcions simples de transformació
- P3: scripts menuts per simular sensors o validar payloads
- P5: utilitats, proves i serveis abans de la integració gran

## Vegeu també

- `Python per a Dades I`
- `Jupyter Notebooks`
- `Scikit-Learn Introductori`
