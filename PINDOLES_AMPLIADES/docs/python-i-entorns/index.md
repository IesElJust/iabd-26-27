---
title: "Python i entorns de treball"
description: "Fonaments, exemples reproduïbles i pràctica progressiva: python i entorns de treball."
tags: [IABD, dades, formació]
icon: material/book-open-page-variant
status: ampliada
---

# 01 · Python i entorns de treball

[← Índex de les píndoles](../index.md)

!!! abstract "Què aprendràs"
    - Distingir intèrpret, entorn i editor.
    - Escriure funcions amb entrades, eixides i errors explícits.
    - Llegir i guardar resultats amb rutes reproduïbles.

**Coneixements previs:** Cap coneixement previ de Python; saber crear carpetes i obrir una terminal.

**Dedicació orientativa:** 2–3 h per a lectura i laboratori guiat; les extensions i els exercicis autònoms requerixen temps addicional.

!!! tip "Dos recorreguts possibles"
    **Essencial:** llig els fonaments, executa el laboratori i completa la pràctica inicial. **Aprofundiment:** continua amb les pràctiques intermèdia i avançada i els exercicis. El professorat pot seleccionar-les segons els coneixements previs; no són totes obligatòries dins del projecte.

## Mapa de la unitat

Què significa programar amb Python → Variables, tipus i estructures → Decisions, repetició i funcions → Entorn virtual, dependències i intèrpret → Fitxers, rutes i errors → Llegir el programa de laboratori

## 1. Què significa programar amb Python

Un programa transforma unes entrades en uns resultats mitjançant instruccions. Per exemple, un sistema de sensors rep lectures textuals, les valida, calcula un resum i guarda un informe. El llenguatge permet expressar el procediment; l’intèrpret de Python executa les instruccions; el sistema operatiu proporciona fitxers, memòria i altres recursos.

El fitxer `.py` és text. No conté les biblioteques instal·lades ni les dades externes. Per compartir un programa cal explicar també com s’executa i de què depén. Una aplicació que funciona només en el terminal de qui l’ha escrita encara no és reproduïble.

Python és de tipatge dinàmic: el tipus pertany a l’objecte amb què treballem. Açò facilita l’experimentació, però no elimina la necessitat de distingir nombres, text, col·leccions i absències. El text `"12"` no es comporta com el nombre `12`.

```python title="Text, nombre i absència"
edat_text = "24"
edat = int(edat_text)
print(edat + 1)                 # 25
print(edat_text + "1")         # 241
lectura = None                 # Encara no hi ha cap lectura.
print(lectura is None)          # True
```

## 2. Variables, tipus i estructures

Un nom identifica un objecte. Assignar un nom nou a una llista no en crea necessàriament una còpia: dos noms poden referir-se a la mateixa col·lecció. Esta distinció és important quan una funció modifica les dades que rep.

| Estructura | Per a què resulta útil | Precaució |
|---|---|---|
| `int`, `float` | Comptatges i magnituds | Un decimal binari pot no representar exactament una quantitat monetària |
| `str` | Identificadors, missatges i dades de text | Un codi postal s’ha de conservar com a text |
| `bool` | Decisions amb dos valors | `False` no equival conceptualment a dada absent |
| `list` | Seqüència ordenada d’elements | És mutable i pot contindre tipus heterogenis |
| `tuple` | Agrupació de valors que no es reassignen per posició | La immutabilitat no transforma els objectes interiors |
| `dict` | Registre amb camps identificats per una clau | Cal decidir què passa si una clau no existeix |
| `set` | Valors únics i pertinença | No s’ha de basar una seqüència de treball en el seu ordre |

```python title="Referència compartida i còpia"
original = [10, 20]
alias = original
alias.append(30)
print(original)                # [10, 20, 30]
copia = original.copy()
copia.append(40)
print(original)                # Continua sense el 40.
```

La còpia anterior és superficial. Si la llista conté altres llistes, estes poden continuar compartides. Abans de recórrer a una còpia profunda, convé preguntar si el programa necessita modificar les estructures o podria construir un resultat nou.

## 3. Decisions, repetició i funcions

Una condició representa una regla del problema. En una sala frigorífica, «valor inferior a zero» pot ser correcte; en un recompte d’unitats, una quantitat negativa necessita una explicació. No hi ha una validació universal desconnectada del significat de la dada.

