import os

from ਲੱਸੀ.TradGrammaire.ਭਾਸ਼ਾ import ਵਿਆਕਰਣ_ਵਧਾ


def ਮੁੜ_ਉਸਾਰੀ_ਬਾਅਦ_ਕਾਰ(ਪਾਠ):
    for ਅ in ਪਾਠ:
        yield '{} '.format(ਅ) if len(ਅ.strip()) and not ਅ.strip(' \t').endswith('\n') else ਅ


class ਲਾਰਕ_ਵਿਆਕਰਣ(ਵਿਆਕਰਣ_ਵਧਾ):
    ਵਿਆ = os.path.join(os.path.split(__file__)[0], 'ਲਾਰਕ.lark')
    ਵਾਧਾ = '.lark'
    ਸਰੋਤ_ਭਾ = 'en'
    ਮੁੜ_ਉਸਾਰੀ_ਬਦਲ = dict(postproc=ਮੁੜ_ਉਸਾਰੀ_ਬਾਅਦ_ਕਾਰ)


g = ਲਾਰਕ_ਵਿਆਕਰਣ()
g.gén_arch_trads()
g.gén_trads(['த', 'ગુ', 'हिं', 'fr', 'kaq'])
