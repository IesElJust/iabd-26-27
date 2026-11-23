# Notebooks i pràctiques

Executeu Jupyter des d'esta carpeta perquè `../dades/` siga accessible. Descarregueu el ZIP complet del site i conserveu l'estructura.

1. Setmana 2: [exploració](01_exploracio_tickets.ipynb).
2. Setmana 3: [baseline per regles](02_classificacio_baseline.ipynb) i [comparació supervisada](03_comparacio_models.md).
3. Setmana 4: [consulta documental i integració](04_consulta_i_integracio.md).

Els dos notebooks són punts de partida, no una solució completa. El segon calcula encerts sobre el conjunt carregat: eixe recompte descriu les regles i no és una validació independent.

Entorn de treball:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install pandas scikit-learn jupyter
jupyter notebook
```

Si trieu una interfície o un model generatiu, documenteu també les dependències i el servei triat. No cal cap compte de pagament per explorar les dades i construir la recuperació inicial.