```python title="Una regla explícita i una funció reutilitzable"
def estat_estoc(unitats, minim):
    if unitats < 0:
        raise ValueError("L'estoc no pot ser negatiu en este model")
    if unitats < minim:
        return "reposar"
    return "suficient"

for unitats in [0, 4, 12]:
    print(unitats, estat_estoc(unitats, minim=5))
```

Una funció permet donar nom a una operació, delimitar entrades i eixides i verificar casos concrets. Una funció que retorna un resultat és més fàcil de reutilitzar que una que només l’imprimix. `print` és útil per comunicar; `return` permet continuar calculant.

Un bucle és apropiat per recórrer registres, aplicar una regla o coordinar passos. Quan arribem a arrays grans, estudiarem operacions vectorials. No cal eliminar els bucles per principi: primer s’ha d’entendre la correcció i, si cal, mesurar el rendiment.

## 4. Entorn virtual, dependències i intèrpret

Un entorn virtual separa les biblioteques d’un projecte de les d’altres projectes. No és una màquina virtual ni un contenidor: utilitza el sistema i un intèrpret base, amb un espai propi de paquets. Activar-lo modifica la manera de resoldre ordres en el terminal actual; també podem invocar-ne directament l’intèrpret.

```bash title="Preparar un entorn a Linux o macOS"
python3 -m venv .venv
source .venv/bin/activate
python -c "import sys; print(sys.executable)"
python -m pip --version
```

En Windows es pot crear amb `py -m venv .venv` i invocar `.venv\Scripts\python.exe` directament. Si PowerShell impedix l’activació, no cal alterar polítiques globals per seguir la pràctica: usa el camí de l’intèrpret.

`python -m pip` associa la instal·lació al Python seleccionat. El nom de l’ordre `pip`, sense més informació, pot correspondre a un altre entorn. Quan un import falla, comprova primer esta correspondència, no instal·les paquets repetidament a cegues.

Un fitxer de requisits comunica dependències; les versions fixades ajuden a repetir una execució, però també importen la versió de Python, el sistema i, de vegades, biblioteques natives. `pip freeze` descriu els paquets instal·lats: no és per si mateix una explicació de quins són necessaris.

## 5. Fitxers, rutes i errors

Una ruta relativa s’interpreta des del directori de treball. En un script, `Path(__file__).resolve().parent` localitza la carpeta del programa; en un notebook `__file__` no sol existir i cal establir la base explícitament. Confondre les dos situacions explica molts «fitxer no trobat».

```python title="Escriure text amb codificació explícita"
from pathlib import Path

base = Path.cwd() / "resultats"
base.mkdir(exist_ok=True)
(base / "nota.txt").write_text("Lectures revisades.\n", encoding="utf-8")
print((base / "nota.txt").read_text(encoding="utf-8"))
```

Llig el rastre de l’error des del tipus i missatge final, i localitza després la línia del teu programa. `ValueError` sol indicar un valor inadequat; `TypeError`, una operació amb tipus incompatibles; `KeyError`, una clau absent. La resposta no és envoltar tot el programa amb `except: pass`, perquè ocultaria la fallada.

Captura només l’error que pots gestionar i conserva informació suficient per revisar el registre. En una importació de dades, separar files vàlides i rebutjades pot ser millor que parar tot el procés o substituir tots els errors per zero.

## 6. Llegir el programa de laboratori

L’exemple descarregable valida temperatures d’un dispositiu fictici. Té quatre decisions deliberades: el zero és vàlid, el text buit és absent, el text no numèric és un error de format i una temperatura fora de rang es rebutja sense «arreglar-la» silenciosament.

La funció retorna una parella `(valor, error)`. El recorregut principal conserva el text original, calcula la mitjana només amb lectures vàlides i exporta l’auditoria. Això separa regla, coordinació i persistència. La mateixa estructura es pot aplicar a lectures industrials, formularis o imports d’un fitxer administratiu.

Observa també les comprovacions `assert`: exemplifiquen invariants en un laboratori. Per validar entrades externes en una aplicació, utilitza excepcions o comprovacions explícites; Python pot desactivar les assercions en mode optimitzat.

## Laboratori complet i reproduïble

**Context:** treballarem amb dades sintètiques creades pel mateix programa. No cal descarregar datasets ni usar els CSV de BiciTierra. Els valors servixen per aprendre i comprovar procediments; no descriuen una població real.

