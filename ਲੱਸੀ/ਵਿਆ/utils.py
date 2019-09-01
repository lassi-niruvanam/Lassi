import os


class postprocesseur(object):
    def __init__(ਖੁਦ):
        ਖੁਦ.liste_proc = [ਖੁਦ.proc]

    def __mul__(ਖੁਦ, autre):
        if autre is not None:
            if isinstance(autre, postprocesseur):

                for a in autre.liste_proc:
                    if a not in ਖੁਦ.liste_proc:
                        ਖੁਦ.liste_proc.append(a)
            elif autre not in ਖੁਦ.liste_proc:
                ਖੁਦ.liste_proc.append(autre)
        return ਖੁਦ

    def __call__(ਖੁਦ, ਪਾਠ):
        for p in ਖੁਦ.liste_proc:
            ਪਾਠ = p(ਪਾਠ)
        return ਪਾਠ

    def proc(ਖੁਦ, ਪਾਠ):
        raise NotImplementedError


class proc_mots_spéciaux(postprocesseur):
    def __init__(ਖੁਦ, règles):
        super().__init__()
        ਖੁਦ.règles = {d['ਸਰੋਤ']: d['ਅਨੁ'] for d in règles if len(d['ਅਨੁ'])}

    def proc(ਖੁਦ, ਪਾਠ):
        for x in ਪਾਠ:
            if x in ਖੁਦ.règles and len(ਖੁਦ.règles[x]):
                yield ਖੁਦ.règles[x]
            else:
                yield x


def résoudre_ext(fichier):
    possibilités = []
    nom, ext = os.path.splitext(fichier)
    nom, ext2 = os.path.splitext(nom)

    grammaires = []
    for grm in grammaires:
        if ext in grm.exts():
            if ext2 in grm.langues():
                possibilités.append((grm, ext2))
            else:
                possibilités.append((grm, None))

    if len(possibilités):
        return possibilités
    else:
        raise ValueError(fichier)


if __name__ == '__main__':
    résoudre_ext('abc.py')
