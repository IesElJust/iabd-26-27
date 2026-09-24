# Site de l’alumnat · Zensical

El punt d’entrada és **DOCUMENT_DE_TREBALL.md**. El site presenta el seu contingut com a portada, amb el mapa setmanal i els enllaços als materials. La navegació dona accés a descàrregues, materials pràctics, píndoles breus i píndoles ampliades.

## Editar i previsualitzar

Des de la carpeta `ALUMNAT`, crea una vegada l’entorn i instal·la Zensical:

```bash
python3 -m venv .venv-site
source .venv-site/bin/activate
python -m pip install -r requirements-site.txt
```

Per construir i obrir un servidor local:

```bash
python site_projecte.py serve
```

Obri `http://127.0.0.1:8000/`. Per aturar-lo, prem Ctrl+C. Este servidor mostra la versió construïda i comprovada; després de modificar un material, atura’l i torna a executar el comandament perquè es reconstruïsca. No és una previsualització amb actualització automàtica.

Per generar només els fitxers publicables:

```bash
python site_projecte.py build
```

El resultat està en `site/`. El procés construïx amb Zensical en mode estricte i comprova els enllaços locals, les àncores i les descàrregues. No requerix les biblioteques de modelatge ni executa els notebooks o els exemples de les píndoles.

## Una única font de contingut

Edita el document de treball i els materials en les carpetes actuals. **No edites `web_docs/` ni `site/`**: es regeneren. `web_docs/index.md` és una còpia automàtica del document de treball amb accessos a les descàrregues i les píndoles ampliades.

El procés incorpora només `DOCUMENT_DE_TREBALL.md`, `MATERIALS_PRACTICS`, `PINDOLES` i `PINDOLES_AMPLIADES`, amb una llista explícita de formats admesos. Els resultats d’execucions, els entorns i els fitxers de configuració de la biblioteca antiga no es publiquen. El professorat queda fora del site.

La configuració de navegació, idioma, URL i presentació està en `zensical.toml`. Els estils addicionals estan en `web_assets/projecte.css`. La configuració MkDocs de les píndoles ampliades es conserva per a l’ús independent, però el site conjunt es construïx amb Zensical.

## Descàrregues

Els enllaços Markdown locals a `.csv`, `.ipynb` i `.py` reben automàticament l’atribut HTML `download` en la còpia web. Així descarreguen el fitxer original des del mateix domini de GitHub Pages. No apunten a `github.com/.../blob/` ni depenen de JavaScript. La preferència de carpeta o el diàleg de desament depén del navegador.

La pàgina **Descàrregues** enumera tots els fitxers d’estos tipus i oferix un ZIP amb els materials pràctics. El ZIP conserva l’estructura `MATERIALS_PRACTICS/notebooks` i `MATERIALS_PRACTICS/dades`, necessària per a les rutes relatives dels notebooks.

Es comprova que cada fitxer publicat és idèntic al de la còpia de construcció. Si afegixes enllaços amb una sintaxi diferent dels enllaços Markdown habituals, la comprovació detectarà que falta l’atribut de descàrrega i impedirà publicar una construcció incompleta.

## GitHub Pages

El remot detectat a l’inici de la preparació era `https://github.com/IesElJust/iabd-26-27.git`. La configuració preveu l’adreça:

`https://ieseljust.github.io/iabd-26-27/`

La carpeta `ALUMNAT` és l’arrel del repositori. El workflow està en `.github/workflows/pages.yml` dins d’esta carpeta; `DOCUMENT_DE_TREBALL.md`, `zensical.toml` i `site_projecte.py` queden al primer nivell. Les rutes del workflow són relatives a esta arrel. El workflow construïx i comprova el site en les propostes de canvi; publica els canvis de `main` i permet una execució manual des d’Actions.

Per activar la publicació:

1. En el repositori de GitHub, entra en **Settings → Pages** i selecciona **GitHub Actions** com a origen.
2. Incorpora al repositori el contingut d’ALUMNAT, inclosa la carpeta oculta `.github`, sense afegir una carpeta ALUMNAT exterior. No puges `site/`, `web_docs/` ni els entorns virtuals.
3. Envia els canvis a `main` i comprova el resultat de **Site de l’alumnat · Zensical** en Actions.
4. Obri l’URL que mostre el desplegament i prova una descàrrega de cada tipus.

La preparació local no activa Pages ni envia canvis a GitHub. Si canvia el repositori o s’usa un domini propi, actualitza `site_url` abans de publicar.

Referència: [publicació amb GitHub Actions en la documentació oficial de Zensical](https://zensical.org/docs/publish-your-site/).

