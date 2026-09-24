---
title: "Interpretabilitat: permutació, SHAP i LIME"
description: "Fonaments, exemples reproduïbles i pràctica progressiva: interpretabilitat: permutació, shap i lime."
tags: [IABD, dades, formació]
icon: material/book-open-page-variant
status: ampliada
---

# 09 · Interpretabilitat: permutació, SHAP i LIME

[← Índex de les píndoles](../index.md)

!!! abstract "Què aprendràs"
    - Distingir explicacions globals i locals.
    - Reconstruir una predicció a partir de contribucions SHAP.
    - Comprovar la fidelitat i els supòsits d’una explicació LIME.

**Coneixements previs:** Model supervisat ja validat i distinció entre correlació i causalitat.

**Dedicació orientativa:** 4–5 h per a lectura i laboratori guiat; les extensions i els exercicis autònoms requerixen temps addicional.

!!! tip "Dos recorreguts possibles"
    **Essencial:** llig els fonaments, executa el laboratori i completa la pràctica inicial. **Aprofundiment:** continua amb les pràctiques intermèdia i avançada i els exercicis. El professorat pot seleccionar-les segons els coneixements previs; no són totes obligatòries dins del projecte.

## Mapa de la unitat

Què volem explicar? → Comença amb una referència interpretable → Importància per permutació → SHAP: referència i contribucions → LIME: aproximar un entorn → Explicacions globals, locals i contradictòries → Com redactar una interpretació defensable → Lectura del laboratori

## 1. Què volem explicar?

Un model pot produir una predicció útil sense que siga evident per què l’ha produïda. La interpretabilitat ajuda a examinar el seu comportament, detectar dependències inesperades i comunicar resultats. No convertix automàticament una associació en una causa ni garantix que el model siga just.

Abans de calcular una explicació, formula la pregunta. «Quines variables usa més el model en general?» és una pregunta global. «Per què esta observació rep este resultat?» és local. «Què passaria si canviàrem una condició en el món real?» és causal i exigix supòsits i evidència addicionals.

| Pregunta | Eina possible | Què no permet concloure per si sola |
|---|---|---|
| Quina informació ajuda a predir? | Importància per permutació | Que la variable siga la causa del resultat |
| Com es repartix una predicció? | SHAP | Que les contribucions siguen úniques fora dels supòsits triats |
| Com aproxima el model un entorn local? | LIME | Que l’aproximació siga fidel lluny del cas |
| Com canvia la resposta del model? | Dependència parcial o ICE | Que una intervenció real tinga el mateix efecte |

La primera explicació hauria de ser la del problema: població, resposta, variables disponibles i ús previst. Una figura sofisticada no substituïx esta informació.

## 2. Comença amb una referència interpretable

Una regla senzilla, una regressió lineal o un arbre poc profund poden servir de referència. En regressió, un coeficient descriu un canvi en la predicció quan varia una entrada mantenint les altres fixes, dins de la representació utilitzada. Si les variables estan estandarditzades, les unitats del coeficient canvien.

La col·linearitat pot fer inestables els coeficients. Una variable binària codificada i una numèrica escalada no s’han de comparar sense explicar-ne les unitats. Un arbre profund tampoc resulta fàcil de llegir només perquè siga un arbre.

Compara primer el rendiment i la complexitat. Si una regla senzilla satisfà l’objectiu, pot ser preferible a afegir una explicació aproximada sobre un model molt complex. Esta és una decisió que cal justificar amb dades i necessitats d’ús.

## 3. Importància per permutació

El procediment calcula una puntuació de referència, desordena una columna, torna a puntuar i mesura la pèrdua de rendiment. Repetir la permutació permet observar variabilitat. Cal fer-ho en un conjunt de validació adequat; una importància alta en entrenament pot reflectir memorització.

La importància depén del model, de les observacions i de la mètrica. Amb `neg_mean_absolute_error`, una pèrdua positiva de puntuació correspon a un augment de MAE quan desordenem la variable. No és un percentatge de causalitat.

Quan dos predictors contenen informació semblant, el model pot compensar la permutació d’un amb l’altre. La importància individual pot resultar baixa encara que el conjunt siga útil. En sèries temporals, una permutació de files també pot generar combinacions irreals; el disseny ha de respectar el context.

```python title="Una permutació que desfà una relació"
import numpy as np
x = np.array([1, 2, 3, 4, 5])
y = 2*x
barrejat = np.random.default_rng(42).permutation(x)
print("MAE original:", np.abs(y-2*x).mean())
print("MAE després de permutar:", np.abs(y-2*barrejat).mean())
```

Ací la regla `2*x` és coneguda. En un problema real, la importància avalua el model ajustat, no una llei del sistema.

