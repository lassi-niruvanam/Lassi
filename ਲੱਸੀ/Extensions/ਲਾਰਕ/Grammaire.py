from ਲੱਸੀ.TradGrammaire.ਭਾਸ਼ਾ import ExtGrammaire


class GrammaireLark(ExtGrammaire):
    gram = 'ਲਾਰਕ.lark'
    ext = '.lark'
    langue_orig = 'en'


g = GrammaireLark()
g.gén_arch_trads()
g.gén_trads(['த', 'ગુ', 'हिं', 'fr', 'kaq'])
