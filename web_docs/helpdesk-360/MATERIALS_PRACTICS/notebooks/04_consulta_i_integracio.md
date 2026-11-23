# Construïx la consulta documental i integra-la

**Objectiu:** obtindre una resposta amb font o una derivació explícita.

1. Prepara el corpus amb els tres procediments d'[empresa](../empresa/02_politica_contrasenyes.md): contrasenyes, VPN i correu. El briefing descriu el negoci; no és un procediment de suport.
2. Assigna a cada document un ID, un títol i una versió de treball. Conserva els passos complets en dividir-lo; guarda ID de fragment, document i text.
3. Crea una primera recuperació amb TF-IDF i similitud cosinus. Prova preguntes amb vocabulari diferent i inspecciona els fragments recuperats. Esta és una cerca lèxica, no embeddings semàntics.
4. Defineix quan falta context. Ajusta el criteri amb preguntes de desenvolupament i reserva preguntes noves per a la prova final. Una similitud alta no demostra que el fragment continga la resposta.
5. Mostra una primera resposta extractiva amb la font. Si afegixes un generador, passa-li només els fragments pertinents i instruïx-lo perquè cite la font i derive quan falte informació. Identifica clarament si has construït consulta documental extractiva o RAG amb generació.
6. Exposa el classificador i la consulta amb una API o interfície. Valida entrada buida, longitud excessiva, errors del model i falta de context. No registres secrets ni dades personals innecessàries.
7. Prova una instrucció maliciosa dins d'un document: el seu text s'ha de tractar com a dada, sense canviar les instruccions del sistema.

Contracte mínim orientatiu:

```json
{"pregunta": "Què faig si la VPN dona error de certificat?"}
```

```json
{"estat": "amb_context", "resposta": "...", "fonts": [{"document_id": "vpn", "fragment_id": "vpn-01"}]}
```

Una derivació ha d'incloure motiu, resposta prudent i `fonts` buida quan no hi haja font pertinent. La categoria d'un ticket no determina per si sola la resposta documental.

**Evidència:** corpus amb metadades, preguntes de desenvolupament, casos reservats, registre de fragments recuperats i demo. [RAG](../../PINDOLES/rag-i-embeddings.md) · [API](../../PINDOLES/apis-rest.md) · [Guardrails](../../PINDOLES/prompt-engineering-i-guardrails.md).
