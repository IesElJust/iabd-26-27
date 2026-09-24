---
title: "Exploració i qualitat de dades"
description: "Fonaments, exemples reproduïbles i pràctica progressiva: exploració i qualitat de dades."
tags: [IABD, dades, formació]
icon: material/book-open-page-variant
status: ampliada
---

# 04 · Exploració i qualitat de dades

[← Índex de les píndoles](../index.md)

!!! abstract "Què aprendràs"
    - Definir què representa cada fila.
    - Auditar absències, formats, duplicats i valors extrems.
    - Documentar decisions de neteja i les seues conseqüències.

**Coneixements previs:** Operacions bàsiques amb pandas.

**Dedicació orientativa:** 3–4 h per a lectura i laboratori guiat; les extensions i els exercicis autònoms requerixen temps addicional.

!!! tip "Dos recorreguts possibles"
    **Essencial:** llig els fonaments, executa el laboratori i completa la pràctica inicial. **Aprofundiment:** continua amb les pràctiques intermèdia i avançada i els exercicis. El professorat pot seleccionar-les segons els coneixements previs; no són totes obligatòries dins del projecte.

## Mapa de la unitat

Explorar és formular i contrastar preguntes → Dimensions de qualitat → Contracte de dades i granularitat → Nuls, errors de format i valors extrems → Distribucions i relacions → L’EDA també pot contaminar l’avaluació → Decisions de neteja amb traçabilitat → Com tancar una exploració

## 1. Explorar és formular i contrastar preguntes

L’anàlisi exploratòria de dades, o EDA, és el procés d’entendre una mostra abans de construir explicacions o models. Inclou estructura, qualitat, distribucions, relacions i límits de representativitat. No és una col·lecció obligatòria de gràfics: cada operació ha de respondre una pregunta.

En un servei d’atenció, una disminució del temps mitjà podria indicar millora, però també desaparició dels casos difícils del registre. En sensors, valors idèntics durant hores poden representar estabilitat o una lectura bloquejada. L’estadística necessita context de captura.

Comença amb tres frases: què representa una fila, de quina població prové i quina decisió volem ajudar a prendre. Després identifica qui genera la dada, amb quina freqüència i quins canvis de sistema poden afectar-la.

## 2. Dimensions de qualitat

| Dimensió | Pregunta de control | Exemple |
|---|---|---|
| Completesa | Falta informació necessària? | Sol·licituds sense data |
| Validesa | El valor complix el format i el domini? | Temperatura textual no convertible |
| Coherència | Dos camps compatibles concorden? | Data de tancament anterior a l’obertura |
| Unicitat | Hi ha repeticions d’una mateixa observació? | Dos registres amb la mateixa clau d’event |
| Actualitat | La dada correspon al període útil? | Catàleg de serveis desactualitzat |
| Cobertura | Queden fora grups o períodes rellevants? | Sensors d’una sola planta |

Una taula sense nuls pot tindre mala qualitat si tots els buits s’han convertit en zero. Igualment, una taula amb nuls pot ser útil si estan identificats i el procediment els tracta de manera coherent.

## 3. Contracte de dades i granularitat

Un contracte de dades descriu camps, tipus, unitats, claus, dominis i regles. No cal començar amb una plataforma complexa: una taula de definicions i unes comprovacions executables ja eviten moltes ambigüitats.

```python title="Comprovacions explícites sobre una taula menuda"
import pandas as pd

df = pd.DataFrame({"id":[1,2,3], "unitats":[2,0,5], "preu":[10.,8.,12.]})
assert df["id"].is_unique
assert df["unitats"].ge(0).all()
df["import"] = df["unitats"] * df["preu"]
print(df)
```

Estes assercions són comprovacions didàctiques. Una aplicació productiva ha de definir com rebutja, aïlla o registra les files invàlides, sense dependre que les assercions estiguen activades.

La granularitat determina la clau. En un sensor, pot ser dispositiu i instant; en vendes agregades, mes, canal i producte. No elimines duplicats per una columna que no identifica la unitat d’observació: dos pagaments d’un mateix client poden ser dos fets legítims.

## 4. Nuls, errors de format i valors extrems

Un valor absent pot deure’s a una fallada aleatòria, a una regla de negoci o a un procés selectiu. Si les incidències més complexes són les que no tenen temps registrat, calcular la mitjana només amb observades infrarepresenta la dificultat. La informació disponible no sempre permet identificar el mecanisme de falta de dades, però sí formular i comprovar hipòtesis.

Un valor extrem tampoc és necessàriament erroni. Una jornada de consum excepcional pot correspondre a una avaria real. Retallar automàticament amb `clip` altera les evidències. Primer comprova unitats, sensor, context, distribució i registres relacionats.

El rang interquartílic, IQR, és Q3−Q1. La regla Q1−1,5×IQR i Q3+1,5×IQR marca observacions per revisar; no és un criteri universal d’eliminació. En distribucions asimètriques pot assenyalar molts casos legítims.

