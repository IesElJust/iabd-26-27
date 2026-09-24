---
title: "MLflow: experiments traçables i comparables"
description: "Fonaments, exemples reproduïbles i pràctica progressiva: mlflow: experiments traçables i comparables."
tags: [IABD, dades, formació]
icon: material/book-open-page-variant
status: ampliada
---

# 11 · MLflow: experiments traçables i comparables

[← Índex de les píndoles](../index.md)

!!! abstract "Què aprendràs"
    - Registrar decisions, mètriques i artefactes per execució.
    - Comparar runs amb dades i particions compatibles.
    - Distingir registre, persistència i desplegament.

**Coneixements previs:** Entrenament, validació, entorn Python i fitxers locals.

**Dedicació orientativa:** 3–4 h per a lectura i laboratori guiat; les extensions i els exercicis autònoms requerixen temps addicional.

!!! tip "Dos recorreguts possibles"
    **Essencial:** llig els fonaments, executa el laboratori i completa la pràctica inicial. **Aprofundiment:** continua amb les pràctiques intermèdia i avançada i els exercicis. El professorat pot seleccionar-les segons els coneixements previs; no són totes obligatòries dins del projecte.

## Mapa de la unitat

De «em va eixir millor» a una comparació verificable → Què cal registrar? → Metadades i artefactes no són el mateix → Un cicle mínim d’experimentació → Comparar sense canviar la pregunta → Guardar i recuperar un model → Consultar el registre → Lectura del laboratori

## 1. De «em va eixir millor» a una comparació verificable

Durant un experiment canviem variables, particions, models i paràmetres. Si només conservem l’última cel·la del notebook, resulta difícil reconstruir què produïa cada resultat. Un registre d’experiments associa decisions, mètriques i fitxers a una execució identificable.

MLflow oferix ferramentes per registrar i consultar este historial. No decidix si una partició és correcta, si hi ha fuga d’informació o si una mètrica respon al problema. Automatitza part del registre; la qualitat del disseny continua sent responsabilitat nostra.

La unitat bàsica és el *run*, una execució amb identificador, estat, paràmetres, mètriques, etiquetes i artefactes. Un experiment agrupa runs relacionats. Convé que tinguen una pregunta compartida, com comparar intensitats de regularització sota una mateixa partició.

## 2. Què cal registrar?

| Element | Exemple | Per què és útil |
|---|---|---|
| Paràmetre | `alpha=0.1` | Descriu una decisió d’ajust |
| Mètrica | `mae_valid=0.40` | Quantifica un resultat i el conjunt on s’ha mesurat |
| Etiqueta | `split=100/50 iid sintetiques` | Afig context llegible |
| Artefacte | Informe, figura o model | Conserva una eixida de l’execució |
| Identificador | ID del run | Permet recuperar exactament l’execució |

Distingix mètriques d’entrenament, validació i prova en els noms. Una columna anomenada només `error` pot barrejar resultats que no són comparables. Registra també unitats i sentit: MAE més baix és millor, mentre que altres puntuacions s’interpreten al contrari.

Una llavor facilita repetir components aleatoris, però no assegura identitat completa entre maquinari, versions o algorismes. Conserva versions de dependències, transformacions i criteris de partició. Si uses control de versions, associa també la revisió del codi.

## 3. Metadades i artefactes no són el mateix

El laboratori usa una base SQLite local per a metadades i un directori local per a artefactes. La base conserva la informació del registre; els fitxers grans, com un model, es guarden al directori d’artefactes. Copiar només la base pot deixar referències a fitxers absents.

L’adreça de seguiment o *tracking URI* indica on es registren les execucions. En l’exemple es construïx una ruta absoluta a `codi/eixides/mlflow.db`, de manera que canviar el directori des del qual executem el programa no cree registres en llocs inesperats.