## 4. SHAP: referència i contribucions

SHAP distribuïx la diferència entre una predicció i un valor de referència entre les variables. Per a l’explicació de regressió del laboratori, la comprovació és:

**predicció = valor base + suma de contribucions**.

Una contribució positiva augmenta la predicció respecte de la base; una negativa la reduïx. No significa «bona» o «roïna» per si mateixa. En classificació, la suma pot expressar-se en una escala distinta de probabilitat, segons el model i la configuració; s’ha d’identificar abans de comunicar-la.

El conjunt de fons determina contra quina població comparem. Usar habitatges menuts com a referència pot donar una lectura distinta d’usar una mostra representativa de tots els habitatges d’entrenament. Documenta com s’ha triat eixa mostra, la seua mida i la seua procedència.

El laboratori usa `TreeExplainer`, un bosc de regressió, una mostra d’entrenament com a fons i `feature_perturbation="interventional"`. Esta configuració té supòsits sobre les dependències entre predictors; la denominació «interventional» no convertix el resultat en una estimació causal del consum.

Una mitjana de valors SHAP absoluts resumeix magnitud global, però perd direcció i heterogeneïtat. Dues persones poden tindre contribucions oposades per a la mateixa variable. Revisa casos concrets a més del resum.

## 5. LIME: aproximar un entorn

LIME genera variacions al voltant d’un cas, consulta el model i ajusta una aproximació local interpretable. La seua lectura depén de la distància, de la ponderació, del mostreig i de la representació de variables contínues o categòriques.

Un coeficient gran en el substitut local no és un coeficient del model original. És una propietat de l’aproximació en l’entorn explorat. Si les pertorbacions generen habitatges impossibles, l’explicació pot descriure comportaments que no tenen sentit en l’ús real.

Cal revisar la fidelitat local. En l’execució de referència del laboratori, la puntuació del substitut és aproximadament **0,15**: això és un senyal per no confiar en una lectura forta dels seus pesos. El propòsit docent és detectar esta limitació, no ocultar-la.

Augmentar el nombre de mostres pot reduir variabilitat de mostreig, però no arregla necessàriament un entorn mal definit o una aproximació inadequada. Compara diverses llavors i configuracions, registra el resultat i explica si les conclusions es mantenen.

## 6. Explicacions globals, locals i contradictòries

És possible que una variable siga important globalment i contribuïsca poc en un cas concret. No hi ha contradicció: les preguntes són diferents. També és possible que SHAP i LIME destaquen aspectes diferents, perquè usen referències i aproximacions distintes.

Una discrepància és una invitació a investigar: hi ha interaccions? El cas està lluny de les dades d’entrenament? Les variables són redundants? La fidelitat local és baixa? El model treballa amb variables transformades i l’explicació mostra noms equivocats?

En pipelines, conserva la correspondència entre transformacions i noms. Si una categoria es desplega en diverses columnes, explica si presentes cada columna o una agrupació. No etiquetes una contribució transformada com si fora una magnitud original sense verificar-ho.

## 7. Com redactar una interpretació defensable

Una fitxa útil conté el cas, la predicció, la unitat, la base de comparació, les principals contribucions, el mètode i una limitació. Per exemple: «El model estima 109 unitats de consum; la referència és 91. La superfície i l’ocupació eleven la predicció en este cas. Esta explicació descriu el model i no demostra l’efecte d’una intervenció real».

Evita frases com «augmenta l’ocupació i estalviaràs» a partir d’una correlació o d’un pes local. També evita usar l’explicació com a substitut de l’avaluació: un model amb bon relat i errors grans continua sent poc útil.

## 8. Lectura del laboratori

Es generen 300 habitatges sintètics amb superfície, ocupants i una variable de soroll. El model s’ajusta només amb entrenament; les importàncies es calculen en validació. S’expliquen cinc casos amb SHAP i un amb LIME.

La suma SHAP es comprova numèricament amb tolerància. El fitxer CSV permet revisar les contribucions i l’HTML de LIME mostra l’aproximació local. Les dades tenen una relació generadora coneguda per facilitar la crítica; això no implica que totes les explicacions recuperen perfectament eixa relació.

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
"""Explicacions d'un model de consum sintètic; no inferència causal."""
from pathlib import Path
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.inspection import permutation_importance
from sklearn.metrics import mean_absolute_error
import shap
from lime.lime_tabular import LimeTabularExplainer

