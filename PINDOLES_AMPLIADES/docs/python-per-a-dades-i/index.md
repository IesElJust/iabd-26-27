---
title: "NumPy i pandas: de les dades a les taules"
description: "Fonaments, exemples reproduïbles i pràctica progressiva: numpy i pandas: de les dades a les taules."
tags: [IABD, dades, formació]
icon: material/book-open-page-variant
status: ampliada
---

# 03 · NumPy i pandas: de les dades a les taules

[← Índex de les píndoles](../index.md)

!!! abstract "Què aprendràs"
    - Treballar amb arrays i operacions vectoritzades.
    - Filtrar, agrupar i unir taules conservant la granularitat.
    - Tractar dates i absències sense confondre-les amb zeros.

**Coneixements previs:** Python bàsic i noció de files i columnes.

**Dedicació orientativa:** 3–4 h per a lectura i laboratori guiat; les extensions i els exercicis autònoms requerixen temps addicional.

!!! tip "Dos recorreguts possibles"
    **Essencial:** llig els fonaments, executa el laboratori i completa la pràctica inicial. **Aprofundiment:** continua amb les pràctiques intermèdia i avançada i els exercicis. El professorat pot seleccionar-les segons els coneixements previs; no són totes obligatòries dins del projecte.

## Mapa de la unitat

De la dada a la taula → Arrays, dimensions i broadcasting → Series, DataFrame i índex → Llegir i seleccionar dades → Tipus, nuls i transformacions → Agregar amb un denominador correcte → Unions i concatenacions → Dates, resums temporals i retards

## 1. De la dada a la taula

Abans d’escollir una funció cal entendre què representa una fila. Una taula pot contindre persones, transaccions, mesures de sensors o resums mensuals. Barrejar estos nivells sense una regla produïx errors que cap biblioteca detectarà automàticament.

NumPy proporciona arrays numèrics i operacions sobre dimensions. Pandas aporta `Series` i `DataFrame`, amb etiquetes, índexs i operacions tabulars. El primer és convenient per a càlcul numèric regular; el segon, per a dades amb camps de tipus diferents i claus. Les dos biblioteques es complementen, però no tenen exactament les mateixes regles d’alineació.

## 2. Arrays, dimensions i broadcasting

Un array té una forma, un nombre de dimensions i un tipus de dada. La forma `(3,)` representa tres elements; `(3, 1)` representa tres files i una columna. Esta diferència afecta operacions i interfícies de models.

```python title="Formes i operacions NumPy"
import numpy as np

minuts = np.array([30., 60., 90.])
print(minuts.shape)                    # (3,)
print(minuts / 60)                     # [0.5, 1.0, 1.5]
matriu = np.array([[1, 2, 3], [4, 5, 6]])
print(matriu + np.array([10, 20, 30]))  # Suma per columnes.
```

El *broadcasting* compara dimensions des de la dreta: són compatibles si són iguals o una d’elles és 1. Un vector de forma `(3,)` i una columna `(3,1)` poden generar una matriu `(3,3)`, no una resta element a element. Comprova la forma abans i després d’un càlcul; un resultat numèric no prova que s’haja calculat allò que esperaves.

Una altra distinció és l’eix. `axis=0` agrega al llarg de les files i retorna un valor per columna; `axis=1` agrega les columnes de cada fila. Escriure abans «vull una mitjana per persona» ajuda a escollir l’operació adequada.

## 3. Series, DataFrame i índex

Una `Series` és una seqüència etiquetada. Un `DataFrame` combina columnes amb un índex de files. L’índex no és necessàriament una clau de negoci: pot ser només el comptador creat en carregar un fitxer.

```python title="L’alineació es fa per etiqueta"
import pandas as pd

a = pd.Series([10, 20], index=["web", "correu"])
b = pd.Series([1, 2], index=["correu", "web"])
print(a + b)  # correu: 21; web: 12, segons les etiquetes.
```

Convertir a NumPy elimina les etiquetes. És útil quan una API requerix arrays, però obliga a garantir que files i columnes mantenen l’ordre correcte. No convertisques per ocultar un problema d’alineació sense investigar-lo.

## 4. Llegir i seleccionar dades

La càrrega ha de fer explícits codificació, separador, decimals i dates quan puguen ser ambigus. Un identificador com `00127` pot perdre zeros inicials si es convertix automàticament a enter. Un `head()` correcte no demostra que totes les files s’hagen interpretat bé.