Esta configuració és per a un laboratori local. Un equip que compartix experiments necessita planificar emmagatzematge, permisos i accés. No cal desplegar un servidor compartit per aprendre els conceptes ni per completar esta pràctica.

## 4. Un cicle mínim d’experimentació

El procés és: preparar dades i partició, ajustar una alternativa, obrir un run, registrar decisions i resultats, guardar els artefactes i tancar el run. Un gestor de context ajuda a tancar l’execució amb l’estat corresponent si hi ha una excepció.

```python title="Estructura del registre, amb una mètrica de demostració"
from pathlib import Path
import mlflow

base = Path("registre_demo").resolve()
base.mkdir(exist_ok=True)
mlflow.set_tracking_uri("sqlite:///" + str(base/"registre.db"))
mlflow.set_experiment("exemple-de-registre")
with mlflow.start_run(run_name="primera-prova"):
    mlflow.log_param("alpha", 1.0)
    mlflow.log_metric("mae_valid_demo", 2.5)
    mlflow.set_tag("origen", "valor il·lustratiu, no calculat")
```

El valor 2,5 d’este fragment és deliberadament il·lustratiu. El laboratori complet calcula les mètriques a partir de prediccions, que és el que s’ha de fer en un experiment real. Mai registres una xifra manual com si fora una avaluació automàtica.

## 5. Comparar sense canviar la pregunta

Dos runs són comparables si avaluen el mateix objectiu, amb la mateixa definició de mètrica i un disseny de validació compatible. Si un usa files aleatòries i l’altre mesos futurs, una diferència de MAE no es pot atribuir només al model.

La versió de dades també importa. El laboratori calcula una empremta SHA-256 dels arrays utilitzats. Això ajuda a detectar canvis en eixa representació concreta, però no substituïx la descripció de les dades, la seua procedència ni una còpia recuperable.

En dades reals, registra el fitxer o versió d’origen i les transformacions. No necessites pujar dades personals als artefactes per fer un bon registre; un resum, un identificador de versió i controls agregats poden ser suficients segons el context.

La selecció es fa amb validació. Consultar repetidament el resultat de prova per triar el millor run convertix eixe conjunt en una altra validació. El laboratori compara dues alternatives i no inclou una prova final: no s’ha de presentar com una estimació definitiva de generalització.

## 6. Guardar i recuperar un model

Guardar un model permet reutilitzar el resultat ajustat. Quan hi ha preprocessament, convé guardar el pipeline complet perquè imputació, codificació i model viatgen junts. Guardar només l’estimador final pot produir entrades incompatibles després.

L’exemple registra un model scikit-learn amb una mostra d’entrada. La signatura ajuda a descriure l’esquema esperat; no comprova que la distribució o el significat de les variables continuen sent adequats.

La recuperació utilitza una URI del model que retorna MLflow o que apareix en la informació registrada. Després de carregar-lo, compara les prediccions d’un mateix lot amb les de l’objecte original. La igualtat dins d’una tolerància és una comprovació útil de persistència.

No confundisques registre amb desplegament. Un model guardat encara necessita un procés d’ús, controls d’entrada i seguiment si s’incorpora a un servei. Esta píndola acaba en experimentació i recuperació local.

## 7. Consultar el registre

Es poden consultar runs des de Python amb `mlflow.search_runs`. Filtra execucions acabades i mostra les columnes que expliquen la comparació. Ordenar una mètrica només té sentit després de comprovar que els candidats són comparables.

La interfície web és una ajuda opcional. Des del directori de la píndola, amb l’entorn activat, es pot iniciar així:

```bash title="Interfície local opcional"
mlflow ui --backend-store-uri sqlite:///codi/eixides/mlflow.db --host 127.0.0.1 --port 5000
```

Obri l’adreça local que indique la terminal. La ruta relativa d’este comandament pressuposa que estàs dins de la píndola; el programa Python imprimix també la URI absoluta per poder comprovar que tots dos apunten a la mateixa base. Atura la interfície quan acabes.