## 5. Distribucions i relacions

La mitjana és sensible a extrems; la mediana descriu el centre per posició. Necessitem també dispersió i mida de mostra. Dos equips amb la mateixa mitjana poden tindre riscos molt diferents si un és estable i l’altre alterna resultats molt baixos i molt alts.

Examina quantils, histogrames i relacions entre variables. Desagrega quan el significat ho demane: una relació global pot desaparèixer o invertir-se quan es distingixen grups. La correlació lineal pròxima a zero no descarta una relació corba, i una correlació alta no prova una causa.

En una taula de centres educatius, l’associació entre recursos i incidències pot reflectir mida del centre. Abans de concloure que més recursos generen problemes, revisa denominadors, cobertura i variables de context.

## 6. L’EDA també pot contaminar l’avaluació

Si es trien variables perquè es veu que funcionen sobre el conjunt de prova, eixa prova ja ha influït en el model. La separació temporal o de grups s’ha de plantejar abans de l’exploració orientada a decisions predictives.

Es poden comprovar claus i formats globals per entendre l’extracte, però els patrons usats per triar models i transformacions han de procedir de l’entrenament i de la validació acordada. Documenta què s’ha mirat i per a què.

En problemes descriptius sense model predictiu, la pregunta és diferent: interessa explicar fidelment la població observada i limitar la generalització. No cal imposar una partició artificial a tota taula només perquè es treballe amb Python.

## 7. Decisions de neteja amb traçabilitat

Una bona neteja deixa una taula d’auditoria: regla, files afectades, justificació i efecte sobre els resultats. Conserva la font immutable i genera una versió derivada. Això permet comparar decisions sense reconstruir manualment l’estat anterior.

En el laboratori hi ha una absència, un text no numèric, una temperatura fora de rang i una repetició exacta. La solució distingix quatre flags i conserva el valor original. Només retira de l’anàlisi les observacions que no complixen el contracte definit.

No s’imputa una lectura impossible com si haguera sigut observada. Si posteriorment es vol imputar, s’haurà de registrar la variable derivada, el mètode i el seu efecte. Una «dada neta» no és una dada sense història.

## 8. Com tancar una exploració

Un informe d’EDA ha d’acabar amb conclusions operatives: què és utilitzable, què queda incert, quines transformacions es proposen i quin risc poden introduir. Inclou almenys una limitació de cobertura i una comprovació que encara falte.

