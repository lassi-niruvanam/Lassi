import pprint

from ਲੱਸੀ.ਵਿਆਕਰਣ.ਭਾਸ਼ਾ import ਵਿਆਕਰਣ_ਵਾਧਾ


class GrammaireJSON(ਵਿਆਕਰਣ_ਵਾਧਾ):
    ਵਿਆ = 'ਜੇਸਾਨ.lark'
    ਵਾਧਾ = '.json'
    ਸਰੋਤ_ਭਾ = 'en'

    def ਬਾਅਦ_ਕਾਰਵਾਈ(ਖੁਦ, ਦਸਤ):
        return pprint.pformat(ਦਸਤ)
