---
title: Visualitzacio Amb Matplotlib I Seaborn
---

# Visualitzacio Amb Matplotlib I Seaborn

## Per a què servix esta capa

Abans d'explicar un model, sovint necessitem veure el comportament de les dades.

`Matplotlib` i `Seaborn` no són només per a fer gràfics bonics. Servixen per detectar patrons, anomalies i relacions que després condicionen la resta del treball.

També tenen un valor més profund: obliguen a mirar les dades abans d'opinar sobre elles. Moltes conclusions precipitades cauen quan una distribució, un outlier o una separació de grups es fan visibles.

## Com repartir els papers

- `Matplotlib`: base general per dibuixar
- `Seaborn`: gràfics estadístics més ràpids i llegibles

La idea no és enfrontar-les. De fet, moltes vegades conviuen:

- `Seaborn` per traure una primera lectura clara
- `Matplotlib` per ajustar títols, eixos, grandària o composició final

## Visualitzar és llegir, no decorar

En context docent és important repetir-ho perquè hi ha un error molt habitual: interpretar el gràfic com una il·lustració final del treball.

En realitat, la visualització entra molt abans:

- per detectar errors de qualitat
- per veure patrons inesperats
- per decidir si cal transformar variables
- per justificar una decisió analítica davant del professorat o d'una direcció fictícia

## Per què un gràfic pot ser millor que una taula

Una taula pot contindre la informació, però no sempre mostra bé:

- dispersió
- patrons
- outliers
- comparacions ràpides entre grups

Per això la visualització no és adorn. És un instrument de diagnòstic.

També és una eina de comunicació, però convé que la comunicació arribe després del diagnòstic i no al revés.

## Exemple mínim

```python
import matplotlib.pyplot as plt
import seaborn as sns

sns.boxplot(data=df, x="canal", y="vendes")
plt.xticks(rotation=45)
plt.show()
```

## Gràfics que més rendiment donen al curs

- histograma
- boxplot
- countplot
- scatterplot
- heatmap de correlació

No perquè siguen els únics possibles, sinó perquè donen molta informació amb una corba d'aprenentatge raonable.

## Abans de dibuixar: quina pregunta vols respondre?

Este pas sembla obvi, però és el que més falta fa en aula.

Preguntes tipus:

- com es distribuïx esta variable?
- hi ha grups molt diferents?
- hi ha valors extrems?
- dos variables pareixen relacionades?
- hi ha massa categories perquè el gràfic siga llegible?

Si l'alumnat no pot formular la pregunta, el gràfic sol acabar sent soroll visual.

## Quina pregunta respon cada un

- histograma: com es distribuix una variable?
- boxplot: hi ha outliers o diferències entre grups?
- scatterplot: dos variables es mouen juntes?
- heatmap: quines variables semblen relacionades?

Ací hi ha una lliçó important: un bon gràfic no és el més vistós, sinó el que respon una pregunta concreta.

## Lectura responsable d'un gràfic

També convé ensenyar què NO es pot concloure massa ràpid.

Per exemple:

- un `scatterplot` suggerix relació, però no prova causalitat
- una correlació alta no significa que una variable explique per si sola l'altra
- un boxplot amb diferències visibles no evita la necessitat de context o qualitat de dades

## Exemple teòric curt: mateix dataset, preguntes diferents

Amb un mateix conjunt de vendes podem voler saber:

- com es distribuïx `vendes`
- si hi ha outliers per `canal`
- si `descompte` i `marge` semblen relacionats

Cap d'estes preguntes no demana exactament el mateix gràfic.

Per això no convé triar visuals "per costum", sinó segons la lectura que volem fer.

## Quan `Seaborn` ajuda molt i quan cal baixar a `Matplotlib`

`Seaborn` ajuda molt quan volem:

- eixir ràpidament amb una visual estadística clara
- treballar amb `DataFrame`
- comparar grups sense massa configuració inicial

`Matplotlib` sol ser més útil quan necessitem:

- ajustar detall fi
- combinar diversos gràfics
- controlar millor eixos, anotacions o format final

Esta distinció és útil perquè evita que l'alumnat veja les dues llibreries com a competidores estrictes.

## Exemple guiat de classe

Situació:

en `Predicció Comercial`, un equip vol saber si el descompte està relacionat amb un marge pitjor.