**Materials:** Python 3.10 o superior, un entorn virtual i els [requisits de la unitat](requirements.txt). Consulta la [preparació comuna](../index.md) abans d’instal·lar-los.

Des de la carpeta d’esta píndola, amb l’entorn activat:

```bash
python -m pip install -r requirements.txt
python codi/exemple.py
```

Esta unitat usa només la biblioteca estàndard: el fitxer de requisits està buit i no cal instal·lar paquets.

El programa crea `codi/eixides/`. Pots examinar les eixides sense modificar el codi original. Per resoldre les variants, treballa sobre una còpia i actualitza les comprovacions quan canvies deliberadament les dades.

### Exemple comentat

[Obri o descarrega el programa complet](codi/exemple.py). Cada comprovació `assert` expressa una propietat esperada de les dades de demostració; si falla, investiga la causa abans d’eliminar-la.

```python title="codi/exemple.py" linenums="1"
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
```

## Pràctiques guiades

Cada pràctica deixa una evidència petita: una eixida comprovada i una explicació de la decisió. Els temps són orientatius i no inclouen instal·lació.

### Pràctica 1 · Identificar l’entorn

**Nivell i temps:** Inicial · 20–30 min.

**Objectiu:** Comprovar quin Python executa el treball abans d’instal·lar dependències.

**Materials:** exemple comentat d’esta unitat, les seues eixides i una còpia de treball per a les modificacions.

**Procediment:**

1. Crea una carpeta de laboratori i un entorn virtual seguint les instruccions de l’índex general. Anota la versió de Python.
2. Activa l’entorn i executa `python -c "import sys; print(sys.executable)"`. Guarda la ruta en una nota.
3. Executa l’exemple des de la carpeta de la píndola i compara la ruta impresa amb l’anterior.
4. Obri `codi/eixides/resum.json` i localitza recompte i mitjana. Relaciona cada camp amb la línia que el calcula.

!!! success "Comprovació i evidència esperada"
    La ruta correspon a l’entorn activat; hi ha 3 lectures vàlides, 4 rebutjades i una mitjana aproximada de 13,17.

**Preguntes de reflexió:**

- Quina diferència hi ha entre instal·lar Python i crear un entorn?
- Per què un paquet pot estar disponible en la terminal i no en l’editor?
- Quina informació mínima permetria a una companya reproduir el resultat?

**Ampliació opcional:** Executa el programa amb una ruta absoluta des d’una altra carpeta i comprova on es guarden les eixides.

### Pràctica 2 · Validar sense perdre informació

**Nivell i temps:** Intermèdia · 30–45 min.

**Objectiu:** Distingir valor zero, absència, format incorrecte i valor fora del rang acordat.

**Materials:** exemple comentat d’esta unitat, les seues eixides i una còpia de treball per a les modificacions.

**Procediment:**

1. Fes una còpia de treball del programa i afegix les entrades `" -5 "`, `None`, `"inf"` i `"80"`.
2. Abans d’executar, escriu el resultat esperat de cada entrada segons el contracte de la funció.
3. Invoca `valida_lectura` individualment amb cada cas i compara la parella valor/error.
4. Actualitza les comprovacions del resum de la còpia perquè reflectisquen les noves entrades. Conserva la columna original en el CSV.

!!! success "Comprovació i evidència esperada"
    −5 i 80 són vàlids; None és absent i infinit queda fora de rang. La funció no confon zero amb absència.

**Preguntes de reflexió:**

- Per què `if valor` seria inadequat per a detectar una lectura vàlida?
- Quina diferència hi ha entre l’entrada original i el valor convertit?
- Què passaria si capturàrem qualsevol excepció sense informar-ne?

**Ampliació opcional:** Afig una regla que accepte coma decimal i documenta quins formats podrien resultar ambigus.

### Pràctica 3 · Un resum robust

**Nivell i temps:** Avançada · 45–60 min.

**Objectiu:** Adaptar el càlcul a un conjunt sense lectures acceptades.

**Materials:** exemple comentat d’esta unitat, les seues eixides i una còpia de treball per a les modificacions.

**Procediment:**

