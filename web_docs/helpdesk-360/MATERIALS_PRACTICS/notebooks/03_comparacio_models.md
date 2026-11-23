# Compara regles i un model supervisat

**Objectiu:** comparar els dos enfocaments sobre els mateixos tickets de prova.

1. Revisa les etiquetes i crea `tickets_revisats.csv` en `../dades/`, conservant els identificadors i un registre dels canvis.
2. Agrupa duplicats i quasi duplicats abans de separar entrenament i prova. Reserva grups complets per a prova i comprova la representació de categories en cada partició. Guarda els IDs de cada partició.
3. Ajusta les regles només amb entrenament. No les revises després de mirar la prova final.
4. Entrena un `Pipeline` de `TfidfVectorizer` i `LogisticRegression` amb `text_ticket` com a entrada i `departament_sospitat` com a objectiu. Ajusta el vectoritzador exclusivament amb entrenament.
5. Aplica regles i model als mateixos IDs reservats. Calcula accuracy, F1 macro i matriu de confusió; mostra el suport de cada classe. Explica què fas amb `sense_regla`.
6. Analitza almenys tres errors o casos ambigus i explica quin enfocament triaries per al pilot.

| Enfocament | IDs de prova | Accuracy | F1 macro | Casos sense resposta | Limitacions |
|---|---|---:|---:|---:|---|
| Regles | | | | | |
| TF-IDF + regressió logística | | | | | |

Si no hi ha prou grups per a una separació útil, explica-ho i acorda amb el professorat ampliar les dades o una validació per grups. No presentes dades inventades com a tickets reals ni percentatges sobre molt pocs casos com a garantia de producció.

**Evidència:** notebook propi executable, particions, taula i conclusió. [Consulta la validació](../../PINDOLES/validacio-de-models.md).