def main():
    rng = np.random.default_rng(21)
    X = pd.DataFrame({'superficie': rng.uniform(40, 180, 300), 'ocupants': rng.integers(1, 6, 300), 'soroll': rng.normal(0, 1, 300)})
    y = 20 + 0.45 * X.superficie + 8 * X.ocupants + rng.normal(0, 4, len(X))
    (train, valid, yt, yv) = train_test_split(X, y, test_size=0.25, random_state=42)
    model = RandomForestRegressor(n_estimators=60, min_samples_leaf=4, random_state=42, n_jobs=1).fit(train, yt)
    print('MAE de validació:', mean_absolute_error(yv, model.predict(valid)))
    # Importància sobre validació: no sobre les dades d’ajust.
    perm = permutation_importance(model, valid, yv, scoring='neg_mean_absolute_error', n_repeats=5, random_state=42)
    print('Importància per permutació:', dict(zip(X.columns, perm.importances_mean)))
    # La referència SHAP procedix d’entrenament i queda documentada.
    background = train.sample(60, random_state=42)
    explainer = shap.TreeExplainer(model, data=background, feature_perturbation='interventional')
    explanation = explainer(valid.iloc[:5])
    # Comprovem l’additivitat en l’escala de regressió del model.
    reconstruction = explanation.base_values + explanation.values.sum(axis=1)
    assert np.allclose(reconstruction, model.predict(valid.iloc[:5]), atol=0.0001)
    print('Predicció local:', model.predict(valid.iloc[[0]])[0])
    print('Base:', explanation.base_values[0], 'Contribucions:', explanation.values[0])

    def predict(array):
        return model.predict(pd.DataFrame(array, columns=X.columns))
    local = LimeTabularExplainer(train.to_numpy(), feature_names=list(X.columns), mode='regression', random_state=42)
    # Exigim revisar la fidelitat local abans d’interpretar els pesos.
    result = local.explain_instance(valid.iloc[0].to_numpy(), predict, num_features=3, num_samples=1000)
    print('LIME:', result.as_list(), 'Fidelitat local:', result.score)
    out = Path(__file__).resolve().parent / 'eixides'
    out.mkdir(exist_ok=True)
    pd.DataFrame(explanation.values, columns=X.columns).to_csv(out / 'shap-local.csv', index=False)
    result.save_to_file(str(out / 'lime-local.html'))
if __name__ == '__main__':
    main()
