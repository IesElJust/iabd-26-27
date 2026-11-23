---
title: Píndoles ampliades · IABD
description: Biblioteca de fonaments, laboratoris i activitats progressives per al projecte 2 i altres contextos.
icon: material/bookshelf
---

# Píndoles ampliades · IABD

Esta biblioteca conté onze píndoles amb teoria, exemples comentats, pràctiques graduades, comprovacions i activitats autònomes. Treballarem amb casos de sensors, aigua, energia, incidències i biblioteques. L’aplicació a BiciTierra Market apareix al final de cada unitat.

Les píndoles breus oferixen una consulta ràpida; les ampliades desenvolupen els conceptes i les activitats. El document de treball indica què necessites en cada setmana.

## Accés per a l’alumnat

1. Localitza el tema que necessites en la taula.
2. Comprova els coneixements previs i llig els fonaments.
3. Executa el laboratori i completa la pràctica que indique el professorat.
4. Usa els reptes i les solucions orientatives per comprovar comprensió.
5. Torna a l’últim apartat per adaptar el que has aprés al projecte.

No és necessari instal·lar totes les eines ni fer totes les pràctiques. El recorregut essencial és lectura, laboratori i pràctica inicial; les altres activitats permeten aprofundir o atendre diferents ritmes.

## Accés per al professorat

Cada unitat inclou objectius, prerequisits, temps orientatius, tres pràctiques amb evidència esperada, preguntes de reflexió i ampliacions, tres reptes amb solució orientativa i errors habituals. Les solucions estan en el mateix material per facilitar autoavaluació; no són un solucionari reservat ni una proposta d’examen.

Selecciona activitats segons les necessitats del grup. La suma de totes les extensions excedix el temps ordinari de sis setmanes. MLflow és una ampliació opcional. Per valorar el treball, demana que l’alumnat explique la pregunta, justifique la decisió, comprove el resultat i reconega una limitació.

## Catàleg i connexió amb les setmanes

La numeració ordena els temes, no les setmanes. Els moments d’ús són orientatius i s’han de llegir junt amb el document de treball del projecte.

| Píndola | Moment en BiciTierra Market | Laboratori general |
|---|---|---|
| [01 · Python i entorns de treball](python-i-entorns/index.md) | 1 | Validació de lectures d’un sensor |
| [02 · Jupyter: notebooks que es poden reproduir](jupyter-notebooks/index.md) | 1 | Consum d’aigua i execució des de zero |
| [03 · NumPy i pandas: de les dades a les taules](python-per-a-dades-i/index.md) | 1–2 | Incidències i catàleg de serveis |
| [04 · Exploració i qualitat de dades](eda-i-qualitat-de-dades/index.md) | 1–2 | Auditoria de sensors |
| [05 · Visualització amb Matplotlib i seaborn](visualitzacio-amb-matplotlib-i-seaborn/index.md) | 2, 4 i 6 | Consum energètic de tres edificis |
| [06 · Aprenentatge supervisat amb scikit-learn](scikit-learn-intro/index.md) | 3 | Regressió sobre habitatges sintètics |
| [07 · Validació: mesurar allò que realment volem predir](validacio-de-models/index.md) | 2, 3 i 5 | Backtesting mensual de dos edificis |
| [08 · Clustering i interpretació de perfils](clustering-i-segmentacio/index.md) | 4 | Perfils d’ús d’una biblioteca |
| [09 · Interpretabilitat: permutació, SHAP i LIME](xai-shap-lime/index.md) | 5 | Explicacions d’un model de consum |
| [10 · Dashboards i modelatge amb Power BI](dashboards-i-powerbi/index.md) | 6 | Indicadors d’un servei tècnic |
| [11 · MLflow: experiments traçables i comparables](mlflow-intro/index.md) | 3–6, ampliació | Comparació local de regressions |

## Preparació comuna

Els programes creen les seues pròpies dades i escriuen només dins de `codi/eixides/` de la píndola. No modifiquen els CSV de BiciTierra. Treballa sobre còpies quan resolgues variants.

Des de la carpeta `PINDOLES_AMPLIADES`, crea un entorn amb Python 3.10 o superior:

```bash title="GNU/Linux o macOS"
python3 -m venv .venv
source .venv/bin/activate
```

En Windows, amb PowerShell:

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
```

Si l’activació no està disponible en l’equip del centre, usa directament l’intèrpret de l’entorn (`.venv/bin/python` o `.venv\Scripts\python.exe`) o la configuració indicada pel professorat.

Després entra en la carpeta de la unitat que vulgues treballar i instal·la els seus requisits. Per exemple:

```bash
cd docs/python-per-a-dades-i
python -m pip install -r requirements.txt
python codi/exemple.py
```

La primera píndola usa només Python estàndard. Els requisits de cada tema eviten instal·lar SHAP o MLflow quan encara no es necessiten. Per a preparar un entorn de professorat amb totes les demostracions, hi ha també [requisits complets](requirements-complets.txt). Les versions s’han fixat segons la comprovació amb Python 3.10; consulta el [registre de validació](VALIDACIO.md).

La interfície de Jupyter és opcional: es pot instal·lar amb `python -m pip install "notebook>=7,<8"`. L’exemple de notebooks crea i executa el fitxer també sense obrir-la. Power BI Desktop és necessari per a construir i verificar el dashboard; Python genera els CSV i els totals de control.

## Com està organitzada cada carpeta?

Les onze unitats estan dins de `docs/`, una carpeta per tema. L’índex general i el registre de validació també estan dins de `docs/`.

- `index.md`: unitat completa de treball, incloent exemples i activitats.
- `codi/exemple.py`: demostració executable i comentada.
- `requirements.txt`: dependències de la unitat.
- `codi/eixides/`: resultats que apareixen quan executes el programa; no són dades d’entrada que hages de buscar.

La unitat de visualització inclou una figura ja generada. Les activitats no requerixen servicis en línia ni comptes externs, llevat de descarregar inicialment les dependències si no estan instal·lades.

## Lectura i presentació

Pots obrir els Markdown en un editor. Per mostrar desplegables, avisos, taules i diagrames amb el mateix estil de la biblioteca de referència, incloem una configuració de MkDocs Material:

```bash
python -m pip install -r docs/requirements-presentacio.txt
mkdocs serve
```

Executa estos comandaments des de `PINDOLES_AMPLIADES` i obri l’adreça local indicada. La presentació és opcional; els programes i els continguts es poden usar sense crear cap web. No hi ha publicació automàtica.
