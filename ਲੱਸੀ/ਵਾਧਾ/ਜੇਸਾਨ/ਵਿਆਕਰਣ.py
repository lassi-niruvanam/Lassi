import pprint

from ਲੱਸੀ.ਵਿਆਕਰਣ.ਭਾਸ਼ਾ import ਵਿਆਕਰਣ_ਵਾਧਾ


class GrammaireJSON(ਵਿਆਕਰਣ_ਵਾਧਾ):
    ਵਿਆ = 'ਜੇਸਾਨ.lark'
    ਵਾਧਾ = '.json'
    ਸਰੋਤ_ਭਾ = 'en'

    def ਬਾਅਦ_ਕਾਰਵਾਈ(ਖੁਦ, ਦਸਤ):
        return pprint.pformat(ਦਸਤ)

if __name__ == '__main__':
    g = GrammaireJSON()
    g.gén_arch_trads()
    g.gén_trads(['த', 'ગુ', 'हिं', 'fr', 'kaq'])
