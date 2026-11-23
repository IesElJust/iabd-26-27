---
title: Prompt Engineering I Guardrails
---

# Prompt Engineering I Guardrails

## Idea clau

Treballar amb `LLMs` no és només "fer una pregunta". El resultat depén molt de:

- què demanem
- amb quin context
- amb quines restriccions
- i què impedim que faça el model

Per a algú que comença, la idea més important és esta: un `LLM` no "sap exactament què vols" només perquè la teua intenció et sembla evident.

El model respon al text que rep. Si eixe text és ambigu, la resposta també pot ser-ho. Si el context és pobre, la resposta pot sonar bé i estar malament.

## Què és un bon prompt

Un bon prompt sol deixar clar:

- quin rol té el sistema
- quina tasca ha de fer
- quin context pot usar
- quin format de resposta volem
- quins límits ha de respectar

Dit més fàcil:

- qui ha de ser
- què ha de fer
- amb quina informació
- com ho ha de tornar
- què no ha de fer

## Exemple simple

Prompt pobre:

`Respon a este ticket.`

Prompt millor:

`Eres un assistent intern de suport. Usa només el context recuperat. Si no hi ha prou informació, indica-ho. Respon en 3 frases com a màxim i no inventes passos no presents al corpus.`

## Per què importen els guardrails

Els `guardrails` són regles que limiten el comportament del model.

Exemples:

- no respondre sense context suficient
- no donar dades sensibles
- no executar accions no autoritzades
- usar un format de resposta controlat

## Què sol fallar en un prompt fluix

Si el prompt és massa vague, el model pot:

- respondre massa llarg
- barrejar informació certa i inventada
- ignorar el format que necessitem
- actuar com si tinguera context que realment no té

Per això no n'hi ha prou amb dir "contesta". Cal especificar amb quina informació pot treballar i què ha de fer si no arriba a una resposta fiable.

## Exemple guiat de classe

Situació:

en `Helpdesk`, volem que l'assistent responga sobre la VPN a partir de fragments recuperats del corpus.

Prompt massa obert:

`Contesta la pregunta del client sobre la VPN.`

Problemes:

- no diu quin rol té el sistema
- no limita les fonts
- no explica què fer si falta context
- no fixa format de resposta

Versió més útil:

`Eres un assistent intern de suport. Usa només els fragments recuperats del manual de VPN. Si no hi ha prou informació, indica-ho clarament. Respon en un màxim de 3 frases i no inventes passos nous.`

Conclusió docent:

el bon prompt no és el més llarg, sinó el que deixa clara la tasca, el context i el límit.

## Patró pràctic que podeu reutilitzar

1. rol: qui és el sistema
2. tasca: què ha de fer exactament
3. context: quina informació pot usar
4. format: com ha d'eixir la resposta
5. límit: què ha de fer si no pot respondre bé

## Exemple encara més bàsic

Pregunta de l'usuari:

`No puc entrar a la VPN, què faig?`

Si el sistema només rep eixa pregunta, pot improvisar passos genèrics.

Si el sistema rep a més:

- fragments del manual de VPN
- instrucció de no inventar passos
- obligació d'indicar falta de context

aleshores la resposta és molt més controlable.

La lliçó important és que el bon resultat no depén només del model, sinó també de com preparem la tasca.

## Error habitual

Pensar que el model ja "entendrà" què volem sense especificar límits ni format.

## Mini pràctica

Pregunta:

Com milloraries este prompt?

`Contesta la pregunta del client sobre la VPN.`

## Solució orientativa

Una millora possible seria:

`Eres un assistent de suport. Usa només els fragments recuperats del manual de VPN. Si la informació no és suficient, indica que no hi ha prou context. Dona una resposta curta, clara i sense inventar passos addicionals.`

## Resum final

El `prompt engineering` no és un truc màgic. És una forma de convertir una tasca ambigua en una instrucció operativa més controlada.

## Com portar-ho a aula

- P1: usar-lo per comparar una resposta sense control amb una resposta amb context i guardrails
- P5: usar-lo quan hi haja capa `RAG` o assistència executiva
- criteri docent: si l'alumnat no especifica què ha de passar sense context suficient, encara no està controlant el sistema

## Criteri docent ampliat

Si l'alumnat diu "el model ha fallat" però no sap explicar quin prompt, quin context i quin límit s'havien definit, encara no està treballant el problema amb prou precisió.
