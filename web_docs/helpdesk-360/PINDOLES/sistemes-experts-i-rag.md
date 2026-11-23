---
title: Sistemes Experts I RAG
---

# Sistemes Experts I RAG

## Idea clau

Hi ha dues maneres molt diferents de fer respondre una màquina sobre coneixement de l'empresa:

- un **sistema expert** codifica el coneixement com a regles explícites que un expert ha escrit
- un **RAG** recupera fragments de documents reals perquè un `LLM` els use com a base de la resposta

La tria no és "el millor de cada tipus", sinó "quina classe de coneixement tinc i com ha de respondre el sistema". Un sistema expert excel·lix quan la resposta ha de ser exacta, estable i justificable. Un `RAG` excel·lix quan la resposta requerix llegir documents extensos en llenguatge natural.

## Què és un sistema expert

Un sistema expert és un programa que reprodueix el raonament d'un expert humà a partir de coneixement explícit.

En compte de xifres i probabilitats, treballa amb:

- fets sobre el cas actual
- regles del tipus `si ... llavors ...`
- un motor que aplica estes regles en ordre lògic

La característica més important per a principiants és esta: **el coneixement està escrit per algú i es pot llegir**. Si el sistema decideix una cosa, el podem preguntar per què, i pot contestar-nos amb la cadena de regles que ha seguit.

Un sistema expert no aprén de dades. Millora quan algú escriu millor les regles.

## Peces d'un sistema expert

1. **Base de coneixement**: el conjunt de regles `si ... llavors ...` que sap el sistema.
2. **Memòria de treball**: els fets concrets del cas que s'està resolent.
3. **Motor d'inferència**: el programari que busca quines regles es poden aplicar i en quin ordre.
4. **Interfície d'explicació**: com el sistema explica la decisió mostrant les regles que ha usat.

## Com funciona un sistema expert

El flux bàsic és:

1. arriben els fets del cas (una petició, un valor, una situació)
2. el motor busca regles els antecedents de les quals es compleixen amb eixos fets
3. aplica les regles trobades i afegeix els conseqüents com a fets nous
4. repetix fins que no queda cap regla aplicable o s'arriba a una conclusió
5. el sistema pot mostrar la cadena d'inferència per justificar la resposta

Dit més senzill: és com seguir un protocol escrit pas a pas, però amb la garantia que el protocol no es salta cap pas.

## Exemple simple

Amb tres regles podem resoldre una casuística típica del `Helpdesk`:

- `si` intents_fallits >= 5 `llavors` compte_bloquejat = cert
- `si` compte_bloquejat `llavors` demanar verificació addicional
- `si` usuari_verificat `llavors` desbloquejar el compte

Si arriba un cas amb `intents_fallits = 7`, el motor aplica les tres regles en cadena i acaba desbloquejant el compte només quan l'usuari està verificat. Si algú pregunta per què, la resposta és directa: per la regla número 1.

Estes tres regles no necessiten cap `LLM`, cap corpus ni cap `embedding`. Necessiten criteri de qui les escriu.

## Què és i què no és un `RAG`

Un `RAG` no codifica regles. Treballa amb documents:

1. es reuneix un corpus de documents interns
2. els documents es trossegen i s'insereixen en una base vectorial
3. davant d'una pregunta, es recuperen els fragments més rellevants
4. un `LLM` redacta la resposta usant només eixos fragments

La part "intel·ligent" del `RAG` no és escriure regles, sinó decidir quins trossos de document són rellevants per a la pregunta i evitar que el model improvise sense evidència.

Per aprofundir en el patró complet, vegeu la píndola `RAG i Embeddings`.

## Sistemes experts vs `RAG`

| Aspecte | Sistema expert | `RAG` |
| --- | --- | --- |
| On viu el coneixement | en regles escrites per experts | en documents de l'empresa |
| Com decideix | el motor d'inferència aplica regles | recupera fragments i el `LLM` redacta |
| Determinis | sí: mateixa entrada, mateixa eixida | pot variar lleugerament entre respostes |
| Explicació de la resposta | cadena de regles visible i revisable | una resposta pot citar fragments, però la justificació és parcial |
| Com s'actualitza | editant regles | actualitzant el corpus |
| Què fa quan no sap | no activa cap regla i ho diu | ha de dir "no ho sé" si els `guardrails` estan ben posats |
| Amb text lliure | costa: cal traduir-lo a fets | funciona bé: entén llenguatge natural |
| Cost principal | modelar el coneixement en regles | preparar i mantenir el corpus |