1. Crea una llista formada només per entrades invàlides en una còpia del programa.
2. Executa-la i identifica per què el càlcul de la mitjana falla abans d’arribar a les comprovacions.
3. Definix el comportament esperat: mitjana absent i un missatge clar quan no hi ha lectures vàlides.
4. Modifica només el càlcul necessari, adapta les assercions i comprova tant el cas buit com el conjunt original.

!!! success "Comprovació i evidència esperada"
    El programa no dividix entre zero; el JSON expressa absència amb `null` i conserva els recomptes.

**Preguntes de reflexió:**

- Per què una mitjana zero seria enganyosa en este cas?
- Quina responsabilitat correspon a la funció de validació i quina al resum?
- Quins casos límit afegiries abans de reutilitzar el programa?

**Ampliació opcional:** Separa validació, resum i escriptura en tres funcions i descriu les entrades i eixides de cadascuna.

## Exercicis autònoms

Intenta resoldre cada repte abans de desplegar l’orientació. Es valora el raonament i les comprovacions, no només obtindre una xifra.

### Repte 1 · Un nou sensor

Adapta la validació a percentatges d’humitat entre 0 i 100. Prova extrems, absències i un text invàlid.

??? example "Solució orientativa i criteri de revisió"
    Canvia el contracte i el rang, no només el nom de la variable. 0 i 100 han de ser vàlids; −1 i 101 no. Conserva el motiu de rebuig.

### Repte 2 · Funció sense efectes laterals

Escriu una funció que reba una llista de valors vàlids i retorne recompte i mitjana sense escriure fitxers.

??? example "Solució orientativa i criteri de revisió"
    La funció retorna un diccionari; la capa exterior decidix com guardar-lo. Amb llista buida, usa una mitjana absent. Això permet comprovar el càlcul independentment del disc.

### Repte 3 · Informe de qualitat

Genera recomptes per tipus d’error i comprova que acceptats més rebutjats coincidix amb entrades.

??? example "Solució orientativa i criteri de revisió"
    Agrupa pel camp error, mantenint una categoria per a acceptats. La suma dels grups ha de coincidir amb la longitud original si cada entrada té un únic resultat de validació.

## Errors habituals i diagnòstic

| Símptoma | Causa que convé investigar | Comprovació o correcció |
|---|---|---|
| Paquet no trobat | S’està usant un altre intèrpret. | Comprova sys.executable i instal·la amb python -m pip dins de l’entorn. |
| Fitxer en una carpeta inesperada | Ruta relativa dependent de la terminal. | Construïx la ruta des de __file__ o una base explícita. |
| Divisió entre zero | No hi ha lectures acceptades. | Definix el resultat buit abans de calcular la mitjana. |

## Autoavaluació i evidències

Abans de donar la unitat per treballada, comprova estos punts i escriu una frase d’evidència per a cadascun:

- [ ] Puc distingir intèrpret, entorn i editor.
- [ ] Puc escriure funcions amb entrades, eixides i errors explícits.
- [ ] Puc llegir i guardar resultats amb rutes reproduïbles.
- [ ] He executat el laboratori i he contrastat almenys un resultat independentment.
- [ ] Puc explicar una limitació i un cas en què el procediment requeriria canvis.

**Lliurable de la píndola:** còpia de treball reproduïble, resultats de la pràctica seleccionada i un text breu que indique pregunta, decisió, comprovació i limitació. Si s’usa dins de BiciTierra Market, integra esta evidència en el lliurable setmanal corresponent; no cal crear una entrega duplicada.

## Fonts per aprofundir

- [Documentació oficial de referència](https://docs.python.org/3/tutorial/venv.html). Consulta especialment els conceptes i els supòsits descrits en la unitat.

Les versions executades i els límits de la comprovació estan en el [registre de validació](../VALIDACIO.md). Els exemples són originals i les dades són sintètiques.

## Aplicació final a BiciTierra Market

**Moment orientatiu:** setmana 1. Esta correspondència ajuda a triar materials i no substituïx el document de treball de l’alumnat.

Prepara l’entorn de treball i comprova les rutes abans d’obrir els CSV de BiciTierra. Reutilitza la distinció entre dada absent i zero en vendes. No copies el rang de temperatures: cada columna del projecte necessita el seu propi contracte.

**Transferència:** identifica quin concepte acabes de practicar, quina dada del projecte l’exigix i què has de canviar respecte del laboratori. Justifica eixa adaptació abans de copiar codi.