```python title="Construcció i selecció reproduïble"
import pandas as pd

df = pd.DataFrame({"id":["001","002","003"],
                   "servei":["web","vpn","web"],
                   "minuts":[20, 50, 35]})
web = df.loc[df["servei"].eq("web"), ["id","minuts"]].copy()
web["hores"] = web["minuts"] / 60
print(web)
```

`loc` selecciona per etiqueta; `iloc`, per posició. En una selecció booleana amb diverses condicions, usa parèntesis i `&`, `|` o `~`. Una còpia explícita deixa clara la intenció de treballar amb una taula derivada. Per modificar la taula original, fes una assignació única amb `.loc` en lloc d’encadenar seleccions.

## 5. Tipus, nuls i transformacions

Un nul significa informació no disponible, no necessàriament zero. La mitjana de [10, nul, 20] sobre valors observats és 15; omplir el nul amb zero la convertiria en 10 i canviaria la interpretació.

`pd.to_numeric(..., errors='coerce')` pot ser útil, però convertix a nul tant l’absència com el text que no s’ha pogut interpretar. Conserva una màscara d’error de conversió si la distinció importa. Les dates requerixen el mateix criteri.

```python title="Distingir absència i error de conversió"
import pandas as pd

text = pd.Series(["10", None, "error", "0"])
valor = pd.to_numeric(text, errors="coerce")
error_format = valor.isna() & text.notna()
print(pd.DataFrame({"original":text,"valor":valor,"error_format":error_format}))
```

La imputació per mediana o mitjana és una decisió analítica. En aprenentatge automàtic, la regla s’ajusta amb entrenament i després s’aplica a validació i prova. Una transformació aparentment simple pot filtrar informació si es calcula sobre tot el conjunt.

## 6. Agregar amb un denominador correcte

`groupby` separa grups, aplica una operació i reunix resultats. `size` compta files; `count` compta valors no nuls del camp. Quan hi ha nuls, les dos xifres expliquen coses diferents.

Una taxa global no és sempre la mitjana de taxes de grup. Si un equip resol 9 de 10 casos i un altre 1 de 100, la taxa conjunta és 10/110, no la mitjana de 90% i 1%. Calcula numerador i denominador compatibles abans d’agregar percentatges.

Amb `sum(min_count=1)`, un grup sense cap valor observat pot conservar el nul en lloc de convertir-se en zero. Una taula dinàmica també pot generar cel·les absents: no les ompligues automàticament si no saps si representen absència d’activitat o de registre.

## 7. Unions i concatenacions

Una unió associa files per una clau; una concatenació apila o alinea taules. Dos camps amb el mateix nom no demostren que existisca una relació vàlida.

El paràmetre `validate='many_to_one'` comprova que la taula de dimensió té una sola fila per clau. `indicator=True` permet detectar files sense correspondència. Comprova també el nombre de files i els totals abans i després de la unió.

En el laboratori, les incidències es relacionen amb el catàleg de serveis. «vpn» no té responsable registrat; una unió esquerra conserva la incidència i exposa el buit. Una unió interna l’eliminaria, reduint silenciosament el volum analitzat.

## 8. Dates, resums temporals i retards

Ordenar text de data només funciona en formats dissenyats per mantindre l’ordre, com ISO. Converteix a data quan necessites períodes, diferències o regles temporals. El canvi de zona horària és una altra decisió: una data local sense zona pot ser ambigua en registres distribuïts.

`resample('MS')` agrupa en períodes mensuals etiquetats a l’inici. `rolling(3)` opera sobre tres observacions; no significa sempre tres mesos. Si falten períodes, una finestra de files no equival a una finestra de temps.

Per a un predictor retardat, ordena per entitat i temps abans de `groupby(...).shift(1)`. Una mitjana mòbil predictiva ha de desplaçar-se perquè no incloga el resultat del moment que pretén anticipar. Estes regles importen en energia, demanda, incidències i moltes altres dades amb dependència temporal.

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

[Obri o descarrega el programa complet](codi/exemple.py). Cada comprovació `assert` expressa una propietat esperada de les dades de demostració; si falla, investiga la causa abans d’eliminar-la.

