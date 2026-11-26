---
title: Sistemes basats en regles, sistemes experts, LLM i RAG
---

# Sistemes basats en regles, sistemes experts, LLM i RAG

## Per què cal distingir-los

En el projecte Helpdesk apareixen quatre maneres de fer que una màquina "sàpiga" què fer davant d'un ticket. Sovint es confonen perquè totes poden acabar donant una resposta en text. La diferència important no és com de moderna és cada tècnica, sinó **on viu el coneixement** i **qui decideix la resposta**.

| Sistema | On viu el coneixement | Qui produïx la resposta |
|---|---|---|
| Basat en regles | En condicions escrites pel programador | El codi que aplica les condicions |
| Expert | En una base de regles separada del motor, que modela un domini | Un motor d'inferència que encadena regles i pot explicar-les |
| LLM | En els paràmetres del model, apresos de molt de text | El model, generant text probable |
| RAG | En documents externs que es consulten en el moment | Un LLM que redacta a partir dels fragments recuperats |

## 1. Sistema basat en regles

Un sistema basat en regles pren decisions amb condicions explícites del tipus **si passa A, llavors fes B**. Pot ser tan simple com uns quants `if` en Python.

Característiques:

- És determinista: la mateixa entrada dona sempre la mateixa eixida.
- És fàcil de llegir, provar i depurar.
- No aprén de les dades. Només canvia quan algú modifica les regles.
- Cobrix bé el que algú ha previst; el que no ha previst queda sense resposta.

Exemple en el Helpdesk: si el text del ticket conté "vpn" o "certificat", assignar-lo a xarxes. Si no s'activa cap regla, el resultat és `sense_regla`.

Límits: els textos reals són variats ("no em deixa entrar", "user blocked", "invalid credentials"). Cada variant requerix una regla nova, i les regles poden entrar en conflicte entre elles.

## 2. Sistema expert

Un sistema expert és un tipus de sistema basat en regles amb una arquitectura més formal, pensat per a reproduir el raonament d'una persona experta en un domini concret. Els exemples històrics més coneguts són de les dècades de 1970 i 1980, com MYCIN, orientat al diagnòstic mèdic.

Les peces habituals són:

1. **Base de coneixement:** les regles del domini, escrites per experts.
2. **Memòria de treball:** els fets del cas que s'està resolent.
3. **Motor d'inferència:** busca les regles aplicables i les encadena per a arribar a conclusions.
4. **Explicació:** mostra quines regles s'han aplicat i per què.

La diferència amb un conjunt de `if` és que el coneixement està **separat del programa que l'executa**, es pot **encadenar** (una regla produïx un fet que activa una altra) i el sistema pot **justificar** la decisió.

Exemple:

- Si intents_fallits >= 5, llavors compte_bloquejat.
- Si compte_bloquejat i usuari_verificat, llavors desbloquejar.

Quan és adequat: decisions exactes, estables i auditables, com prioritats, bloquejos, validacions o derivacions.

Quan no: quan l'entrada és text lliure i el coneixement és extens o canvia sovint, perquè mantindre les regles té un cost alt.

Relació entre ambdós: tot sistema expert clàssic es basa en regles, però no tot sistema de regles és un sistema expert.

## 3. LLM

Un LLM (*Large Language Model*) és un model de llenguatge entrenat amb grans quantitats de text per a predir quin fragment de text és més probable a continuació. Això li permet entendre instruccions, resumir, traduir, redactar i respondre preguntes en llenguatge natural.

Conceptes bàsics:

- **Prompt:** el text d'entrada, amb instruccions i context.
- **Token:** unitat en què el model divideix el text.
- **Finestra de context:** quantitat màxima de text que el model pot considerar en una consulta.
- **Coneixement paramètric:** el que el model ha après durant l'entrenament, sense una font consultable.

Punts forts: entén variants de llenguatge i redacta respostes naturals sense escriure regles.

Límits que cal conéixer:

- Pot generar respostes plausibles però falses (**al·lucinacions**).
- No coneix els documents interns d'una empresa, ni informació posterior al seu entrenament, llevat que se li proporcionen.
- Pot variar la resposta entre execucions.
- No ofereix, per si mateix, una font verificable.
- Pot seguir instruccions incloses dins del text que processa (**injecció de prompt**).

