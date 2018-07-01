from ਲੱਸੀ.TradGrammaire.ਭਾਸ਼ਾ import ExtGrammaire


class GrammaireJSON(ExtGrammaire):
    gram = 'ਜੇਸਾਨ.lark'
    ext = '.json'
    langue_orig = 'en'

g = GrammaireJSON()
g.gén_arch_trads()
g.gén_trads(['த', 'ગુ', 'हिं', 'fr', 'kaq'])