```python title="codi/exemple.py" linenums="1"
"""Taules i arrays: unió controlada d'incidències amb serveis."""
from pathlib import Path
import numpy as np
import pandas as pd

def main():
    temps = np.array([20.0, 30.0, 50.0])
    assert temps.shape == (3,)
    print('Minuts a hores:', temps / 60)
    incidencies = pd.DataFrame({'id': [1, 2, 3, 4, 5], 'servei': ['web', 'web', 'correu', 'correu', 'vpn'], 'minuts': [20.0, 30.0, None, 50.0, 10.0], 'data': ['2026-01-01', '2026-01-03', '2026-02-01', '2026-02-03', '2026-02-04']})
    serveis = pd.DataFrame({'servei': ['web', 'correu'], 'responsable': ['Equip A', 'Equip B']})
    incidencies['data'] = pd.to_datetime(incidencies['data'], format='%Y-%m-%d')
    # Exigim una sola coincidència de catàleg per incidència.
    resultat = incidencies.merge(serveis, on='servei', how='left', validate='many_to_one', indicator=True)
    assert len(resultat) == 5
    assert (resultat['_merge'] == 'left_only').sum() == 1
    # size compta files; count només valors no absents.
    resum = resultat.groupby('servei', dropna=False).agg(files=('id', 'size'), observades=('minuts', 'count'), mitjana=('minuts', 'mean'))
    # min_count evita presentar absència completa com a suma zero.
    mensual = incidencies.set_index('data')['minuts'].resample('MS').sum(min_count=1)
    out = Path(__file__).resolve().parent / 'eixides'
    out.mkdir(exist_ok=True)
    resultat.to_csv(out / 'incidencies.csv', index=False)
    resum.to_csv(out / 'resum-serveis.csv')
    print(resum.to_string())
    print('Totals mensuals observats:\n', mensual)
    print('Nuls conservats:', resultat.minuts.isna().sum())
if __name__ == '__main__':
    main()
```

## Pràctiques guiades

Cada pràctica deixa una evidència petita: una eixida comprovada i una explicació de la decisió. Els temps són orientatius i no inclouen instal·lació.

### Pràctica 1 · Comptar allò que hi ha i allò que falta

**Nivell i temps:** Inicial · 20–30 min.

**Objectiu:** Distingir files totals de valors observats dins de cada grup.

**Materials:** exemple comentat d’esta unitat, les seues eixides i una còpia de treball per a les modificacions.

**Procediment:**

1. Executa el laboratori i obri `resum-serveis.csv`.
2. Reconstruïx manualment el grup correu: dos registres, un valor de minuts absent i un valor 50.
3. Compara les columnes `files`, `observades` i `mitjana`. Calcula què passaria si imputàrem zero.
4. Escriu una nota que diferencie la mitjana observada de la mitjana que s’obtindria amb aquella imputació.

!!! success "Comprovació i evidència esperada"
    Correu té 2 files, 1 valor observat i mitjana 50; substituir l’absència per zero produiria 25.

**Preguntes de reflexió:**

- Per què `size` i `count` donen resultats diferents?
- És legítim considerar l’absència com a zero?
- Quina dada faltaria per decidir una imputació?

**Ampliació opcional:** Afig una columna de percentatge d’absències per servei.

### Pràctica 2 · Unir taules amb un contracte

**Nivell i temps:** Intermèdia · 30–45 min.

**Objectiu:** Verificar cobertura i cardinalitat d’una unió abans d’usar-la.

**Materials:** exemple comentat d’esta unitat, les seues eixides i una còpia de treball per a les modificacions.

**Procediment:**

1. Localitza la unió amb `validate="many_to_one"` i explica què exigix al catàleg.
2. Identifica el registre VPN sense correspondència a partir de `_merge`.
3. En una còpia, duplica el servei web dins del catàleg i executa la unió per observar l’error.
4. Restaura la unicitat i incorpora VPN amb un responsable explícit. Actualitza la comprovació de cobertura.

!!! success "Comprovació i evidència esperada"
    El catàleg duplicat es rebutja; amb tres serveis únics la unió conserva 5 files i no queda cap `left_only`.

**Preguntes de reflexió:**

- Quin total podria inflar-se si eliminàrem el control de cardinalitat?
- Quan tindria sentit una unió molts a molts?
- Per què una unió esquerra facilita auditar registres sense catàleg?

**Ampliació opcional:** Compara una unió interna i una esquerra sobre el catàleg original i explica quina fila desapareix.

### Pràctica 3 · Resumir per períodes

**Nivell i temps:** Avançada · 45–60 min.

**Objectiu:** Construir un agregat mensual que conserve el significat dels nuls.

