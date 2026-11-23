# Helpdesk Intel·ligent · Document de treball

[Dades del projecte](MATERIALS_PRACTICS/dades/README.md){ .md-button }
[Píndoles ampliades](PINDOLES_AMPLIADES/docs/index.md){ .md-button }
[Glossari](glossari_terms.md){ .md-button }

Construïu per a **Valencia HelpDesk 360** un sistema que classifique tickets i permeta consultar procediments interns amb fonts. El resultat ha de mostrar també quan cal derivar a una persona.

Este és el recorregut únic de treball. Les píndoles s'obrin quan les necessiteu; els materials pràctics es descarreguen conservant les carpetes. Treballeu en equip, registreu les decisions i repartiu responsabilitats. Tot l'equip ha de poder explicar el flux complet.

## Repte i producte final

Llegiu el [briefing de l'empresa](MATERIALS_PRACTICS/empresa/01_briefing_empresa.md). El pilot ha d'incloure una taxonomia de categories i prioritats, dades revisades, comparació de dos classificadors bàsics, corpus documental, consulta amb fonts, API o interfície i proves amb casos nous. Diferencieu la consulta extractiva del RAG amb generació i declareu què heu implementat.

No introduïu dades personals reals ni credencials en el repositori o en les consultes. Els procediments són materials del cas docent: representeu-los amb fidelitat, sense presentar-los com una política universal.

## Mapa de les cinc setmanes

La duració prové de la proposta original del projecte. El professorat concreta dates i adapta el ritme després de BiciTierra; els checkpoints són punts de revisió, no pesos addicionals.

| Setmana | Tasca principal | Evidència i revisió |
|---|---|---|
| 1 | Categories, prioritats i arquitectura | CP1: proposta inicial |
| 2 | Revisar tickets i preparar corpus | CP2: dades i corpus traçables |
| 3 | Comparar regles i model supervisat | Taula de resultats i errors |
| 4 | Consulta documental i integració | CP3: flux complet amb fonts i derivació |
| 5 | Proves reservades, riscos i defensa | CP4: entrega final reproduïble |

## Píndoles ampliades: contingut nou

[Obri el recull ampliat](PINDOLES_AMPLIADES/docs/index.md). Reutilitzeu les bases ja treballades en P2; ací només s’amplien classificació textual, RAG, APIs i guardrails.

## Abans de començar

1. Creeu un repositori d'equip amb README, tasques i responsables.
2. Conserveu una còpia dels originals. Guardeu revisions i resultats en fitxers diferents.
3. Prepareu l'entorn de la [guia de notebooks](MATERIALS_PRACTICS/notebooks/README.md).
4. Anoteu les dates acordades, els criteris d'acceptació i el repartiment del treball.

Estructura orientativa de la vostra entrega:

```text
README.md
dades/             # originals, revisions i particions identificades
corpus/            # documents, metadades i fragments
notebooks/         # exploració i comparació
src/               # classificació, recuperació i aplicació
proves/            # entrades, resultats esperats i observats
memoria/           # decisions, mètriques, riscos i conclusions
```

## Setmana 1 · Entendre i dissenyar

**Objectiu:** convertir el problema de negoci en decisions comprovables.

1. Llegiu el briefing i una mostra de [tickets](MATERIALS_PRACTICS/dades/tickets_helpdesk.csv).
2. Proposeu categories de departament, tipologies i prioritats. Escriviu una definició i exemples; expliqueu els casos ambigus i la regla de derivació.
3. Diferencieu urgència declarada i prioritat operativa. Una etiqueta del CSV és una proposta que cal revisar.
4. Dibuixeu el flux: entrada → classificació → consulta → resposta amb fonts o derivació. La consulta també pot entrar com a pregunta independent.
5. Definiu els camps del ticket i del document, i tres preguntes que el sistema hauria de poder resoldre.
6. Feu que dos membres classifiquen els mateixos exemples i reviseu desacords.

**Consulta:** [Python i entorns](PINDOLES/python-i-entorns.md) · [RAG i embeddings](PINDOLES/rag-i-embeddings.md).

**CP1:** entregueu categories, esquema de dades, diagrama, tres preguntes i dos riscos. Reviseu amb el professorat si l'abast és viable abans d'implementar.

## Setmana 2 · Preparar tickets i documents

**Objectiu:** obtindre dades revisades i un corpus localitzable.

1. Executeu el [notebook d'exploració](MATERIALS_PRACTICS/notebooks/01_exploracio_tickets.ipynb).
2. Consulteu el [diccionari](MATERIALS_PRACTICS/dades/DICCIONARI_DADES.md) i el [context del dataset](MATERIALS_PRACTICS/dades/README.md). Reviseu nuls, etiquetes, estat, duplicats i quasi duplicats.
3. Conserveu els IDs originals i documenteu cada correcció. No elimineu tickets només perquè són difícils de classificar.
4. Prepareu [contrasenyes](MATERIALS_PRACTICS/empresa/02_politica_contrasenyes.md), [VPN](MATERIALS_PRACTICS/empresa/03_manual_vpn.md) i [correu](MATERIALS_PRACTICS/empresa/04_procediment_correu.md). Anoteu document, versió, fragment i text; conserveu els passos dels procediments.
5. Separeu preguntes de desenvolupament i prova. Reserveu les de prova per a la setmana 5.

**Consulta:** [Jupyter](PINDOLES/jupyter-notebooks.md) · [Python per a dades](PINDOLES/python-per-a-dades-i.md) · [EDA i qualitat](PINDOLES/eda-i-qualitat-de-dades.md).

**Ampliació nova:** [corpus, fragments i recuperació](PINDOLES_AMPLIADES/docs/rag-i-embeddings/index.md).

**CP2:** entregueu informe curt de qualitat, dades revisades, registre de canvis i inventari del corpus. Comproveu que cada fragment es pot rastrejar fins al document original.

## Setmana 3 · Comparar classificadors

**Objectiu:** justificar una primera classificació amb dades que no han servit per ajustar-la.

1. Executeu la [baseline per regles](MATERIALS_PRACTICS/notebooks/02_classificacio_baseline.ipynb) per entendre la lògica inicial. El recompte sobre tots els tickets no és una prova independent.
2. Seguiu la [pràctica de comparació](MATERIALS_PRACTICS/notebooks/03_comparacio_models.md): regles contra TF-IDF i regressió logística.
3. Manteniu duplicats i quasi duplicats en la mateixa partició. Useu exactament els mateixos casos de prova per als dos enfocaments.
4. Compareu accuracy, F1 macro, suport per classe, matriu de confusió i casos sense regla. Analitzeu almenys tres errors o ambigüitats.
5. Justifiqueu quin enfocament usaríeu i què falta per a un pilot real. El conjunt és menut: expliciteu els límits de les mètriques.

**Consulta:** [Scikit-learn](PINDOLES/scikit-learn-intro.md) · [Validació](PINDOLES/validacio-de-models.md).

**Ampliació nova:** [classificació de text i TF-IDF](PINDOLES_AMPLIADES/docs/classificacio-text/index.md).

**Evidència:** notebook reproduïble, IDs de les particions, comparativa i lectura d'errors. Revisió abans d'integrar el model.

## Setmana 4 · Consultar amb fonts i integrar

**Objectiu:** mostrar un flux complet, inclosa la falta de context.

1. Seguiu la [pràctica de consulta i integració](MATERIALS_PRACTICS/notebooks/04_consulta_i_integracio.md).
2. Inspeccioneu els fragments recuperats abans d'afegir generació. No confongueu una coincidència de vocabulari amb una resposta fonamentada.
3. Feu que la resposta mostre font i fragment. Si falta informació, expliqueu-ho i deriveu.
4. Connecteu classificació i consulta amb API o interfície; documenteu entrades, eixides i errors.
5. Proveu una consulta resolta, una sense context i una entrada invàlida. Identifiqueu si el sistema fa extracció o generació amb context.

**Consulta:** [RAG](PINDOLES/rag-i-embeddings.md) · [APIs REST](PINDOLES/apis-rest.md) · [Guardrails](PINDOLES/prompt-engineering-i-guardrails.md).

**Ampliacions noves:** [RAG i embeddings](PINDOLES_AMPLIADES/docs/rag-i-embeddings/index.md) · [API executable](PINDOLES_AMPLIADES/docs/apis-rest/index.md) · [Prompts i guardrails](PINDOLES_AMPLIADES/docs/prompt-engineering-i-guardrails/index.md).

**CP3:** demo reproduïble amb classificació, resposta traçable, derivació i gestió d'errors. Guardeu pregunta, fragments recuperats, resposta i decisió de derivar, sense secrets.

## Setmana 5 · Provar i defensar

**Objectiu:** valorar el resultat amb casos reservats i explicar-ne els límits.

1. Executeu els casos reservats sense ajustar després el sistema sobre ells. Si feu canvis, declareu-los i reserveu una nova prova independent.
2. Incloeu consulta documental, pregunta fora del corpus, dada actual que el corpus no pot donar, entrada buida i intent de canviar les instruccions.
3. Registreu entrada, resultat esperat, resultat observat, fonts, encert o error i correcció proposada. No afirmeu que un prompt garantix seguretat.
4. Reviseu que una altra persona pot seguir el README en un entorn net.
5. Prepareu la memòria, l'autoavaluació i la defensa. Expliqueu decisions i errors amb evidències.

**Ampliació nova:** [bateria de casos i límits dels controls](PINDOLES_AMPLIADES/docs/prompt-engineering-i-guardrails/index.md).

**CP4:** repositori complet, memòria, proves i defensa. La demo ha de mostrar una classificació correcta, una consulta amb font i una derivació per falta de context. Indiqueu també un error conegut i una millora viable.

## Plantilla de checkpoint

Copieu-la en cada revisió:

- Equip, membres, data i checkpoint:
- Objectiu acordat i responsables:
- Evidències i enllaços al repositori:
- Resultat observat i criteri d'acceptació:
- Errors, bloquejos i decisions:
- Retorn del professorat:
- Accions següents, responsable i termini:

## Memòria i defensa

La memòria ha d'explicar context i objectius, taxonomia i arquitectura, qualitat de dades, particions, comparació de classificadors, corpus i recuperació, generació si n'hi ha, integració, proves, privacitat, límits i millores. Enllaceu les evidències; no substituïu resultats per captures sense interpretació.

En la defensa repartiu la paraula i mostreu el sistema. Cada membre ha de poder explicar una decisió, una prova i un límit. Prepareu una alternativa local si falla un servei extern i declareu quan l'esteu utilitzant.

## Autoavaluació d'equip

- Quina aportació verificable ha fet cada membre?
- Quina decisió hem canviat després d'una prova?
- Què funciona i amb quina evidència?
- Què falla, quan derivem i què milloraríem primer?

## Avaluació

Es mantenen els cinc criteris del projecte original, amb pes orientatiu del 20% cadascun i escala d'1 a 5. El professorat concreta l'aplicació abans del lliurament.

## Escala comuna

- `1`: molt insuficient
- `2`: insuficient
- `3`: acceptable
- `4`: notable
- `5`: excel.lent

## Evidències mínimes esperades

- taxonomia de categories i prioritats
- base documental preparada i justificable
- baseline de classificació amb proves mínimes
- flux `RAG` o consulta documental demostrable
- demo funcional amb casos correctes i casos límit
- document de límits, riscos i decisions preses

## Criteris d'avaluació

### 1. Comprensió del problema i model funcional

Pes orientatiu: `20%`

| Nivell | Descripció |
|---|---|
| 1 | No queda clar quin problema resolen ni com han traduït els tickets a categories útils. |
| 2 | Hi ha una idea general del problema, però les categories o prioritats són confuses, solapades o poc aplicables. |
| 3 | El problema està ben entés i les categories bàsiques es poden usar, encara que hi ha alguns dubtes o ambigüitats. |
| 4 | El model funcional és clar, coherent i aplicable a casos nous amb criteri raonable. |
| 5 | El model funcional és molt clar, justificat i operatiu; l'equip explica bé decisions, excepcions i límits de la taxonomia. |

### 2. Base documental i criteri de `RAG`

Pes orientatiu: `20%`

| Nivell | Descripció |
|---|---|
| 1 | No hi ha corpus usable o la documentació està desordenada i sense criteri. |
| 2 | Hi ha documents, però sense neteja, estructura o justificació suficient. |
| 3 | El corpus és usable i l'equip diferencia mínimament consulta documental i altres tipus de pregunta. |
| 4 | La base documental està ben preparada i l'equip sap quan el sistema ha de respondre i quan no. |
| 5 | La base documental està molt ben seleccionada i justificada; l'equip domina el límit entre resposta documental, falta de context i consulta que exigix altres capes. |

### 3. Classificació de tickets i proves

Pes orientatiu: `20%`

| Nivell | Descripció |
|---|---|
| 1 | No hi ha classificació funcional o no es pot provar. |
| 2 | La classificació funciona només parcialment i sense lectura clara dels errors. |
| 3 | Hi ha una baseline funcional i alguna evidència bàsica de prova. |
| 4 | La classificació és usable, està provada amb criteri i l'equip sap explicar errors i confusions habituals. |
| 5 | La classificació està ben validada per al nivell del projecte; l'equip compara casos, interpreta errors i justifica què és fiable i què no. |

### 4. Integració i demo funcional

Pes orientatiu: `20%`

| Nivell | Descripció |
|---|---|
| 1 | No hi ha integració real o la demo no permet veure el sistema. |
| 2 | Hi ha peces soltes, però la integració és fràgil o poc demostrable. |
| 3 | La demo mostra l'essencial del flux, encara que amb poca robustesa o poca claredat. |
| 4 | La integració és clara i la demo permet seguir bé classificació, consulta i resultat. |
| 5 | La integració és molt clara per al nivell del projecte i la demo mostra també límits, errors o casos on el sistema s'atura amb bon criteri. |

### 5. Criteri tècnic, riscos i defensa de decisions

Pes orientatiu: `20%`

| Nivell | Descripció |
|---|---|
| 1 | No identifiquen riscos ni justifiquen decisions. |
| 2 | Enumeren riscos o límits, però de manera superficial. |
| 3 | Identifiquen riscos bàsics i defensen algunes decisions amb coherència mínima. |
| 4 | Expliquen bé decisions tècniques, privacitat, límits i millores plausibles. |
| 5 | La defensa és madura: connecten riscos, qualitat, privacitat i decisions de disseny amb criteri tècnic clar. |

## Full ràpid de valoració

| Criteri | Pes | Nivell 1-5 | Observacions |
|---|---:|---:|---|
| Comprensió del problema i model funcional | 20 |  |  |
| Base documental i criteri de `RAG` | 20 |  |  |
| Classificació de tickets i proves | 20 |  |  |
| Integració i demo funcional | 20 |  |  |
| Criteri tècnic, riscos i defensa | 20 |  |  |

## Preguntes de comprovació docent

- Les categories es podrien aplicar també en casos nous?
- L'equip sap diferenciar classificació, cerca documental i generació?
- La demo mostra només encerts o també límits?
- El document final diu què és fiable i què encara no ho és?


## Checklist final

- [ ] Les categories i prioritats tenen criteris i exemples.
- [ ] Les dades originals es conserven i les revisions són traçables.
- [ ] La comparació usa la mateixa prova i evita fuites per duplicats.
- [ ] Les respostes tenen fonts pertinents i es deriva quan falta context.
- [ ] Hem declarat si hi ha generació o consulta extractiva.
- [ ] L'API o interfície gestiona entrades invàlides i errors.
- [ ] El README permet reproduir el treball i identifica les dependències.
- [ ] Les proves inclouen casos nous i límits coneguts.
- [ ] No hem inclòs secrets ni dades personals innecessàries.
- [ ] Hem completat memòria, autoavaluació i defensa.