## Quan funciona millor un sistema expert

- quan la resposta ha de ser **exacta i estable** (no pot variar el missatge entre dues consultes)
- quan les regles de decisió són **clares i pocs canviants** (prioritats, bloquejos, validacions)
- quan necessitem **justificar** la decisió davant d'una auditoria o d'un responsable
- quan hi ha **poc text lliure**: l'entrada es pot convertir en fets concrets
- quan el nombre de casos possibles es pot cobrir amb un nombre raonable de regles

En estos casos, un sistema expert sol ser més barat i més fiable que muntar un `RAG`.

## Quan funciona millor un `RAG`

- quan el coneixement és un **conjunt gran de documents en llenguatge natural** que canvien amb freqüència
- quan les preguntes són **obertes** i no es poden reduir a regles `si ... llavors ...`
- quan cal llegir diversos fragments abans de respondre (manuals, polítiques, procediments)
- quan les regles serien massa nombroses, massa fràgils o impossibles de mantenir

Per exemple: explicar la política de VPN d'una empresa amb cent pàgines d'instruccions és molt més fàcil amb `RAG` que intentant escriure totes les combinacions com a regles.

## I el `LLM` sol?

Un `LLM` sense context pot sonar convincent sense tindre ni idea de la documentació de l'empresa. Per això no es compara directament amb un sistema expert: comparar-lo amb regles seria enganyós.

- el sistema expert diu el que les regles diuen
- el `RAG` diu el que els documents diuen
- el `LLM` sol diu el que sembla plausible

El `LLM` passa a ser útil quan té una font d'evidència (documents del `RAG`) o quan redacta dins d'un marc controlat de `guardrails`.

## Com es complementen

No cal triar només un. Un patró habitual en projectes reals:

1. unes **regles** decideixen la via del cas (prioritat, acció requerida, derivació)
2. un **RAG** aporta la documentació quan la resposta depén d'un document
3. el **LLM** redacta la resposta final amb eixa evidència
4. els **guardrails** frenen el model si no hi ha prou context

Per exemple: el `Helpdesk` pot usar regles per a gestionar bloquejos i prioritats, i un `RAG` per a explicar procediments interns. Cap dels dos substituïx l'altre; cada peça resol el que sap fer millor.

## Mini pràctica

Classifiqueu estes tres consultes segons si les resoldríeu amb regles d'un sistema expert, amb documentació via `RAG`, o amb cap dels dos:

1. "Què faig si el compte queda bloquejat després de 5 intents fallits?"
2. "Quina és la política de despeses del departament de compres?"
3. "Quant costarà ampliar la flota de vehicles l'any que ve?"

## Solució orientativa

1. Regla clara i estable: un sistema expert (o una condició de codi) la resol directament.
2. Depén d'un document intern: un `RAG` és la via adequada.
3. Ni regla ni corpus: és una consulta de dades i projecció que necessita una altra capa del sistema.

## Resum final

Un sistema expert i un `RAG` resolen problemes diferents. Les regles són ideals quan la decisió ha de ser exacta, estable i justificable; el `RAG` és ideal quan la resposta depén de documents extensos i canviants.

Entendre eixa diferència evita el defecte típic de voler resoldre-ho tot amb `RAG`, i també el de pretendre que unes poques regles cobrisquen un corpus enorme.

## Com portar-ho a aula

- `P1`: usar regles per a prioritat, bloqueig i derivació, i reservar el `RAG` per a la documentació interna
- `P5`: diferenciar la capa de regles operatives de la capa documental de l'assistent
- criteri docent: si l'alumnat sap dir quan una resposta és "una regla" o "un document", ja ha entés la peça central

## Vegeu també

- `RAG i Embeddings`
- `Prompt Engineering I Guardrails`
- `MongoDB I Vector DB`