## 8. Lectura del laboratori

El programa genera 150 observacions sintètiques independents, reserva 100 per a entrenament i 50 per a validació i compara Ridge amb `alpha=0.1` i `alpha=10`. Manté dades i partició constants.

Cada execució completa del programa crea dos runs nous. Tornar-lo a executar no substituïx els anteriors: l’historial creix. La comprovació final verifica que els dos identificadors acabats de generar apareixen amb estat `FINISHED`.

En l’entorn de comprovació, els MAE han sigut aproximadament 0,401 i 0,555. Estes xifres són una referència del laboratori, no una regla que diga que una regularització baixa sempre és millor. Canviar dades o partició pot canviar la comparació.

## Laboratori complet i reproduïble

**Context:** treballarem amb dades sintètiques creades pel mateix programa. No cal descarregar datasets ni usar els CSV de BiciTierra. Els valors servixen per aprendre i comprovar procediments; no descriuen una població real.

**Materials:** Python 3.10 o superior, un entorn virtual i els [requisits de la unitat](requirements.txt). Consulta la [preparació comuna](../index.md) abans d’instal·lar-los.

Des de la carpeta d’esta píndola, amb l’entorn activat:

```bash
python -m pip install -r requirements.txt
python codi/exemple.py
```

El programa crea `codi/eixides/`. Pots examinar les eixides sense modificar el codi original. Per resoldre les variants, treballa sobre una còpia i actualitza les comprovacions quan canvies deliberadament les dades.

### Exemple comentat

[Obri o descarrega el programa complet](codi/exemple.py). Cada comprovació `assert` expressa una propietat esperada de les dades de demostració; si falla, investiga la causa abans d’eliminar-la.

```python title="codi/exemple.py" linenums="1"
"""Registre local d'experiments amb SQLite, sense servidor extern."""
from pathlib import Path
import hashlib, json, sys
import numpy as np
import mlflow
import mlflow.sklearn
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_absolute_error

def main():
    out = Path(__file__).resolve().parent / 'eixides'
    out.mkdir(exist_ok=True)
    # La base local guarda metadades; els artefactes van a una altra carpeta.
    mlflow.set_tracking_uri('sqlite:///' + str(out / 'mlflow.db'))
    experiment = 'energia-docent'
    if mlflow.get_experiment_by_name(experiment) is None:
        mlflow.create_experiment(experiment, artifact_location=(out / 'artifacts').as_uri())
    mlflow.set_experiment(experiment)
    rng = np.random.default_rng(42)
    X = rng.normal(size=(150, 2))
    y = 10 + 3 * X[:, 0] - 2 * X[:, 1] + rng.normal(0, 0.5, 150)
    (train, valid) = (X[:100], X[100:])
    (yt, yv) = (y[:100], y[100:])
    # Empremta de la representació concreta usada en este experiment.
    fingerprint = hashlib.sha256(X.tobytes() + y.tobytes()).hexdigest()
    run_ids = []
    # Comparem paràmetres mantenint dades i partició constants.
    for alpha in [0.1, 10.0]:
        model = Ridge(alpha=alpha).fit(train, yt)
        with mlflow.start_run(run_name=f'ridge-alpha-{alpha}') as run:
            mlflow.log_params({'alpha': alpha, 'seed': 42, 'train_rows': 100, 'valid_rows': 50})
            mlflow.set_tags({'data_sha256': fingerprint, 'split': '100/50 iid sintetiques', 'python': sys.version.split()[0]})
            mlflow.log_metric('mae_valid', mean_absolute_error(yv, model.predict(valid)))
            mlflow.log_text('Dades sintètiques; comparació en validació, sense test final en esta demo.', 'decisions.txt')
            mlflow.sklearn.log_model(model, name='model', input_example=train[:2])
            run_ids.append(run.info.run_id)
    # Comprovem que les execucions han acabat i es poden recuperar.
    runs = mlflow.search_runs(experiment_names=[experiment], filter_string="attributes.status = 'FINISHED'")
    assert set(run_ids).issubset(set(runs.run_id))
    print(runs[['run_id', 'params.alpha', 'metrics.mae_valid']].head().to_string(index=False))
    (out / 'execucio.json').write_text(json.dumps({'run_ids': run_ids, 'data_sha256': fingerprint}, indent=2))
    print('Tracking URI:', mlflow.get_tracking_uri())
if __name__ == '__main__':
    main()
```

