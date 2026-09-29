# Glossari de termes tècnics

Glossari de consulta ràpida amb el vocabulari tècnic que apareix al llarg del curs d'especialització en IA i Big Data. Cada entrada inclou l'àmbit al qual pertany entre claudàtors.

**Àmbits:** [IA] Intel·ligència Artificial · [ML] Machine Learning · [Dades] Ciència de dades · [BBDD] Bases de dades · [Big Data] · [Streaming] · [IoT] · [Observabilitat] · [DevOps] Desenvolupament i operació · [Visualització] · [Desenvolupament] · [Seguretat] · [Context] Expressions pròpies del context de negoci en què treballen els projectes.

---

## A

- **Accuracy (exactitud)** [ML] — Mètrica que mesura quants encerts hi ha en relació amb el total de prediccions. Cal mirar-la amb cautela quan les classes del dataset estan desequilibrades.

- **Agent (d'IA)** [IA] — Sistema que percep l'entorn, decideix i actua per assolir un objectiu. Els agents simples s'integren amb freqüència dins d'una aplicació.

- **Agregació** [BBDD] — Operació que resumeix un grup de registres o documents (suma, mitjana, comptatge). Més enllà de SQL, és típica de MongoDB i indispensable als dashboards (Projecte P2).

- **Anàlisi de sentiments** [IA] — Tasca de PLN que identifica i classifica opinions o emocions expressades en text (positiu, negatiu, neutral), útil per a monitoritzar opinions de clients o xarxes socials.

- **API** *(Application Programming Interface)* [Desenvolupament] — Interfície que permet que dos sistemes es comuniquen i intercanvien dades de manera estandarditzada (per exemple, via REST o GraphQL).

- **Aprenentatge no supervisat** [ML] — Tipus de ML que treballa sense etiquetes per descobrir estructures ocultes en les dades, com ara grups de clients (clustering).

- **Aprenentatge per reforç** *(reinforcement learning)* [ML] — Tipus de ML en què un agent aprèn a prendre decisions mitjançant proves i errors, rebent recompenses o sancions per les seues accions (entorn, política, recompensa).

- **Aprenentatge supervisat** [ML] — Tipus de ML en què el model aprèn a partir de dades etiquetades, per fer classificacions o prediccions de valors numèrics.

- **Arbre de decisió** [ML] — Model que divideix les dades en branques mitjançant decisions successives. És la base de tècniques més potents com Random Forest.

- **Arquitectura** [Desenvolupament] — Disseny d'alt nivell del sistema: quines peces el componen (dades, model, aplicació, eixida), com es connecten i per què s'han triat aquestes tecnologies.

- **Automatització** [DevOps] — Conversió de tasques manuals en processos automàtics, per exemple mitjançant workflows.

- **Avro** [Big Data] — Sistema de serialització de dades de codi obert que utilitza esquemes JSON i dades binàries compactes, dissenyat per a Big Data i fluxos de streaming (compatible amb Kafka i Schema Registry).

## B

- **Baseline** [ML] — Model o solució de referència, simple i barat de construir, contra el qual es comparen les solucions més avançades. Sense baseline no es pot justificar que un model "funciona".

- **Base de coneixement documental** [IA] — Repositori de documents preparats i organitzats que un sistema utilitza per recuperar informació rellevant. Ha d'estar neta i localitzable, no ser una carpeta caòtica.

- **Big Data** [Big Data] — Tractament de volums de dades tan grans o ràpids que calen infraestructures distribuïdes (Spark, Cassandra, Kafka) en lloc d'aproximacions tradicionals.

- **Biaix** *(bias)* [IA] — Desviació sistemàtica en les dades o en el model que produeix resultats esbiaixats o discriminatoris. És un risc ètic que cal identificar i mitigar.

- **BI** *(Business Intelligence)* [Visualització] — Conjunt d'eines i processos per transformar dades en informació útil per a la presa de decisions empresarials.

- **Bottleneck (coll de botella)** [Context] — Punt de congestió d'un procés que redueix la capacitat global del sistema. En el projecte logístic es vol predir en les franges de màxima activitat.

## C

- **Caixa negra** *(black box)* [IA] — Sistema lògic intern del qual no es pot inspeccionar, i que només s'avalua per les seues entrades i eixides. Els models de deep learning tendeixen a ser-ho.

- **Cassandra** [Big Data] — Base de dades NoSQL distribuïda, dissenyada per a grans volums de dades amb alta disponibilitat i particionat horitzontal.

- **Checksum** [Dades] — Valor calculat a partir d'un fitxer o conjunt de dades que permet verificar que no s'han corromput ni alterat.

- **Chunk / Chunking** [IA] — Divisió de documents en fragments més xicotets per poder-los indexar i processar, molt típica en fluxos RAG.

- **Classificació** [ML] — Tasca d'aprenentatge supervisat que assigna a cada dada una categoria o etiqueta entre un conjunt predefinit. Al Projecte P1 s'aplica a la classificació de tickets.

- **Cloud (núvol)** [DevOps] — Model de desplegament en què els serveis s'executen en infraestructura remota i externalitzada en lloc d'equips locals.

- **Clustering** [ML] — Tècnica d'aprenentatge no supervisat que agrupa dades semblants en clústers, sense etiquetes prèvies. La base de la segmentació de clients.

- **CNN** *(Convolutional Neural Network)* [IA] — Xarxa neuronal convolucional, arquitectura de deep learning especialitzada a processar imatges. És la base de models com YOLO.

- **Codificació** *(encoding)* [Dades] — Transformació de variables categòriques en valors numèrics perquè el model les puga processar.

- **Consistència (de dades)** [BBDD] — Propietat que garanteix que les dades romanen correctes i coherents en sistemes distribuïts i replicats.

- **Consumer (consumidor)** [Streaming] — Aplicació que es connecta a un sistema de streaming (Kafka) i processa els missatges publicats en els topics.

- **Contenidor** [DevOps] — Unitat lleugera que empaqueta una aplicació amb totes les seues dependències perquè s'execute de manera aïllada i igual en qualsevol entorn.

- **Contracte de dades** *(data contract)* [Big Data] — Acord formal sobre l'estructura i la qualitat de les dades entre qui les produeix i qui les consumeix. Garanteix l'evolució controlada dels formats.

- **Corpus** [IA] — Conjunt de documents o textos que alimenten un sistema de classificació o un flux RAG. Ha de ser propi del projecte, no un chatbot genèric.

- **Correlació** [Dades] — Relació estadística entre dues variables: fins a quin punt una varia de manera associada a l'altra.

- **Cross-validation (validació creuada)** [ML] — Tècnica que divideix les dades en diverses parts i alterna entrenament i avaluació per estimar millor la capacitat de generalització del model.

- **Cua de camions** *(truck queue)* [Context] — Indicador operatiu de saturació d'un terminal: el volum de camions en espera. Si supera el llindar operatiu, es genera l'alerta.

## D

- **Dades documentals** [BBDD] — Dades emmagatzemades en format de document (per exemple, en MongoDB), en lloc de taules relacionals rígides.

- **Dades en temps real** [Big Data] — Dades que es generen i processen de manera (quasi) immediata, com els esdeveniments de sensors o terminals.

- **Dades històriques** [Dades] — Registres recollits en el passat, utilitzats com a base per a la construcció i validació de models predictius.

- **Dades tabulars** [Dades] — Dades organitzades en taules de files i columnes, el format estàndard de treball amb Pandas i Power BI.

- **Dashboard** [Visualització] — Panell visual que mostra dades, KPIs i alertes consolidades per ajudar a prendre decisions. No ha de mostrar tot: només el que ajuda a decidir millor.

- **Dashboard executiu** [Visualització] — Panell dissenyat per a la direcció, pensat per a la lectura ràpida d'indicadors estratègics.

- **Data mining** *(excavació de dades)* [Dades] — Procés d'explorar i analitzar grans volums de dades per descobrir patrons, correlacions i coneixements útils que no són obvis a primera vista.

- **Databricks Lakehouse** [Big Data] — Plataforma unificada que combina les capacitats de data warehouse i data lake sobre una arquitectura oberta, facilitant l'anàlisi i el machine learning sobre grans volums.

- **Dataset (conjunt de dades)** [Dades] — Col·lecció estructurada de dades utilitzada per analitzar, entrenar o validar models.

- **DBSCAN** [ML] — Algorisme de clustering basat en densitat que detecta grups de forma irregular i, a la vegada, identifica punts anòmals (outliers).

- **Decisió de negoci** [Context] — Decisió estratègica empresarial (estoc, campanya, segment de clients) que es recolza en els resultats de les dades i dels models.

- **Deep Learning (DL)** [IA] — Subcamp del machine learning basat en xarxes neuronals profundes, capaç de treballar amb dades complexes com imatges, àudio o també text.

- **Delta Lake** [Big Data] — Capa d'emmagatzematge oberta que aporta transaccions ACID, esquemes evolutius i versionat a data lakes, fent-los més fiables per a analítica i ML.

- **Desplegament (deploy)** [DevOps] — Procés de posar en marxa un servei o aplicació en un entorn operatiu, local o en el núvol.

- **Detecció d'objectes** [IA] — Tasca de visió per computador que localitza i identifica objectes dins d'una imatge, com fa YOLO.

- **Deute tècnic** [Desenvolupament] — Costos d'execució de decisions ràpides (codi poc estructurat, documentació absent) que caldrà "pagar" amb millores futures.

- **Diagrama de dispersió** [Visualització] — Gràfic que mostra la relació entre dues variables numèriques mitjançant punts.

- **Distribució** [Dades] — Forma en què es reparteixen els valors d'una variable (freqüències per valor), permetent detectar patrons i anomalies.

- **Docker** [DevOps] — Plataforma de contenidors que permet construir, desplegar i executar aplicacions de manera aïllada i portable.

- **Docker Compose** [DevOps] — Eina per definir i llançar aplicacions multi-contenidor a partir d'un fitxer de configuració (YAML).

## E

- **EDA** *(Exploratory Data Analysis)* [Dades] — Anàlisi exploratòria de dades: inspecció inicial per entendre l'estructura, patrons, outliers i qualitat d'un dataset abans de modelar.

- **Edge AI** [IA] — IA executada de forma local en el dispositiu de vora (edge), sense dependre d'un servidor central.

- **ELK stack** *(Elasticsearch, Logstash, Kibana)* [Observabilitat] — Conjunt d'eines per a la ingesta, cerca i visualització de logs i altres dades d'operació.

- **Embedding** [IA] — Representació vectorial de text (o d'altres dades) que codifica el seu significat, de manera que valors o conceptes semblants queden a prop en l'espai vectorial.

- **Enginyeria de variables** *(feature engineering)* [ML] — Procés de crear, transformar i seleccionar variables perquè el model aprenga millor.

- **Esdeveniment** *(event)* [Streaming] — Unitat mínima d'informació que flueix en temps real per un sistema de missatgeria, com un canvi d'estat d'un sensor o terminal.

- **Escalat (de variables)** [Dades] — Normalització o estandardització de variables numèriques perquè tinguen rangs comparables dins del model.

- **Esquema de dades** [BBDD] — Definició formal de com s'organitzen les dades: camps, tipus i relacions.

## F

- **F1-score** [ML] — Mitjana harmònica entre precisió i recall; resumeix en un sol nombre l'equilibri entre els dos i és molt usada per valorar classificadors.

- **Fals positiu / fals negatiu** [ML] — Errors de classificació: el model prediu un positiu que no ho és, o no detecta un positiu que ho era. Els falsos positius són especialment problemàtics en entorns operatius.

- **FastAPI** [Desenvolupament] — Framework modern de Python per a crear APIs, incloses les REST.

- **Fine-tuning** *(ajust fi)* [IA] — Procés de prendre un model preentrenat i ajustar-lo amb dades específiques del domini per millorar-ne el rendiment en una tasca concreta.

- **FIWARE / Orion** [IoT] — Plataforma oberta de gestió de context per a IoT; Orion és el "context broker" que gestiona les dades de context i les seues subscripcions en temps real.

- **Flask** [Desenvolupament] — Microframework lleuger de Python per a crear aplicacions web i APIs.

## G

- **Generalització** [ML] — Capacitat d'un model de funcionar bé amb dades que no ha vist durant l'entrenament. És l'objectiu real de qualsevol model.

- **Git** [Desenvolupament] — Sistema de control de versions que permet portar l'historial de canvis del codi i treballar en equip de manera ordenada.

- **Gradient Boosting** [ML] — Tècnica d'ensemble que construeix models de manera seqüencial, corregint els errors dels models anteriors.

- **Grafana** [Observabilitat] — Eina de visualització i dashboarding de mètriques, habitualment acompanyada de Prometheus; genera panells i alertes.

- **GraphQL** [Desenvolupament] — Llenguatge de consulta d'APIs alternatiu a REST que permet al client demanar exactament les dades que necessita.

- **Gradio** [Desenvolupament] — Eina per crear interfícies web interactives per a models d'IA/ML de forma ràpida.

- **Guardrails** [IA] — Mecanismes de seguretat que limiten les respostes d'un sistema d'IA perquè no genere contingut inadequat o fora de context (per exemple, obligar-lo a dir "no ho sé").

## H

- **Heurística** [IA] — Regla pràctica o estratègia que troba solucions prou bones sense explorar totes les possibilitats (base de la cerca en sistemes d'IA).

## I

- **IA (Intel·ligència Artificial)** [IA] — Disciplina que persegueix que les màquines facen tasques que requereixen intel·ligència: raonar, percebre, comprendre llenguatge i aprendre.

- **Iceberg** [Big Data] — Format de taules obert i escalable dissenyat per a data lakes, que permet consultes analítiques eficients, evolució d'esquemes i versionat de dades.

- **Imputació** [Dades] — Tècnica per omplir valors que falten en un dataset amb estimacions raonables, en lloc de descartar els registres.

- **Inferència** [IA] — Execució d'un model ja entrenat sobre dades noves per obtindre prediccions o deteccions (per exemple, passar una imatge a YOLO).

- **Integració de serveis** [Desenvolupament] — Connexió i coordinació de components o serveis perquè funcionen com un sistema únic.

- **Integració vertical** [Desenvolupament] — Flux que recorre totes les capes de la solució de punta a punta: des de la dada fins a la decisió o eixida operativa. Cada projecte ha de mostrar com a mínim una.

- **Integritat de dades** [Dades] — Garantia que les dades són completes, correctes i no han estat alterades de manera no autoritzada.

- **Interpretabilitat** [IA] — Capacitat d'entendre què fa i per què un model; un pas previ a l'explicabilitat.

- **IoT (Internet de les Coses)** [IoT] — Xarxa de dispositius connectats (sensors, actuadors) que recullen i envien dades de l'entorn en temps real.

## K

- **K-Means** [ML] — Algorisme de clustering que agrupa les dades en K grups segons la distància al centróide del grup.

- **Kafka** [Streaming] — Plataforma de missatgeria distribuïda per processar fluxos d'esdeveniments en temps real. Els missatges s'organitzen en topics i els gestionen producers i consumers.

- **KNN** *(K-Nearest Neighbors)* [ML] — Algorisme de classificació que assigna a una dada la classe majoritària dels seus K veïns més pròxims.

- **KPI** *(Key Performance Indicator)* [Visualització] — Indicador clau de rendiment: una mètrica de negoci que ajuda a avaluar l'assoliment d'objectius. Exemples: terminals en risc, cua mitjana, alertes actives.

## L

- **Lakehouse** [Big Data] — Arquitectura de dades que combina les millors característiques dels data lakes (baix cost i flexibilitat) i els data warehouses (fiabilitat i rendiment analític) en una sola plataforma.

- **Lectura executiva / comercial** [Context] — Interpretació dels resultats tècnics en termes de valor per a l'empresa, pensada per a qui pren decisions sense formació tècnica.

- **LIME** [IA] — Mètode d'explicabilitat que explica una predicció concreta de manera local, apropant el comportament del model amb simplificacions.

- **Línia temporal** [Visualització] — Gràfic de línies que mostra l'evolució d'una variable al llarg del temps.

- **Llindar (operatiu)** [Observabilitat] — Valor límit que, en superar-se, activa una alerta o protocol d'actuació (per exemple, una cua de camions que supera la capacitat d'un terminal).

- **LLM** *(Large Language Model)* [IA] — Model de llenguatge gran: xarxa neuronal entrenada amb grans quantitats de text capaç de generar i comprendre llenguatge natural.

- **LLMOps** [IA] — Pràctiques i eines per gestionar el cicle de vida dels LLMs en producció: ajust fi, avaluació, desplegament, monitorització i actualització.

- **Log (registre)** [Observabilitat] — Esdeveniment registrat cronològicament d'activitat del sistema, essencial per a la depuració, l'auditoria i la traçabilitat.

## M

- **Machine Learning (ML, aprenentatge automàtic)** [ML] — Disciplina en què els sistemes aprenen a partir de dades en lloc de ser programats amb regles explícites.

- **MapReduce** [Big Data] — Model de programació distribuïda que processa i genera grans volums de dades en paral·lel (fase de "map" i fase de "reduce"); és la base de Hadoop.

- **Matplotlib** [Desenvolupament] — Llibreria de Python per a la creació de gràfiques i visualitzacions.

- **Matriu de confusió** [ML] — Taula que mostra, per a cada classe, quants encerts i quants errors ha comès un classificador. Permet veure de quina mena són els errors.

- **Mètrica** [ML] — Valor numèric que avalua el rendiment d'un model o sistema (accuracy, precisió, recall, F1...). Cal triar la mètrica adequada a l'objectiu.

- **MLflow** [IA] — Plataforma per a la gestió del cicle de vida de models: tracking d'experiments, versions i desplegament.

- **MLOps** [IA] — Pràctiques per portar models de ML a producció de manera fiable i automatitzable, com es fa amb el codi tradicional.

- **Model (predictiu)** [ML] — Resultat de l'entrenament: una funció capaç de predir valors o categories a partir de noves entrades. Ha d'estar justificat i comparat amb un baseline.

- **Modelatge de dades** [BBDD] — Disseny de l'estructura de les dades (documents, taules, particions) perquè les consultes siguen eficients.

- **MongoDB** [BBDD] — Base de dades NoSQL orientada a documents, molt usada per a dades persistents com tickets o registres d'interacció.

- **Monitorització** [Observabilitat] — Seguiment continu de l'estat del sistema (dades, serveis, infraestructura) per detectar anomalies i riscos.

- **MQTT** [IoT] — Protocol de missatgeria lleuger pensat per a la comunicació entre dispositius IoT en xarxes d'amplada de banda reduïda.

- **MVP** *(Minimum Viable Product)* [Desenvolupament] — Producte mínim viable: versió reduïda però funcional que demostra el valor central de la solució.

## N

- **n8n** [DevOps] — Eina d'automatització de fluxos de treball (workflows) de codi obert, que orquestra serveis externs (correu, missatgeria, OCR, IA).

- **Neteja de dades** [Dades] — Eliminació o correcció de dades errònies, incompletes o incoherents abans d'analitzar.

- **Node-RED** [IoT] — Eina de programació visual basada en fluxos que connecta dispositius IoT, APIs i serveis a partir de nodes.

- **NoSQL** [BBDD] — Família de bases de dades no relacionals (documents, columnes, clau-valor, grafs), pensades per a escalar horitzontalment.

- **Notebook (de Jupyter)** [Desenvolupament] — Document que combina codi executable, text i resultats visuals, ideal per a exploració, modelatge i pràctiques guiades.

- **NumPy** [Desenvolupament] — Llibreria de Python per al càlcul numèric amb arrays i operacions matricials.

## O

- **Observabilitat** [Observabilitat] — Capacitat de comprendre l'estat intern d'un sistema a partir de les seues eixides externes: logs, mètriques i traces.

- **Objectius de direcció** [Context] — Fites que la direcció de l'empresa vol assolir i que orienten el projecte tècnic (reduir cues, detectar sensors avariats, millorar la satisfacció...).

- **OpenCV (cv2)** [IA] — Llibreria de visió per computador per al processament d'imatges (llegir, convertir a escala de grisos, redimensionar).

- **Orquestració** [DevOps] — Coordinació automatitzada de múltiples serveis o contenidors perquè funcionen conjuntament.

- **Outlier (valor atípic)** [Dades] — Punt aïllat que s'aparta del comportament general de la resta de les dades; pot ser un error o una dada realment singular.

- **Overfitting** *(sobreajust)* [ML] — Situació en què un model aprèn massa bé les dades d'entrenament (incloent el soroll) i generalitza malament amb dades noves. Es detecta quan l'error d'entrenament és molt menor que el de prova.

## P

- **Pandas** [Desenvolupament] — Llibreria de Python per a la manipulació i anàlisi de dades tabulars (DataFrames), el cavall de treball de la ciència de dades.

- **Parquet** [Big Data] — Format de fitxer de dades columnar optimitzat per a l'emmagatzematge i l'anàlisi eficient de grans volums de dades en entorns distribuïts.

- **Particionat** [BBDD] — Estratègia de distribució de les dades entre nodes per obtenir escalabilitat i disponibilitat, característica de Cassandra.

- **Payload** [IoT] — Càrrega d'informació que un dispositiu (per exemple, un sensor) envia dins d'un missatge.

- **PCA** *(Principal Component Analysis)* [ML] — Tècnica de reducció de dimensionalitat que transforma variables correlacionades en uns quants components principals, per simplificar i visualitzar.

- **Pipeline** [ML] — Cadena ordenada de passos que transforma les dades des de l'entrada fins al resultat (neteja, preprocessament, model, eixida).

- **PLN** *(Processament de Llenguatge Natural, NLP)* [IA] — Camp de la IA que treballa la interacció entre ordinadors i llenguatge humà: comprensió, generació i anàlisi de text.

- **Power BI** [Visualització] — Eina de Microsoft per crear dashboards i informes interactius a partir de dades de l'organització (Projecte P2).

- **Precisió (precision)** [ML] — Mètrica: dels elements predits com a positius, quants són realment positius. Baixa precisió vol dir molts falsos positius.

- **Preprocessament** [Dades] — Preparació de les dades abans de modelar: neteja, imputació, codificació i escalat.

- **Preguntes de negoci** [Context] — Problemes formulats en llenguatge empresarial que el sistema de dades ha de respondre (per exemple, "com afecta el descompte a les vendes?"). No són preguntes tècniques: guien l'anàlisi i el disseny del model.

- **Producer (productor)** [Streaming] — Aplicació que publica missatges en els topics d'un sistema de streaming com Kafka.

- **Prometheus** [Observabilitat] — Sistema de monitorització i recollida de mètriques que alimenta alertes i panells, habitualment visualitzades a Grafana.

- **Prompt engineering** [IA] — Disseny i afinament de les instruccions (prompts) que se li donen a un LLM per obtindre respostes més útils i fiables.

- **PyTorch** [Desenvolupament] — Framework de deep learning per construir i entrenar xarxes neuronals.

- **Python** [Desenvolupament] — Llenguatge de programació principal del curs, amb un ecosistema massiu per a dades i IA.

## Q

- **Qualitat de dades** [Dades] — Grau de correcció, completitud i fiabilitat d'un dataset. Cal revisar-la abans de modelar.

## R

- **RAG** *(Retrieval-Augmented Generation)* [IA] — Tècnica que genera respostes amb ajuda d'un LLM però augmentades amb documents recuperats d'una base de coneixement. Primer recupera, després genera, i ha de saber dir "no ho sé" si no hi ha context (Projecte P1).

- **Random Forest** [ML] — Ensemble de molts arbres de decisió que combina les seues prediccions per millorar l'estabilitat i la precisió.

- **Recall (sensibilitat)** [ML] — Mètrica: dels elements realment positius, quants ha detectat el model. Baix recall vol dir que es perden casos positius.

- **Recomanacions accionables** [Context] — Conclusions pràctiques i concretes que la direcció pot aplicar directament, derivades de l'anàlisi de dades.

- **Regressió** [ML] — Tipus d'algorisme d'aprenentatge supervisat que prediu un valor numèric continu (vendes, minuts de cua, temperatura...).

- **Repositori (repo)** [Desenvolupament] — Espai on es guarda el codi d'un projecte amb el seu històric de versions (Git). 

- **REST** [Desenvolupament] — Estil arquitectònic per a APIs web basat en recursos i verbs HTTP (GET, POST, PUT, DELETE).

- **RGPD** [Seguretat] — Reglament europeu de protecció de dades personals; tot sistema que tracte dades personals ha de complir-lo.

- **ROC / AUC** [ML] — Curva ROC i àrea sota la corba: mètriques que valoren la capacitat del model per separar classes al llarg de diversos llindars.

- **RPA** *(Robotic Process Automation)* [IA] — Automatització de processos basats en regles mitjançant "robots" de programari, sovint contextualitzada amb IA.

## S

- **S3** *(Amazon Simple Storage Service)* [Big Data] — Servei d'emmagatzematge d'objectes d'Amazon Web Services, àmpliament utilitzat com a base dels data lakes al núvol.

- **scikit-learn** [Desenvolupament] — Llibreria de Python de ML clàssic: classificació, regressió, clustering i preprocessament amb una API coherent.

- **Seaborn** [Desenvolupament] — Llibreria de visualització estadística construïda sobre Matplotlib, amb gràfics més elaborats.

- **Segmentació (de clients)** [ML] — Agrupació de clients en segments amb característiques comunes mitjançant tècniques de clustering. Els segments han de tindre una lectura comercial, no ser només etiquetes.

- **Sensor** [IoT] — Dispositiu que captura dades de l'entorn (temperatura, humitat, estat de maquinària) i les tramet al sistema.

- **Sèrie temporal** [Dades] — Seqüència de dades ordenada cronològicament. S'utilitza generalment per a predicció d'evolució.

- **Serverless** [DevOps] — Model de desplegament en què el núvol gestiona el servidor; el codi s'executa sota demanda (functions as a service).

- **SHAP** [IA] — Mètode d'explicabilitat que descompon cada predicció i mostra la contribució de cada variable a partir de la teoria de jocs.

- **Schema Registry** [Streaming] — Registre centralitzat d'esquemes que valida i controla l'evolució dels formats de dades en un sistema de streaming.

- **Sistemes experts** [IA] — Sistemes basats en regles i coneixement explícit, contraposats als LLMs dins de l'evolució de la IA.

- **Snowflake** [Big Data] — Plataforma de data cloud que separa l'emmagatzematge i la computació, permetent escalar-los de manera independent i simplificant la gestió de dades.

- **Soroll (en dades)** [Dades] — Dades no útils, incorrectes o irrelevants que interferixen en l'anàlisi o el model.

- **Spark** [Big Data] — Motor de processament distribuït per a grans volums de dades i analítica sobre clusters.

- **Streaming** [Streaming] — Processament continu de fluxos de dades a mesura que es generen, en lloc de per lots.

- **Streamlit** [Desenvolupament] — Eina per crear aplicacions web interactives a partir de scripts de Python, molt usada per a demos i panells.

- **SVM** *(Support Vector Machine)* [ML] — Algorisme de classificació que busca el hiperplà que separa millor les classes.

## T

- **Target (variable objectiu)** [ML] — La variable que el model vol predir; la resta de dades són les característiques o variables independents.

- **Taxonomia** [IA] — Estructura ordenada de categories i prioritats que un sistema de classificació utilitza per etiquetar.

- **Token** [IA] — Unitat mínima de text amb la qual treballen els models de llenguatge (paraula, fragment o caràcter); el procés de dividir el text es diu tokenització.

- **Topic (tema)** [Streaming] — Canal lògic de Kafka on s'agrupen i s'emmagatzemen els missatges d'un mateix assumpte.

- **Traçabilitat** [Dades] — Capacitat de seguir i documentar l'origen i el recorregut de cada dada o resposta del sistema. Cal poder justificar d'on ix cada resultat.

- **Train/test (partició)** [ML] — Divisió del dataset en un conjunt d'entrenament i un de prova per entrenar i avaluar el model amb dades no vistes.

- **Transformers** [IA] — Arquitectura de xarxes neuronals sobre la qual es construeixen els LLMs moderns.

- **Tracking (d'experiments)** [IA] — Registre sistemàtic de paràmetres, mètriques i versions dels experiments de ML, per exemple amb MLflow.

- **Transfer learning** *(aprenentatge per transferència)* [ML] — Tècnica que reaprofita un model entrenat en una tasca com a punt de partida per a una altra tasca similar, reduint el temps i les dades necessaris.

## U

- **UI** *(User Interface)* [Desenvolupament] — Interfície gràfica amb la qual interactua l'usuari final.

- **Underfitting** *(infraajust)* [ML] — Situació en què un model és massa simple per capturar els patrons de les dades, i obté resultats dolents tant en entrenament com en prova.

## V

- **Valor perdut** [Dades] — Dada absent en un dataset; cal decidir entre imputar-la o descartar el registre.

- **Vector DB (Base de dades vectorial)** [BBDD] — Base de dades pensada per emmagatzemar i cercar embeddings de forma eficient; el suport funcional del RAG.

- **Vertical funcional** [Desenvolupament] — Versió reduïda però completa del sistema que travessa totes les capes (dada → anàlisi → eixida) i demostra que el flux principal funciona.

- **Visió per computador** [IA] — Camp de la IA que dona a les màquines la capacitat d'interpretar imatges i vídeo.

- **Visualització de dades** [Visualització] — Representació gràfica de dades per facilitar-ne la interpretació i la presa de decisions.

## W

- **Web scraping** [Desenvolupament] — Tècnica per extreure automàticament dades de pàgines web, transformant el contingut HTML en dades estructurades per al seu anàlisi.

- **Workflow** [DevOps] — Flux de treball automatitzat que orquestra passos, condicions i respostes entre serveis.

## X

- **XAI** *(Explainable AI, IA explicable)* [IA] — Camp d'IA que aporta tècniques per fer comprensibles i justificables les decisions dels models (SHAP, LIME, importàncies).

- **Xarxa neuronal (artificial)** [IA] — Model inspirat en el cervell format per capes de neurones que aprén representacions a partir de les dades; la base del deep learning.

- **XGBoost / CatBoost / LightGBM** [ML] — Implementacions optimitzades i escalables de la tècnica Gradient Boosting, molt utilitzades en competicions i projectes reals per la seua alta precisió.

## Y

- **YOLO** *(You Only Look Once)* [IA] — Arquitectura de detecció d'objectes en temps real sobre imatges i vídeo. S'utilitza per inferència (no entrenament) amb la variant YOLOv8n, per exemple per a detecció visual en el projecte IoT/logística.

---

## Índex per àmbits

| Àmbit | Termes |
|---|---|
| [IA] Intel·ligència Artificial | Anàlisi de sentiments, Agent, Embedding, LLM, LLMOps, RAG, PLN, Fine-tuning, Token, Tokenització, Prompt engineering, Guardrails, XAI, SHAP, LIME, Interpretabilitat, Caixa negra, Sistemes experts, Visió per computador, YOLO, Detecció d'objectes, Inferència, CNN, Transformers, Deep Learning, Xarxa neuronal, RPA, Edge AI, MLOps, MLflow, Tracking, Base de coneixement documental, Corpus, Taxonomia, Chunk, Biaix, Heurística |
| [ML] Machine Learning | Machine Learning, Aprenentatge supervisat, Aprenentatge no supervisat, Aprenentatge per reforç, Baseline, Classificació, Regressió, Clustering, K-Means, DBSCAN, PCA, KNN, SVM, Arbre de decisió, Random Forest, Gradient Boosting, Cross-validation, Train/test, Matriu de confusió, Accuracy, Precisió, Recall, F1-score, ROC/AUC, Fals positiu/fals negatiu, Mètrica, Generalització, Valor objectiu, Enginyeria de variables, Model predictiu, Segmentació de clients, Pipeline, Overfitting, Underfitting, Transfer learning, XGBoost / CatBoost / LightGBM |
| [Dades] Ciència de dades | EDA, Dataset, Qualitat de dades, Neteja de dades, Data mining, Preprocessament, Imputació, Codificació, Escalat, Outlier, Valor perdut, Sèrie temporal, Correlació, Distribució, Soroll, Dades històriques, Dades tabulars, Dades en temps real, Integritat de dades, Traçabilitat, Checksum |
| [BBDD] Bases de dades | MongoDB, Cassandra, NoSQL, Esquema de dades, Modelatge de dades, Agregació, Particionat, Consistència, Vector DB, Dades documentals |
| [Big Data] | Big Data, Spark, MapReduce, Avro, Parquet, Delta Lake, Iceberg, Lakehouse, Databricks Lakehouse, S3, Snowflake |
| [Streaming] | Kafka, Topic, Producer, Consumer, Schema Registry, Contracte de dades, Esdeveniment, Streaming |
| [IoT] | IoT, Sensor, MQTT, Node-RED, FIWARE/Orion, Payload |
| [Observabilitat] | Observabilitat, Monitorització, Log, Mètrica, Alerta, Llindar, Prometheus, Grafana, ELK stack | 
| [DevOps] | Docker, Docker Compose, Contenidor, Orquestració, n8n, Workflow, Cloud, Serverless, Automatització, Desplegament |
| [Visualització] | Dashboard, Dashboard executiu, KPI, Power BI, Visualització de dades, BI, Línia temporal, Diagrama de dispersió |
| [Desenvolupament] | Python, Entorn virtual, NumPy, Pandas, Matplotlib, Seaborn, scikit-learn, PyTorch, OpenCV, Notebook, API, REST, GraphQL, FastAPI, Flask, Streamlit, Gradio, UI, Git, Repositori, Arquitectura, Integració de serveis, Integració vertical, Vertical funcional, MVP, Deute tècnic, Autenticació, Web scraping |
| [Seguretat] | RGPD, Autenticació |
| [Context] Expressions de negoci | Preguntes de negoci, Objectius de direcció, Recomanacions accionables, Decisió de negoci, Lectura executiva/comercial, Bottleneck (coll de botella), Cua de camions, Triatge |


## Per aprofundir

[Obri la píndola ampliada, amb pràctiques i exercicis](../PINDOLES_AMPLIADES/docs/glossari_terms/index.md).
