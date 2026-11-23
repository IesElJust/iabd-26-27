"""Mecànica de classificació textual amb dades sintètiques; no valida el pilot."""
from sklearn.pipeline import make_pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix


def main():
    entrenament = [
        ('contrasenya incorrecta en iniciar sessio', 'identitat'),
        ('compte bloquejat per intents de contrasenya', 'identitat'),
        ('canviar contrasenya del compte', 'identitat'),
        ('vpn amb error de certificat', 'xarxes'),
        ('connexio vpn interrompuda', 'xarxes'),
        ('renovar certificat per a vpn', 'xarxes'),
        ('correu amb quota plena', 'correu'),
        ('missatge de correu rebotat', 'correu'),
        ('configuracio imap del correu', 'correu'),
    ]
    prova = [
        ('compte amb contrasenya incorrecta', 'identitat'),
        ('vpn no connecta per certificat', 'xarxes'),
        ('quota de correu plena', 'correu'),
    ]
    x, y = zip(*entrenament)
    xt, yt = zip(*prova)
    model = make_pipeline(TfidfVectorizer(strip_accents='unicode', ngram_range=(1, 2)),
                          LogisticRegression(max_iter=1000, random_state=42))
    model.fit(x, y)
    pred = model.predict(xt)
    classes = sorted(set(y))
    print(classification_report(yt, pred, labels=classes, zero_division=0))
    print('Ordre de files i columnes:', classes)
    print(confusion_matrix(yt, pred, labels=classes))
    desconegut = ['xyzzy qqqvv']
    vector = model[0].transform(desconegut)
    print('Termes reconeguts:', vector.nnz)
    print('Etiqueta tot i no reconeixer termes:', model.predict(desconegut)[0])
    assert vector.nnz == 0


if __name__ == '__main__':
    main()
