import pprint

from ਲੱਸੀ.TradGrammaire.ਭਾਸ਼ਾ import ਵਿਆਕਰਣ_ਵਧਾ


class GrammaireJSON(ਵਿਆਕਰਣ_ਵਧਾ):
    ਵਿਆ = 'ਜੇਸਾਨ.lark'
    ਵਾਧਾ = '.json'
    ਸਰੋਤ_ਭਾ = 'en'

    def ਬਾਅਦ_ਕਾਰਵਾਈ(ਖੁਦ, ਦਸਤ):
        return pprint.pformat(ਦਸਤ)

g = GrammaireJSON()
g.gén_arch_trads()
g.gén_trads(['த', 'ગુ', 'हिं', 'fr', 'kaq'])
