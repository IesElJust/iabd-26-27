"""Comprovació estructural: NO verifica veracitat ni suport factual."""


def validar(resultat, fonts_disponibles):
    if not isinstance(resultat, dict):
        return False
    if set(resultat) != {'estat', 'resposta', 'fonts'}:
        return False
    estat, text, fonts = resultat['estat'], resultat['resposta'], resultat['fonts']
    if estat not in ('respondre', 'derivar') or not isinstance(text, str) or not text.strip():
        return False
    if not isinstance(fonts, list) or not all(isinstance(f, str) for f in fonts):
        return False
    if any(f not in fonts_disponibles for f in fonts):
        return False
    if estat == 'respondre' and not fonts:
        return False
    return True


if __name__ == '__main__':
    fonts = {'contrasenyes:01'}
    casos = [
        ({'estat': 'respondre', 'resposta': 'El bloqueig dura 15 minuts.',
          'fonts': ['contrasenyes:01']}, True),
        ({'estat': 'respondre', 'resposta': 'Resposta sense font disponible.',
          'fonts': ['inventada:99']}, False),
        ({'estat': 'derivar', 'resposta': 'Falta context suficient.', 'fonts': []}, True),
        ({'estat': 'respondre', 'resposta': 'El bloqueig dura 900 anys.',
          'fonts': ['contrasenyes:01']}, True),
    ]
    for resultat, esperat in casos:
        observat = validar(resultat, fonts)
        assert observat == esperat
        print(observat, resultat)
    print("L’últim cas passa el format però és fals: cal revisar suport factual.")