Un `scatterplot` o un `boxplot` per trams de descompte pot donar una lectura inicial molt millor que una intuïció verbal.

També pot permetre una conversa més madura:

- el marge cau sempre o només en certs trams?
- hi ha canals on el patró és diferent?
- tenim outliers que poden distorsionar la lectura?

En una bona sessió de classe, el gràfic no es tanca amb `ací està la figura`, sinó amb una frase de lectura:

`pareix que a partir d'un cert tram de descompte el marge es torna molt més inestable, especialment en certs canals.`

## Error habitual

Omplir el notebook de gràfics sense dir què està mirant cadascun ni quina decisió pot afectar.

També és habitual:

- no etiquetar bé els eixos
- posar massa categories juntes i perdre llegibilitat
- interpretar una correlació visual com si ja fora causalitat

També és habitual:

- elegir un tipus de gràfic inadequat per la pregunta
- usar colors o formats que dificulten la lectura
- mostrar el mateix patró diverses vegades sense afegir informació nova

## Pràctica guiada suggerida

Agafeu una variable numèrica i una categòrica del vostre projecte.

1. feu un histograma de la variable numèrica
2. feu un boxplot per categoria
3. escriviu què aporta el segon gràfic que no veieu tan bé al primer

Després, afegiu una segona variable numèrica i feu un `scatterplot`.

L'objectiu no és acumular gràfics, sinó aprendre a justificar per què cada visual aporta una lectura distinta.

## Pràctica guiada llarga

### Objectiu

Aprendre a usar `Matplotlib` i `Seaborn` com a eines de lectura i justificació analítica, no només de presentació final.

### Situació

Suposeu un notebook de `Predicció Comercial` amb variables de vendes, canal, descompte, marge i devolucions.

### Pas 1. Començar per una variable numèrica

Trieu una variable com `vendes` o `marge` i feu un histograma.

La pregunta docent és:

- la distribució pareix simètrica?
- hi ha cua llarga?
- hi ha concentració en trams concrets?

### Pas 2. Passar a comparació entre grups

Ara feu un `boxplot` per `canal` o per segment.

Expliqueu:

- si hi ha grups diferents
- si hi ha outliers
- si la dispersió és semblant o molt desigual

### Pas 3. Provar una relació entre variables

Feu un `scatterplot` entre dues variables com `descompte` i `marge`.

No tanqueu la lectura amb una afirmació massa forta. Useu una formulació prudent:

- `pareix que...`
- `es veu una possible relació...`
- `caldria revisar si...`

### Pas 4. Pensar en quins visuals no val la pena insistir

Ací hi ha una part molt madura:

- quins gràfics no aporten quasi res nou?
- quins només repeteixen una lectura ja feta?
- quins serien massa sorollosos per a un dashboard?

### Pas 5. Tancar amb una decisió analítica

L'equip hauria d'acabar amb 2 o 3 frases com:

- `cal revisar outliers en este canal`
- `pareix que el descompte excessiu empitjora el marge en certs casos`
- `esta variable necessita transformació o segmentació`

### Criteri docent

La pràctica està ben resolta si cada gràfic acaba en una lectura útil i si l'alumnat sap explicar per què l'ha triat i què en conclou amb prudència.

## Mini pràctica

Pregunta:

si vols veure ràpidament si una variable té valors extrems, quin gràfic triaries primer?

## Solució orientativa

Un `boxplot`, perquè ajuda a detectar dispersió i possibles outliers de manera molt directa.

## Resum final

Visualitzar no és decorar. És una manera de pensar millor abans de transformar o modelar.

Si l'alumnat aprén a mirar bé una distribució, un outlier o una relació sospitosa, després entendrà molt millor per què modela d'una manera o d'una altra.

## Com usar-la en estos projectes

- BiciTierra Market: EDA i justificació de decisions de neteja
- P3: sèries simples i evolució de lectures
- P5: anàlisi exploratòria abans d'una lectura executiva o predictiva

## Vegeu també

- `Python per a Dades I`
- `EDA i Qualitat de Dades`
- `Dashboards i PowerBI`


## Per aprofundir

[Obri la píndola ampliada, amb pràctiques i exercicis](../PINDOLES_AMPLIADES/docs/visualitzacio-amb-matplotlib-i-seaborn/index.md).