Un LLM sol no és un sistema de coneixement de l'empresa: és una capacitat de llenguatge.

## 4. RAG

RAG (*Retrieval-Augmented Generation*) combina recuperació d'informació i generació. En lloc de confiar en el que el LLM "recorda", se li donen en cada consulta els fragments de documents que s'han trobat com a rellevants.

Flux:

1. **Preparació:** es reuneix el corpus, es divideix en fragments i es guarden amb metadades (document, fragment, versió).
2. **Indexació:** es calculen representacions dels fragments. Amb *embeddings*, els textos amb significat semblant queden propers en un espai numèric.
3. **Recuperació:** la pregunta es representa de la mateixa manera i es busquen els fragments més pròxims.
4. **Generació:** el LLM redacta la resposta usant només eixos fragments i citant-los.
5. **Control:** si el context no és suficient, el sistema ho diu i deriva.

Què aporta: respostes basades en documents propis, traçabilitat i actualització editant el corpus, sense reentrenar el model.

Límits:

- Si es recuperen fragments equivocats, la resposta es fonamentarà en context equivocat.
- Una similitud alta no garantix que el fragment continga la resposta.
- La qualitat depén de com s'ha fragmentat i preparat el corpus.
- Si el document no tracta el tema, no hi ha res que recuperar; el sistema ha de poder reconéixer-ho.

Variant més simple: una **consulta documental extractiva** mostra directament els fragments recuperats, sense generació. És convenient declarar quina de les dues s'implementa.

## 5. Comparació

| Aspecte | Basat en regles | Expert | LLM sol | RAG |
|---|---|---|---|---|
| Entrada ideal | Dades o patrons previsibles | Fets estructurats | Text lliure | Text lliure sobre documents |
| Aprén de dades | No | No | Sí, en l'entrenament | No ho fa el RAG; depén del model i del corpus |
| Determinisme | Alt | Alt | Baix o mitjà | Baix o mitjà |
| Explicació | Condició aplicada | Cadena de regles | Limitada | Fonts citades, amb justificació parcial |
| Actualització | Editar codi o regles | Editar la base de regles | Canviar o reentrenar el model, o afegir context | Actualitzar el corpus |
| Risc principal | Casos no previstos | Mantenir moltes regles | Respostes inventades | Recuperar context inadequat |
| Cost principal | Escriure regles | Modelar coneixement | Ús del model | Preparar i mantindre el corpus |

## 6. Aplicació al Helpdesk

Cap tècnica és adequada per a tot:

- **Prioritat, bloqueig i derivació:** regles o sistema expert, perquè han de ser estables i justificables.
- **Departament d'un ticket:** regles com a baseline i classificació supervisada per a comparar, perquè el text varia.
- **Explicar un procediment intern:** RAG, perquè la resposta depén de documents.
- **Redactar la resposta amb bon llenguatge:** LLM, sempre amb context recuperat i control de falta d'informació.
- **Una dada que no és en cap document:** el sistema ha de reconéixer-ho i derivar, no inventar.

Un disseny habitual combina les peces: regles per a decidir la via, RAG per a buscar la documentació, LLM per a redactar i controls per a aturar-se quan falta evidència.

## 7. Mini pràctica

Indica quin enfocament usaries per a cada consulta i justifica-ho:

1. "Què faig si el compte queda bloquejat després de 5 intents fallits?"
2. "Com configure l'IMAP al mòbil?"
3. "Quant costarà ampliar el servidor l'any que ve?"
4. "Reescriu esta resposta amb un to més amable."
5. "Assigna prioritat alta si el ticket indica que no es pot accedir al portal."

Orientació:
1. Regla o document, segons si la norma és una condició fixa o està descrita en un procediment.
2. RAG, si hi ha un procediment documentat; si no, derivació.
3. Cap dels enfocaments per si sol: requerix dades i projecció externes.
4. LLM, sense necessitat de recuperació.
5. Regla.

## 8. Idees per a recordar

- Regles: el coneixement està en condicions escrites.
- Sistema expert: regles organitzades, encadenades i explicables.
- LLM: capacitat de llenguatge, no font fiable de dades de l'empresa.
- RAG: LLM més documents recuperats, amb fonts i límits.
- El bon criteri consisteix a saber quan una resposta és una regla, quan és un document i quan no hi ha prou informació.