**Materials:** exemple comentat d’esta unitat, les seues eixides i una còpia de treball per a les modificacions.

**Procediment:**

1. Revisa la conversió explícita de dates i l’ús de `resample("MS")`.
2. Comprova a mà els totals observats de gener i febrer: 50 i 60 minuts.
3. Crea un mes addicional amb totes les durades absents i usa `sum(min_count=1)`.
4. Exporta un resum amb total observat i recompte de durades disponibles, i redacta una nota de qualitat.

!!! success "Comprovació i evidència esperada"
    El mes sense cap durada observada queda absent, no com un zero de treball.

**Preguntes de reflexió:**

- Quina diferència hi ha entre cap fila i files sense durada?
- Per què cal ordenar o indexar correctament les dates?
- Quina informació es perd quan només exportem la suma?

**Ampliació opcional:** Agrupa alhora per mes i servei i comprova que la suma dels totals observats coincidix amb la del conjunt.

## Exercicis autònoms

Intenta resoldre cada repte abans de desplegar l’orientació. Es valora el raonament i les comprovacions, no només obtindre una xifra.

### Repte 1 · Un grup sense valors

Crea tres files d’un servei nou amb minuts absents i compara size, count, mean i sum(min_count=1).

??? example "Solució orientativa i criteri de revisió"
    Obtindràs 3 files, 0 observacions, mitjana absent i suma absent. Una suma zero sense min_count podria ocultar que no s’ha observat cap durada.

### Repte 2 · Claus compostes

Dissenya una unió entre lectures i catàleg quan un mateix codi de sensor es repetix en edificis diferents.

??? example "Solució orientativa i criteri de revisió"
    La clau pot ser edifici més sensor si eixa combinació identifica una única entrada de catàleg. Comprova unicitat i usa les dues columnes en la unió.

### Repte 3 · Vectoritzar una regla

Crea una columna booleana per a durades observades superiors a 45 minuts sense recórrer files amb un bucle.

??? example "Solució orientativa i criteri de revisió"
    Usa una màscara sobre la sèrie i decidix explícitament com representar absències. Si marques els nuls com False, documenta que significa no confirmat, no durada curta demostrada.

## Errors habituals i diagnòstic

| Símptoma | Causa que convé investigar | Comprovació o correcció |
|---|---|---|
| Augment de files després d’unir | Clau duplicada en el catàleg. | Comprova unicitat i validate abans d’agregar. |
| Mitjana massa baixa | Absències substituïdes per zero sense justificació. | Conserva absències i informa del recompte observat. |
| Dates mal interpretades | Format o configuració regional ambigua. | Indica format i comprova dates que distingisquen dia de mes. |

## Autoavaluació i evidències

Abans de donar la unitat per treballada, comprova estos punts i escriu una frase d’evidència per a cadascun:

- [ ] Puc treballar amb arrays i operacions vectoritzades.
- [ ] Puc filtrar, agrupar i unir taules conservant la granularitat.
- [ ] Puc tractar dates i absències sense confondre-les amb zeros.
- [ ] He executat el laboratori i he contrastat almenys un resultat independentment.
- [ ] Puc explicar una limitació i un cas en què el procediment requeriria canvis.

**Lliurable de la píndola:** còpia de treball reproduïble, resultats de la pràctica seleccionada i un text breu que indique pregunta, decisió, comprovació i limitació. Si s’usa dins de BiciTierra Market, integra esta evidència en el lliurable setmanal corresponent; no cal crear una entrega duplicada.

## Fonts per aprofundir

- [Documentació oficial de referència](https://pandas.pydata.org/docs/user_guide/merging.html). Consulta especialment els conceptes i els supòsits descrits en la unitat.

Les versions executades i els límits de la comprovació estan en el [registre de validació](../VALIDACIO.md). Els exemples són originals i les dades són sintètiques.

## Aplicació final a BiciTierra Market

**Moment orientatiu:** setmana 1–2. Esta correspondència ajuda a triar materials i no substituïx el document de treball de l’alumnat.

Carrega els CSV del projecte, verifica claus i granularitat abans d’unir-los i construïx agregats mensuals amb recompte d’observacions. No pressuposes que el fitxer de clients es pot unir directament a vendes agregades sense una clau i una relació justificades.

**Transferència:** identifica quin concepte acabes de practicar, quina dada del projecte l’exigix i què has de canviar respecte del laboratori. Justifica eixa adaptació abans de copiar codi.