## Pràctiques guiades

Cada pràctica deixa una evidència petita: una eixida comprovada i una explicació de la decisió. Els temps són orientatius i no inclouen instal·lació.

### Pràctica 1 · Localitzar dos experiments comparables

**Nivell i temps:** Inicial · 20–30 min.

**Objectiu:** Relacionar run, paràmetre, mètrica i artefacte.

**Materials:** exemple comentat d’esta unitat, les seues eixides i una còpia de treball per a les modificacions.

**Procediment:**

1. Executa el programa i guarda els dos identificadors impresos o registrats en `execucio.json`.
2. Localitza la base SQLite i el directori d’artefactes generats.
3. Consulta els runs acabats i compara els valors d’alpha i MAE de validació.
4. Explica quins elements es mantenen constants entre les dues alternatives.

!!! success "Comprovació i evidència esperada"
    Els dos runs figuren com FINISHED, compartixen empremta de dades i partició, i tenen alpha diferent.

**Preguntes de reflexió:**

- Quina diferència hi ha entre experiment i run?
- Per què la mètrica es diu `mae_valid`?
- Què perdríem si només conservàrem una captura de pantalla?

**Ampliació opcional:** Obri la interfície local opcional apuntant a la mateixa base i comprova els identificadors.

### Pràctica 2 · Fer una comparació traçable

**Nivell i temps:** Intermèdia · 30–45 min.

**Objectiu:** Afegir una alternativa sense canviar silenciosament dades o criteris.

**Materials:** exemple comentat d’esta unitat, les seues eixides i una còpia de treball per a les modificacions.

**Procediment:**

1. Afig alpha 1 a la llista de candidats en una còpia del programa.
2. Registra una etiqueta amb una justificació breu de la comparació.
3. Executa i filtra els tres identificadors d’esta execució, evitant barrejar-los amb anteriors.
4. Ordena per MAE de validació i escriu una decisió provisional amb límits.

!!! success "Comprovació i evidència esperada"
    La comparació inclou tres runs de la mateixa execució; no es presenta el resultat com a prova final.

**Preguntes de reflexió:**

- Per què repetir el programa crea nous runs?
- Com distingiries una millora de model d’un canvi en les dades?
- Quin problema hi ha a triar segons el millor resultat de prova de molts runs?

**Ampliació opcional:** Afig duració d’entrenament i valora si una millora petita compensa el cost addicional.

### Pràctica 3 · Recuperar i comprovar

**Nivell i temps:** Avançada · 45–60 min.

**Objectiu:** Verificar que un model guardat conserva el comportament esperat.

**Materials:** exemple comentat d’esta unitat, les seues eixides i una còpia de treball per a les modificacions.

**Procediment:**

1. Modifica la còpia perquè conserve l’objecte retornat per `mlflow.sklearn.log_model`.
2. Usa la seua `model_uri` amb `mlflow.sklearn.load_model`.
3. Compara les prediccions del model original i del recuperat sobre el mateix lot amb `numpy.allclose`.
4. Documenta què cal conservar per moure l’experiment a un altre ordinador: dades o versió, codi, entorn, metadades i artefactes.

!!! success "Comprovació i evidència esperada"
    La comprovació de prediccions passa; l’informe no confon el fitxer del model amb un servei desplegat.

**Preguntes de reflexió:**