Per exemple: «les lectures de dues sales tenen formats consistents, però la tercera conté errors de conversió; el resum exclou estes files i no representa tot el període». És més útil que «hem eliminat nuls i fet gràfics», perquè explica a què s’aplica el resultat.

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
```

## Pràctiques guiades

Cada pràctica deixa una evidència petita: una eixida comprovada i una explicació de la decisió. Els temps són orientatius i no inclouen instal·lació.

### Pràctica 1 · Inventari de problemes

**Nivell i temps:** Inicial · 20–30 min.

**Objectiu:** Detectar problemes abans de modificar valors.

**Materials:** exemple comentat d’esta unitat, les seues eixides i una còpia de treball per a les modificacions.

**Procediment:**

1. Executa l’auditoria i compara les dades originals amb `auditoria.csv`.
2. Localitza una absència original, un error de conversió, un valor fora de rang i una repetició excedent.
3. Comprova que les sales s’han normalitzat però la temperatura original es conserva.
4. Crea una taula amb problema, nombre de casos, regla aplicada i decisió pendent.

!!! success "Comprovació i evidència esperada"
    Hi ha 7 files; cadascuna de les quatre banderes compta un cas. Queden 3 lectures utilitzables.

**Preguntes de reflexió:**

- Una mateixa fila podria activar diverses banderes?
- Per què no convé sumar sempre els recomptes com si foren excloents?
- Què permet auditar conservar el valor original?

**Ampliació opcional:** Calcula el percentatge de files amb almenys una incidència mitjançant una combinació lògica de banderes.

### Pràctica 2 · Duplicat o observació repetida?

**Nivell i temps:** Intermèdia · 30–45 min.

**Objectiu:** Distingir una repetició exacta d’un conflicte d’identitat.

**Materials:** exemple comentat d’esta unitat, les seues eixides i una còpia de treball per a les modificacions.

**Procediment:**

1. Revisa les dues files amb id 2 i comprova que coincidixen.
2. En una còpia, canvia la temperatura d’una d’elles a 22.
3. Abans de descartar-la, crea un informe dels identificadors amb més d’un valor diferent.
4. Proposa una política per als conflictes: consulta de font, quarantena o selecció justificada amb marca temporal.

!!! success "Comprovació i evidència esperada"
    El nou cas es tracta com un conflicte a investigar; no s’elimina automàticament només perquè compartix id.

**Preguntes de reflexió:**

- Què representa la clau en este conjunt?
- Quan serien legítimes dues lectures de la mateixa sala?
- Quina informació faria possible triar la lectura correcta?

**Ampliació opcional:** Afig una marca temporal i compara una clau simple amb una clau composta sala–instant.

### Pràctica 3 · Mesurar l’efecte de netejar

**Nivell i temps:** Avançada · 45–60 min.

**Objectiu:** Relacionar decisions de qualitat amb canvis en els resums.

**Materials:** exemple comentat d’esta unitat, les seues eixides i una còpia de treball per a les modificacions.

**Procediment:**

1. Calcula la mitjana numèrica abans de filtrar i després d’aplicar la política del laboratori.
2. Compara-la amb la mediana i identifica l’efecte de 999.
3. Redacta un registre de decisions que justifique el rang docent de −20 a 60 i la gestió del duplicat conegut.
4. Desa per separat dades auditades i dades utilitzables, amb recompte d’entrada i eixida.

!!! success "Comprovació i evidència esperada"
    El resum final correspon a 20, 21 i 23; la mitjana és aproximadament 21,33. Cap correcció queda amagada.

**Preguntes de reflexió:**

- Una mediana robusta fa innecessària l’auditoria?
- Un valor extrem és sempre incorrecte?
- Per què el rang d’acceptació no es pot copiar sense revisar-lo a qualsevol sensor?

**Ampliació opcional:** Repeteix el resum per sala i explica per què alguns grups queden sense observacions vàlides.

## Exercicis autònoms

Intenta resoldre cada repte abans de desplegar l’orientació. Es valora el raonament i les comprovacions, no només obtindre una xifra.

### Repte 1 · Zero i absència

Dissenya quatre observacions de consum que incloguen zero, buit, text invàlid i un valor positiu. Audita-les.

??? example "Solució orientativa i criteri de revisió"
    Zero és una observació possible; buit i conversió fallida han de tindre marques distintes. La regla de rang depén de la unitat i del procés.

### Repte 2 · Contracte de dades

Escriu un contracte per a una taula de préstecs amb clau, tipus, valors admesos i dos controls entre columnes.

??? example "Solució orientativa i criteri de revisió"
    Exemple: id únic, dates vàlides, devolució posterior o igual al préstec quan existix, estat compatible amb devolució. Diferencia préstec encara obert d’un error.

### Repte 3 · Decisió reversible

Proposa com corregir una errada coneguda de sensor sense destruir el valor original.

??? example "Solució orientativa i criteri de revisió"
    Conserva original, valor corregit, regla, motiu i versió del procés. Una taula d’auditoria permet reconstruir la decisió; sobreescriure sense traça no.

## Errors habituals i diagnòstic

| Símptoma | Causa que convé investigar | Comprovació o correcció |
|---|---|---|
| Desapareixen massa files | Filtres encadenats sense recompte. | Registra cada regla i compara identificadors abans i després. |
| Tots els extrems corregits al límit | Retall automàtic sense evidència. | Marca i investiga abans de modificar. |
| Conflictes tractats com duplicats exactes | Clau incompleta o regla indiscriminada. | Compara contingut i significat de la clau. |

## Autoavaluació i evidències

Abans de donar la unitat per treballada, comprova estos punts i escriu una frase d’evidència per a cadascun:

- [ ] Puc definir què representa cada fila.
- [ ] Puc auditar absències, formats, duplicats i valors extrems.
- [ ] Puc documentar decisions de neteja i les seues conseqüències.
- [ ] He executat el laboratori i he contrastat almenys un resultat independentment.
- [ ] Puc explicar una limitació i un cas en què el procediment requeriria canvis.

**Lliurable de la píndola:** còpia de treball reproduïble, resultats de la pràctica seleccionada i un text breu que indique pregunta, decisió, comprovació i limitació. Si s’usa dins de BiciTierra Market, integra esta evidència en el lliurable setmanal corresponent; no cal crear una entrega duplicada.

## Fonts per aprofundir

- [Documentació oficial de referència](https://pandas.pydata.org/docs/user_guide/missing_data.html). Consulta especialment els conceptes i els supòsits descrits en la unitat.

Les versions executades i els límits de la comprovació estan en el [registre de validació](../VALIDACIO.md). Els exemples són originals i les dades són sintètiques.

## Aplicació final a BiciTierra Market

**Moment orientatiu:** setmana 1–2. Esta correspondència ajuda a triar materials i no substituïx el document de treball de l’alumnat.

Elabora el primer informe de qualitat de sales_history.csv i customers.csv per separat. Comprova períodes, cobertura de combinacions, rangs i absències. Separa la detecció de problemes de les decisions que dependran del model o de la segmentació.

**Transferència:** identifica quin concepte acabes de practicar, quina dada del projecte l’exigix i què has de canviar respecte del laboratori. Justifica eixa adaptació abans de copiar codi.