```

## Pràctiques guiades

Cada pràctica deixa una evidència petita: una eixida comprovada i una explicació de la decisió. Els temps són orientatius i no inclouen instal·lació.

### Pràctica 1 · Importància i rendiment

**Nivell i temps:** Inicial · 20–30 min.

**Objectiu:** Interpretar una importància global a partir d’un model avaluat.

**Materials:** exemple comentat d’esta unitat, les seues eixides i una còpia de treball per a les modificacions.

**Procediment:**

1. Executa el laboratori i registra primer el MAE de validació.
2. Ordena les importàncies per permutació i identifica la variable de soroll.
3. Compara la importància amb la relació generadora coneguda de les dades sintètiques.
4. Escriu una frase que descriga dependència predictiva sense atribuir causalitat.

!!! success "Comprovació i evidència esperada"
    Superfície i ocupants aporten informació en este model; el soroll té una importància molt menor en l’execució de referència.

**Preguntes de reflexió:**

- Per què cal conéixer el rendiment abans de confiar en una explicació?
- Què podria passar amb dues variables redundants?
- Una importància negativa demostra un efecte protector?

**Ampliació opcional:** Augmenta les repeticions de permutació i mostra també la dispersió dels resultats.

### Pràctica 2 · Reconstruir una predicció SHAP

**Nivell i temps:** Intermèdia · 30–45 min.

**Objectiu:** Llegir contribucions amb una base i una unitat explícites.

**Materials:** exemple comentat d’esta unitat, les seues eixides i una còpia de treball per a les modificacions.

**Procediment:**

1. Pren el primer cas explicat i anota predicció, valor base i les tres contribucions.
2. Suma-les manualment o amb un càlcul separat i compara amb la predicció.
3. Redacta una fitxa local que distingisca contribucions positives i negatives.
4. Canvia en una còpia la mostra de fons, mantenint el model, i compara base i atribucions.

!!! success "Comprovació i evidència esperada"
    Base més contribucions reconstruïx la predicció amb tolerància; canviar la referència pot redistribuir atribucions.

**Preguntes de reflexió:**

- Què significa que una contribució siga negativa?
- Per què cal documentar el conjunt de fons?
- Quina part de la conclusió seria incorrecta si usàrem el verb causar?

**Ampliació opcional:** Compara dos casos amb prediccions semblants i comprova si les contribucions també ho són.

### Pràctica 3 · Criticar una explicació LIME

**Nivell i temps:** Avançada · 45–60 min.

**Objectiu:** Avaluar fidelitat i estabilitat abans de comunicar pesos locals.

**Materials:** exemple comentat d’esta unitat, les seues eixides i una còpia de treball per a les modificacions.

**Procediment:**

1. Obri `lime-local.html` i localitza els pesos de l’aproximació.
2. Relaciona’ls amb la puntuació de fidelitat impresa, pròxima a 0,15 en l’execució comprovada.
3. Repetix l’explicació amb una altra llavor i amb més mostres, conservant el mateix cas.
4. Registra configuració, puntuació i canvis dels factors destacats; decidix si hi ha prou evidència per usar la interpretació.

!!! success "Comprovació i evidència esperada"
    La conclusió pot ser que l’aproximació no és prou fidel; no s’exigix que augmente la puntuació per completar la pràctica.

**Preguntes de reflexió:**

- Quina diferència hi ha entre la predicció original i el substitut local?
- Per què més mostres no asseguren una millor explicació?
- Quines pertorbacions podrien generar observacions impossibles?

**Ampliació opcional:** Compara discretització activada i desactivada i explica quina pregunta local està responent cada configuració.

## Exercicis autònoms

Intenta resoldre cada repte abans de desplegar l’orientació. Es valora el raonament i les comprovacions, no només obtindre una xifra.

### Repte 1 · Llegir signes

Una base és 50 i les contribucions són +12, −4 i +2. Interpreta el resultat.

??? example "Solució orientativa i criteri de revisió"
    La predicció és 60, deu unitats per damunt de la base. El signe negatiu reduïx la predicció respecte d’eixa referència; no implica una valoració moral ni un efecte causal.

### Repte 2 · Global i local

Explica com una variable important globalment pot aportar quasi zero en un cas.

??? example "Solució orientativa i criteri de revisió"
    El resum global agrega casos; el cas concret pot situar-se prop de la referència o en una regió on la variable tinga poc efecte en el model. Cal identificar la pregunta de cada gràfic.

### Repte 3 · Fidelitat baixa

Redacta una conclusió si LIME produïx pesos clars però puntuació local baixa.

??? example "Solució orientativa i criteri de revisió"
    No dones una interpretació forta dels pesos. Informa de l’aproximació deficient, revisa entorn i mostreig i contrasta alternatives. Un gràfic llegible no és una evidència de fidelitat.

## Errors habituals i diagnòstic

| Símptoma | Causa que convé investigar | Comprovació o correcció |
|---|---|---|
| La suma no coincidix amb la predicció | Escala de sortida, model o cas diferents. | Comprova base, unitats i les mateixes entrades. |
| SHAP i LIME no destaquen el mateix | Referències i aproximacions diferents. | Examina supòsits i fidelitat local. |
| Pes interpretat com causa | Confusió entre model i mecanisme real. | Redacta la conclusió com a comportament predictiu. |

## Autoavaluació i evidències

Abans de donar la unitat per treballada, comprova estos punts i escriu una frase d’evidència per a cadascun:

- [ ] Puc distingir explicacions globals i locals.
- [ ] Puc reconstruir una predicció a partir de contribucions SHAP.
- [ ] Puc comprovar la fidelitat i els supòsits d’una explicació LIME.
- [ ] He executat el laboratori i he contrastat almenys un resultat independentment.
- [ ] Puc explicar una limitació i un cas en què el procediment requeriria canvis.

**Lliurable de la píndola:** còpia de treball reproduïble, resultats de la pràctica seleccionada i un text breu que indique pregunta, decisió, comprovació i limitació. Si s’usa dins de BiciTierra Market, integra esta evidència en el lliurable setmanal corresponent; no cal crear una entrega duplicada.

## Fonts per aprofundir

- [Documentació oficial de referència](https://shap.readthedocs.io/en/latest/generated/shap.TreeExplainer.html). Consulta especialment els conceptes i els supòsits descrits en la unitat.
- [Documentació oficial de LIME](https://lime-ml.readthedocs.io/en/latest/lime.html).

Les versions executades i els límits de la comprovació estan en el [registre de validació](../VALIDACIO.md). Els exemples són originals i les dades són sintètiques.

## Aplicació final a BiciTierra Market

**Moment orientatiu:** setmana 5. Esta correspondència ajuda a triar materials i no substituïx el document de treball de l’alumnat.

Explica el model de vendes que haja superat la validació, sobre casos seleccionats amb un criteri explícit. Documenta fons, escala i correspondència de variables del pipeline. Diferencia associacions predictives de recomanacions causals sobre preus o promocions.

**Transferència:** identifica quin concepte acabes de practicar, quina dada del projecte l’exigix i què has de canviar respecte del laboratori. Justifica eixa adaptació abans de copiar codi.