- Per què cal guardar el preprocessament quan existix?
- Quina garantia aporta una signatura i quina no?
- Per què copiar només SQLite pot ser insuficient?

**Ampliació opcional:** Registra un pipeline amb estandardització i Ridge i repetix la comprovació de recuperació.

## Exercicis autònoms

Intenta resoldre cada repte abans de desplegar l’orientació. Es valora el raonament i les comprovacions, no només obtindre una xifra.

### Repte 1 · Mètriques incomparables

Dos runs tenen MAE 4 i 3 però usen particions diferents. Es pot declarar guanyador?

??? example "Solució orientativa i criteri de revisió"
    No atribuesques la diferència només al model. Repeteix amb un disseny comparable o descriu explícitament que responen preguntes diferents.

### Repte 2 · Empremta de dades

Explica què permet i què no permet recuperar un hash de les dades.

??? example "Solució orientativa i criteri de revisió"
    Permet contrastar identitat de la representació usada amb una altra còpia. No reconstruïx les dades ni explica la seua procedència, qualitat o permisos d’ús.

### Repte 3 · Persistència completa

Fes una llista mínima per recuperar un pipeline i verificar-ne la predicció mesos després.

??? example "Solució orientativa i criteri de revisió"
    Model i preprocessament, esquema d’entrada, versions, codi, dades o versió recuperable, partició i un lot de comprovació. L’ID del run ajuda a trobar-ho però no substituïx els artefactes.

## Errors habituals i diagnòstic

| Símptoma | Causa que convé investigar | Comprovació o correcció |
|---|---|---|
| Interfície sense runs | Apunta a una altra base de seguiment. | Compara la URI absoluta del programa amb la de la interfície. |
| Model registrat però no recuperable | Artefactes absents o rutes canviades. | Conserva artefactes junt amb metadades i comprova la URI retornada. |
| Guanyador aparent entre runs diferents | Canvis de dades, partició o mètrica. | Filtra candidats comparables i registra el context. |

## Autoavaluació i evidències

Abans de donar la unitat per treballada, comprova estos punts i escriu una frase d’evidència per a cadascun:

- [ ] Puc registrar decisions, mètriques i artefactes per execució.
- [ ] Puc comparar runs amb dades i particions compatibles.
- [ ] Puc distingir registre, persistència i desplegament.
- [ ] He executat el laboratori i he contrastat almenys un resultat independentment.
- [ ] Puc explicar una limitació i un cas en què el procediment requeriria canvis.

**Lliurable de la píndola:** còpia de treball reproduïble, resultats de la pràctica seleccionada i un text breu que indique pregunta, decisió, comprovació i limitació. Si s’usa dins de BiciTierra Market, integra esta evidència en el lliurable setmanal corresponent; no cal crear una entrega duplicada.

## Fonts per aprofundir

- [Documentació oficial de referència](https://mlflow.org/docs/latest/ml/tracking/). Consulta especialment els conceptes i els supòsits descrits en la unitat.
- [Inici amb MLflow](https://mlflow.org/docs/latest/ml/getting-started/quickstart/).

Les versions executades i els límits de la comprovació estan en el [registre de validació](../VALIDACIO.md). Els exemples són originals i les dades són sintètiques.

## Aplicació final a BiciTierra Market

**Moment orientatiu:** setmana 3–6, ampliació. Esta correspondència ajuda a triar materials i no substituïx el document de treball de l’alumnat.

És una ampliació opcional per registrar els models de vendes. Mantín constants els talls temporals quan compares runs i etiqueta la versió de dades. Si l’equip encara està aprenent pipelines i validació, una taula d’experiments ben documentada pot ser el primer pas abans d’automatitzar-la.

**Transferència:** identifica quin concepte acabes de practicar, quina dada del projecte l’exigix i què has de canviar respecte del laboratori. Justifica eixa adaptació abans de copiar codi.
