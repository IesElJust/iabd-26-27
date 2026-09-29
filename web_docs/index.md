# BiciTierra Market · Document de treball

[Descàrregues](DESCARREGUES.md){ .md-button }
[Píndoles ampliades](PINDOLES_AMPLIADES/docs/index.md){ .md-button }
[Glossari](glossari_terms.md){ .md-button }


**Projecte inicial del curs · Proposta de sis setmanes.** Este és el document que heu de seguir. Les píndoles i els fitxers pràctics estan a banda i s’enllacen en la setmana en què els necessiteu. El professorat concretarà les dates segons el calendari i el nivell del grup.

**Equip:** … · **Membres:** … · **Repositori:** …

| Setmana | Dates acordades | Data de revisió o entrega |
|---|---|---|
| 1 | … | … |
| 2 | … | … |
| 3 | … | … |
| 4 | … | … |
| 5 | … | … |
| 6 | … | … |

## Com utilitzar este document

1. Localitzeu la setmana actual en el [mapa del projecte](#mapa-setmanal).
2. Llegiu l’objectiu i seguiu les tasques en ordre. Consulteu cada píndola quan la tasca ho requerisca.
3. Treballeu amb els materials indicats i guardeu els resultats al repositori de l’equip.
4. Completeu l’entrega setmanal i el [registre de seguiment](#registre). Anoteu la revisió docent i el pròxim pas.

Els notebooks són una base que heu d’executar, entendre i adaptar. **No executeu tot el notebook de modelatge en la setmana 2:** la prova final es reserva per a la setmana 5, després de triar el model. Les dates dels CSV pertanyen al cas simulat; no són les dates del calendari de classe.

## El repte de l’empresa

BiciTierra Market combina botiga física i comerç electrònic. Vol millorar les decisions sobre vendes, estoc i campanyes. La direcció planteja tres preguntes:

- Podem anticipar les vendes mensuals amb prou fiabilitat per planificar l’estoc?
- Quins perfils de client tenim i quines accions comercials tenen sentit per a cadascun?
- Quines decisions podem justificar amb els resultats i quins límits tenen?

**Producte final:** anàlisi de dades, predicció mensual justificada, segmentació interpretable, dashboard executiu, memòria breu i defensa de **8–10 minuts**.

L’objectiu predictiu de partida és `sales_units`: unitats venudes durant un mes per canal, línia de producte i regió. Una altra variable objectiu s’ha d’acordar amb el professorat i ha de mantindre una separació temporal correcta.

Heu de comparar almenys una referència senzilla amb un model alternatiu, justificar una mètrica principal, aplicar una tècnica de segmentació i transformar els resultats en recomanacions. Un gràfic o una mètrica sense interpretació no tanca una tasca.

## Les dades i les regles del cas

| Material | Què conté | Quan s’utilitza |
|---|---|---|
| [Històric de vendes](MATERIALS_PRACTICS/dades/sales_history.csv){ download="sales_history.csv" } | 1.188 files, 18 sèries mensuals completes, gener de 2021–juny de 2026 | Setmanes 1–3 i 5–6 |
| [Clients](MATERIALS_PRACTICS/dades/customers.csv){ download="customers.csv" } | 2.000 clients, fotografia a 30/06/2026 | Exploració en setmana 1; segmentació en setmana 4 |
| [Entrada de predicció](MATERIALS_PRACTICS/dades/sales_forecast_input.csv){ download="sales_forecast_input.csv" } | 18 combinacions de juliol de 2026 sense resultat real | Setmana 5, després de validar |
| [Diccionari](MATERIALS_PRACTICS/dades/DICCIONARI_DADES.md) | Camps, unitats, significat i disponibilitat | Abans de triar variables i quan hi haja dubtes |
| [Referència tècnica de les dades](MATERIALS_PRACTICS/dades/README.md) | Generació sintètica, cobertura, nuls i ús dels fitxers | Consulta durant el projecte |

Totes les dades són **sintètiques per a docència**. Els clients són una mostra independent de les vendes agregades: no hi ha una clau transaccional que permeta unir les dues taules fila a fila. No s’espera que la despesa dels clients sume els ingressos de vendes.

**Informació disponible abans del mes:** canal, producte, regió, calendari, pressupost de màrqueting, descompte previst, estoc inicial i preu de tarifa. També es poden usar retards de mesos anteriors de la mateixa sèrie.

**Informació coneguda després del mes:** vendes, ingressos, visites web, despesa real de màrqueting, descompte real, estoc final i ruptura d’estoc. No useu estos valors del mateix mes per anticipar-ne les vendes.

| Partició | Període | Funció |
|---|---|---|
| Històric inicial | 2021 | Construir el retard de 12 mesos quan s’utilitze |
| Entrenament | Fins a desembre de 2024; efectivament 2022–2024 amb `lag_12` | Ajustar models i transformacions |
| Validació | Gener–desembre de 2025 | Comparar models i triar paràmetres |
| Prova final | Gener–juny de 2026 | Avaluar després de fixar les decisions; setmana 5 |
| Predicció nova | Juliol de 2026 | Aplicar el model sense disposar encara del resultat |

Separeu mesos complets, sense barrejar files aleatòriament. Ajusteu la imputació i l’escala només amb entrenament. La prova representa prediccions successives d’un mes vista: per predir juny, maig ja s’ha observat. No és una predicció simultània de sis mesos feta al desembre.

<a id="mapa-setmanal"></a>
## Mapa del projecte per setmanes

| Setmana | Focus | Material pràctic principal | Evidència de tancament |
|---|---|---|---|
| [1](#setmana-1) | Entorn, pregunta de negoci i EDA | Notebook 01 + històric + clients | Pregunta, dues hipòtesis i diagnòstic inicial · **CP1** |
| [2](#setmana-2) | Neteja, partició temporal i referències | Notebook 02, apartats 1–2 | Dades preparades, predictors justificats i baseline · **CP2** |
| [3](#setmana-3) | Entrenament i comparació | Notebook 02, apartats 3–4 | Taula de validació i elecció provisional de model |
| [4](#setmana-4) | Segmentació i perfils | Notebook 03 + clients | Perfils, accions comercials i model comparat · **CP3** |
| [5](#setmana-5) | Prova final, errors i explicació | Notebook 02, apartats 5–6 | Resultat de prova reservada, límits i previsió de juliol |
| [6](#setmana-6) | Dashboard, memòria i defensa | Materials de dashboard + resultats propis | Paquet final i defensa · **CP4** |

Cada setmana té quatre moments: **preparar → desenvolupar → comprovar → entregar**. Distribuïu-los entre les sessions reals amb el professorat. Les ampliacions són opcionals i es fan després del mínim de la setmana.

<a id="setmana-1"></a>
## Setmana 1 · Entendre el repte i explorar

**Objectiu:** formular una pregunta de negoci concreta i comprovar què permeten respondre les dades.

### Píndoles, en ordre d’ús

1. [Python i entorns](PINDOLES/python-i-entorns.md): preparació de l’entorn; reforç segons el nivell inicial.
2. [Jupyter Notebooks](PINDOLES/jupyter-notebooks.md): obrir, executar cel·les i escriure conclusions.
3. [Python per a dades](PINDOLES/python-per-a-dades-i.md): carregar CSV, seleccionar camps i resumir dades.
4. [EDA i qualitat](PINDOLES/eda-i-qualitat-de-dades.md): decidir què revisar abans de modelar.

### Materials que heu d’obrir

- [Notebook 01 · EDA](MATERIALS_PRACTICS/notebooks/01_eda.ipynb){ download="01_eda.ipynb" }.
- [Històric](MATERIALS_PRACTICS/dades/sales_history.csv){ download="sales_history.csv" }, [clients](MATERIALS_PRACTICS/dades/customers.csv){ download="customers.csv" } i [diccionari](MATERIALS_PRACTICS/dades/DICCIONARI_DADES.md).

### Tasques

1. Acordeu l’equip i creeu el repositori amb l’[estructura mínima](#repositori).
2. Escriviu una pregunta principal i una de secundària. Concreteu quina decisió prendria la direcció amb la resposta.
3. Prepareu Python, Jupyter, pandas i NumPy. Des de la carpeta `MATERIALS_PRACTICS/notebooks/`, executeu la lectura inicial dels CSV.
4. Comproveu què representa cada fila, les claus, les dates, els tipus i els nuls. Diferencieu falta de dada i valor zero.
5. Useu els patrons d’entrenament per explorar diferències entre canals, productes, regions i mesos. No useu la prova de 2026 per orientar decisions de model.
6. Escriviu dues hipòtesis i exemples concrets que les motiven. Anoteu també què encara no podeu concloure.

### Entrega i comprovació · CP1

Completeu esta fitxa en el repositori:

| Apartat | Resposta de l’equip |
|---|---|
| Pregunta principal i decisió de negoci | … |
| Pregunta secundària | … |
| Variable objectiu i unitat d’observació | … |
| Predictors inicials i moment en què es coneixen | … |
| Problemes de qualitat detectats i exemples | … |
| Baseline, model alternatiu i mètrica que proposem | … |
| Variables i tècnica inicial de segmentació | … |
| Hipòtesi 1 i hipòtesi 2 | … |

Adjunteu el notebook executat amb comentaris. Podeu avançar quan qualsevol membre explique la pregunta, la clau d’una fila i almenys un problema de qualitat.

<a id="setmana-2"></a>
## Setmana 2 · Preparar les dades i establir una referència

**Objectiu:** tindre una preparació reproduïble i una primera predicció amb què comparar els models.

### Píndoles

- [Python per a dades](PINDOLES/python-per-a-dades-i.md): tractament de nuls, transformacions i agrupacions.
- [Visualització](PINDOLES/visualitzacio-amb-matplotlib-i-seaborn.md): representar distribucions i justificar decisions.
- [Validació de models](PINDOLES/validacio-de-models.md): mètriques i separació de dades. En este projecte preval el tall temporal indicat ací sobre exemples genèrics de partició aleatòria.

### Materials

- [Notebook 01](MATERIALS_PRACTICS/notebooks/01_eda.ipynb){ download="01_eda.ipynb" }, per documentar qualitat i decisions.
- [Notebook 02 · Modelatge](MATERIALS_PRACTICS/notebooks/02_modelatge_baseline.ipynb){ download="02_modelatge_baseline.ipynb" }: càrrega i **apartats 1–2**, inclosa la comprovació de referències de setmana 2.
- [Diccionari](MATERIALS_PRACTICS/dades/DICCIONARI_DADES.md).

### Tasques

1. Per cada problema detectat, decidiu conservar, corregir, imputar o excloure i escriviu el motiu. Manteniu els CSV originals intactes.
2. Ordeneu per sèrie i mes; comproveu la cobertura abans de crear retards d’un i dotze mesos.
3. Separeu entrenament, validació i prova. Guardeu dates i recompte de files de cada partició.
4. Elaboreu una taula de variables admeses i excloses segons si es coneixen abans del mes. Justifiqueu especialment l’exclusió d’ingressos i sessions del mateix mes.
5. Calculeu la mitjana històrica de grup només amb entrenament i compareu-la amb la referència del mateix mes de l’any anterior.
6. Mesureu l’error en validació: **MAE en unitats** i **WAPE en percentatge**. Expliqueu què implica l’error per al negoci.

### Entrega i comprovació · CP2

- Notebook amb preparació reproduïble i decisions de qualitat.
- Taula de particions, llista de predictors i resultats de les referències.
- Un exemple de com una mala imputació o una variable posterior podria falsejar el resultat.

Atureu-vos abans de l’apartat 3 del notebook 02. El conjunt de prova queda reservat.

<a id="setmana-3"></a>
## Setmana 3 · Comparar models

**Objectiu:** seleccionar una alternativa amb evidències de validació, sense mirar el resultat de la prova final.

### Píndoles

- [Introducció a scikit-learn](PINDOLES/scikit-learn-intro.md): conceptes d’ajust, predicció i pipeline. El notebook base calcula ridge amb NumPy; traslladar-lo a scikit-learn és una ampliació.
- [Validació de models](PINDOLES/validacio-de-models.md): comparació justa, sobreajust i lectura de mètriques.
- **Ampliació:** [MLflow](PINDOLES/mlflow-intro.md), per registrar experiments si la comparació bàsica ja funciona.

### Materials

- [Notebook 02](MATERIALS_PRACTICS/notebooks/02_modelatge_baseline.ipynb){ download="02_modelatge_baseline.ipynb" }, **apartats 3–4**. Executeu abans les cel·les de preparació de setmana 2 si reinicieu l’entorn.
- Resultats de les referències de setmana 2.

### Tasques

1. Expliqueu què aporta un model lineal regularitzat respecte de les referències simples.
2. Entreneu amb els predictors disponibles abans del mes i amb transformacions ajustades només en entrenament.
3. Compareu, com a mínim, una referència i un model alternatiu amb les mateixes files de validació i mètriques.
4. Registreu model, variables, paràmetres, MAE, WAPE i observacions. Mostreu casos en què la predicció s’allunye del resultat.
5. Trieu provisionalment el model amb dades de 2025 i justifiqueu si la millora compensa la complexitat.

### Entrega i comprovació

Taula comparativa, elecció argumentada i dos casos d’error en validació. Tots els membres han de distingir entrenament, validació i prova.

**Atureu-vos abans de l’apartat 5.** La selecció es revisa en CP3 juntament amb la segmentació; la prova final arribarà en setmana 5.

<a id="setmana-4"></a>
## Setmana 4 · Segmentar clients i proposar accions

**Objectiu:** descriure perfils de client que ajuden a decidir campanyes, serveis o prioritats comercials.

### Píndoles

- [Clustering i segmentació](PINDOLES/clustering-i-segmentacio.md): triar variables, escalar i interpretar grups.
- [Visualització](PINDOLES/visualitzacio-amb-matplotlib-i-seaborn.md): comparar perfils sense quedar-se en etiquetes numèriques.
- [Scikit-learn](PINDOLES/scikit-learn-intro.md): suport si s’implementa K-Means o un altre algorisme.

### Materials

- [Notebook 03 · Segmentació](MATERIALS_PRACTICS/notebooks/03_segmentacio.ipynb){ download="03_segmentacio.ipynb" }.
- [Clients](MATERIALS_PRACTICS/dades/customers.csv){ download="customers.csv" } i la seua definició en el [diccionari](MATERIALS_PRACTICS/dades/DICCIONARI_DADES.md).

### Tasques

1. Reviseu nuls, valors extrems, recència, freqüència, despesa i devolucions. Excloeu identificador i data de fotografia com a variables de clustering.
2. Justifiqueu les variables triades. La despesa anual és tiquet mitjà × comandes: usar les tres pot donar massa pes al mateix comportament.
3. Executeu les regles del notebook com a primera referència. El notebook inclou una segmentació heurística; no conté un clustering complet resolt.
4. Desenvolupeu i justifiqueu la tècnica acordada amb el professorat. Per practicar clustering, useu la píndola de K-Means, ajusteu l’escala i argumenteu el nombre de grups. Una tècnica més complexa no és millor només pel nom.
5. Descriviu almenys dos perfils útils: mida, comportament, diferències i casos fronterers.
6. Proposeu una acció per perfil i expliqueu què hauria de comprovar l’empresa abans d’aplicar-la.

### Entrega i comprovació · CP3

- Notebook amb preparació, tècnica i perfils interpretats.
- Taula de segments i accions comercials.
- Comparativa de models de setmana 3 i decisió final abans d’obrir el test.

No hi ha una etiqueta de segment «correcta». Cal justificar utilitat i límits. No uniu esta fotografia de clients amb vendes històriques com si foren les mateixes transaccions.

<a id="setmana-5"></a>
## Setmana 5 · Fer la prova final i explicar el resultat

**Objectiu:** comprovar el model en dades reservades i comunicar els seus errors i límits.

### Píndoles

- [Validació de models](PINDOLES/validacio-de-models.md): lectura crítica de la prova i diferència amb validació.
- [Explicabilitat amb SHAP i LIME](PINDOLES/xai-shap-lime.md): lectura conceptual de factors i explicacions. Aplicar les llibreries és una ampliació; el mínim és explicar decisions i casos concrets amb evidències.

### Materials

- [Notebook 02](MATERIALS_PRACTICS/notebooks/02_modelatge_baseline.ipynb){ download="02_modelatge_baseline.ipynb" }, **apartats 5–6**, després de recuperar l’ajust i la selecció ja fixats.
- [Entrada de juliol](MATERIALS_PRACTICS/dades/sales_forecast_input.csv){ download="sales_forecast_input.csv" }.
- Comparativa i decisions congelades en CP3.

### Tasques

1. Deixeu per escrit el model, els predictors i els paràmetres abans d’executar la prova.
2. Avalueu gener–juny de 2026 una vegada. No canvieu el model per millorar esta mètrica i continuar presentant-la com a prova independent.
3. Compareu el resultat amb validació i analitzeu almenys dos casos d’error. Considereu estoc insuficient, diferències de grup i informació no observada.
4. Expliqueu factors que influeixen en el model i límits de la interpretació. En dades sintètiques, una relació apresa no demostra una causa en el mercat real.
5. Apliqueu el model a juliol i guardeu les 18 prediccions amb la clau completa. Diferencieu predicció i venda real.
6. Redacteu una recomanació d’estoc i una de campanya, amb el grau de confiança que permeten les evidències.

### Entrega i comprovació

Mètriques finals, anàlisi d’errors, fitxer de prediccions i límits documentats. La venda real de juliol no està inclosa: no hi ha una mètrica validada per a eixe mes.

Esta entrega prepara CP4. Les mètriques no s’avaluen per superar un llindar màgic: importa que el procés siga correcte i que sapieu explicar el resultat.

<a id="setmana-6"></a>
## Setmana 6 · Construir el dashboard i defensar decisions

**Objectiu:** presentar una proposta que la direcció puga entendre i utilitzar.

### Píndoles

- [Dashboards i Power BI](PINDOLES/dashboards-i-powerbi.md): triar KPIs i visuals segons la pregunta.
- [Visualització](PINDOLES/visualitzacio-amb-matplotlib-i-seaborn.md): llegibilitat i comunicació de resultats, si es necessita reforç.

### Materials

- [Briefing del panell](MATERIALS_PRACTICS/dashboards/01_briefing_powerbi.md).
- [KPIs i visuals](MATERIALS_PRACTICS/dashboards/02_kpis_i_visuals.md).
- [Model de taules](MATERIALS_PRACTICS/dashboards/03_model_taules.md).
- Resultats propis de vendes, validació, segments i prediccions.

### Tasques

1. Dissenyeu el panell en paper abans de construir-lo. Assigneu una pregunta o decisió a cada visual.
2. Incloeu una lectura de vendes o ingressos, comparació per canal/producte, perfils de client i conclusions. Separeu clarament previsió i dades observades.
3. Eviteu duplicar vendes amb unions incorrectes. No sumeu preus ni percentatges; justifiqueu les agregacions.
4. Prepareu la [memòria](#memoria) i el repositori reproduïble. Mostreu de quins resultats ix cada recomanació.
5. Prepareu la defensa de 8–10 minuts: problema, dades, comparació, segments, demo del panell, decisions i límits.
6. Completeu l’[autoavaluació](#autoavaluacio) i reviseu la [rúbrica](#avaluacio).

### Entrega final · CP4

- Notebooks executats amb conclusions i instruccions per repetir-los.
- Comparativa en validació, decisió de model i mètriques de prova reservada.
- Segmentació i almenys dues interpretacions comercials útils.
- Prediccions de juliol identificades com a previsió.
- Dashboard o visual equivalent, fitxer o enllaç accessible.
- Memòria amb recomanacions, limitacions i repartiment de treball.
- Defensa i autoavaluació.

**Comprovació mínima de defensa:** una comparativa entre models, dos perfils útils i una recomanació concreta que la direcció podria considerar. Cada membre ha de poder explicar la seua aportació i el fil general del projecte.

<a id="registre"></a>
## Registre de treball i revisions

Manteniu este registre en la còpia de treball de l’equip o en el repositori. No cal crear una altra guia del projecte.

| Setmana | Evidència: fitxer o enllaç | Què funciona / què falta | Decisió i motiu | Revisió docent i pròxim pas |
|---|---|---|---|---|
| 1 · CP1 | … | … | … | … |
| 2 · CP2 | … | … | … | … |
| 3 | … | … | … | … |
| 4 · CP3 | … | … | … | … |
| 5 | … | … | … | … |
| 6 · CP4 | … | … | … | … |

En cada checkpoint indiqueu **equip, data, objectiu, treball acabat, bloqueig, proves fetes, decisió tècnica, alternatives descartades, feedback i acció següent**. El professorat pot valorar comprensió, autonomia i qualitat tècnica amb nivell alt, mitjà o baix per orientar el progrés; això no substituïx la rúbrica final.

<a id="repositori"></a>
## Organització del treball de l’equip

```text
equip_bicitierra/
  README.md
  docs/          memòria, decisions i seguiment
  data/          originals conservats i dades derivades diferenciades
  notebooks/     exploració, modelatge i segmentació
  src/           funcions reutilitzables, si en creeu
  tests/         comprovacions de dades o codi, si escau
  evidencies/    mètriques, prediccions, captures i resultats del panell
```

El README de l’equip ha d’indicar objectiu, membres, estructura, dependències, ordre d’execució i limitacions. Si traslladeu els notebooks al vostre repositori, adapteu les rutes de dades. En el paquet lliurat, els notebooks troben els CSV en `../dades/` respecte de la seua carpeta.

<a id="memoria"></a>
## Estructura de la memòria final

1. **Resum executiu:** problema, proposta i valor per a l’empresa.
2. **Dades i flux de treball:** fonts sintètiques, granularitat, qualitat, transformacions, eines i dependències.
3. **Predicció:** variable objectiu, predictors, dates de les particions, models, mètriques i elecció.
4. **Segmentació:** variables, tècnica, perfils, interpretació i accions.
5. **Proves i resultats:** errors, resultats reservats, dashboard i recomanacions.
6. **Límits i millores:** què no es pot concloure, riscos i següents passos.
7. **Repartiment del treball:** aportacions, decisions compartides i dificultats resoltes.

<a id="autoavaluacio"></a>
## Autoavaluació de l’equip

- Qui ha assumit l’anàlisi, les dades, el modelatge, la segmentació, la visualització i la documentació?
- Quina ha sigut la millor decisió i quina evidència la sustenta?
- Quin problema ha costat més i com s’ha resolt?
- Què canviaríeu si tornàreu a començar?
- Quin nivell d’autonomia heu assolit i en què encara necessiteu suport?
- Cada membre explica una aportació concreta i un aspecte que necessita reforçar.

<a id="avaluacio"></a>
## Avaluació i evidències

S’aplica l’escala existent: **1 molt insuficient · 2 insuficient · 3 acceptable · 4 notable · 5 excel·lent**. Els pesos orientatius del projecte continuen sent **20% per criteri**; el professorat confirmarà l’aplicació en la programació del mòdul. La rúbrica de defensa de més avall orienta l’observació de la presentació i no afegix una segona ponderació automàtica.

### 1. EDA i qualitat de dades · 20%

| Nivell | Descripció |
|---|---|
| 1 | No hi ha EDA útil o s’ignoren problemes bàsics de qualitat. |
| 2 | Exploració superficial, sense decisions clares sobre nuls, extrems o incoherències. |
| 3 | EDA correcta i decisions mínimes justificades sobre qualitat. |
| 4 | L’EDA orienta el modelatge i detecta problemes rellevants amb bon criteri. |
| 5 | Connecta qualitat, risc i impacte de negoci de manera clara i sòlida. |

### 2. Modelatge i validació · 20%

| Nivell | Descripció |
|---|---|
| 1 | No hi ha model usable o no està validat. |
| 2 | Hi ha model, però sense baseline clara o mètrica adequada. |
| 3 | Hi ha baseline i comparació bàsica amb un altre model. |
| 4 | Validació coherent, mètriques ben triades i lectura dels errors. |
| 5 | Comparació clara, lectura crítica i justificació sòlida de l’elecció final. |

### 3. Segmentació i lectura de perfils · 20%

| Nivell | Descripció |
|---|---|
| 1 | No hi ha segmentació útil o no es pot interpretar. |
| 2 | Hi ha agrupacions o etiquetes, sense lectura comercial clara. |
| 3 | Segmentació acceptable i perfils bàsics descrits. |
| 4 | Perfils clars i connectats amb decisions comercials plausibles. |
| 5 | Perfils ben descrits que es traduïxen en prioritats o accions concretes. |

### 4. Traducció a negoci i visualització · 20%

| Nivell | Descripció |
|---|---|
| 1 | El treball tècnic no es traduïx en decisions de negoci. |
| 2 | Visualització o conclusions genèriques i desconnectades del problema. |
| 3 | Dashboard i conclusions que permeten una lectura bàsica del negoci. |
| 4 | Dashboard i recomanacions que ajuden a prendre decisions. |
| 5 | Visualització i recomanacions clares, prioritzades i accionables. |

### 5. Criteri tècnic i defensa global · 20%

| Nivell | Descripció |
|---|---|
| 1 | No es justifiquen decisions ni es reconeixen límits. |
| 2 | Justificació parcial i poca consciència de riscos o límits. |
| 3 | Defensa coherent en l’essencial, amb límits principals reconeguts. |
| 4 | Expliquen bé models, segments, visuals i millores possibles. |
| 5 | Defensa madura que connecta dades, mètriques, negoci, límits i següents passos. |

### Full de valoració

| Criteri | Pes orientatiu | Nivell 1–5 | Evidència i observacions |
|---|---:|---|---|
| EDA i qualitat | 20% | … | … |
| Modelatge i validació | 20% | … | … |
| Segmentació i perfils | 20% | … | … |
| Negoci i visualització | 20% | … | … |
| Criteri tècnic i defensa | 20% | … | … |

### Observació de la defensa oral

| Aspecte | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| Comprensió del problema | No l’expliquen o el confonen | Explicació parcial amb errors | Essencial correcte | Connecten problema, solució i context | Explicació clara amb visió crítica |
| Justificació tècnica | Decisions arbitràries | Justificació feble | Decisions principals coherents | Justificació sòlida vinculada al projecte | Comparació madura i consciència de límits |
| Demo funcional | No funciona o no es pot seguir | Parcial i poc clara | Funciona en l’essencial | Mostra bé les parts importants | Mostra amb claredat funcionament, límits i casos especials |
| Comunicació | Confusa | Entenedora amb buits | Clara en general | Ordenada i professional | Sintètica, segura i adaptada al públic |
| Límits i millores | No els detecten | Els enumeren sense explicar | Expliquen límits i una millora | Connecten riscos i millores | Lectura crítica sòlida del sistema i la seua evolució |

Anoteu el nivell i una evidència per aspecte, una fortalesa tècnica, un aspecte a millorar i una recomanació per a la següent iteració.

## Checklist abans de la defensa

- [ ] La pregunta de negoci és concreta i les conclusions hi responen.
- [ ] El procés de dades és reproduïble i les transformacions estan justificades.
- [ ] Cap predictor anticipat incorpora informació posterior del mateix mes.
- [ ] Hi ha una comparació justa i una prova temporal reservada.
- [ ] Els perfils de client tenen una interpretació i una acció proposada.
- [ ] El dashboard diferencia real i previsió i usa agregacions correctes.
- [ ] La memòria, les evidències i les instruccions d’execució estan disponibles.
- [ ] Tots els membres poden explicar decisions, aportacions i límits.
- [ ] La defensa dura 8–10 minuts i mostra una recomanació concreta.

## Índex de consulta de píndoles

| Píndola | Moment principal |
|---|---|
| [Python i entorns](PINDOLES/python-i-entorns.md) | Setmana 1, reforç inicial |
| [Jupyter](PINDOLES/jupyter-notebooks.md) | Setmana 1 |
| [Python per a dades](PINDOLES/python-per-a-dades-i.md) | Setmanes 1–2 |
| [EDA i qualitat](PINDOLES/eda-i-qualitat-de-dades.md) | Setmana 1 |
| [Visualització](PINDOLES/visualitzacio-amb-matplotlib-i-seaborn.md) | Setmanes 2, 4 i 6 |
| [Scikit-learn](PINDOLES/scikit-learn-intro.md) | Setmanes 3–4 |
| [Validació](PINDOLES/validacio-de-models.md) | Setmanes 2, 3 i 5 |
| [Clustering](PINDOLES/clustering-i-segmentacio.md) | Setmana 4 |
| [XAI](PINDOLES/xai-shap-lime.md) | Setmana 5; implementació avançada opcional |
| [Dashboards](PINDOLES/dashboards-i-powerbi.md) | Setmana 6 |
| [MLflow](PINDOLES/mlflow-intro.md) | Ampliació opcional des de setmana 3 |
