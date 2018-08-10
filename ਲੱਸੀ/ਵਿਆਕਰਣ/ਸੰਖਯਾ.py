from ਲੱਸੀ.ਵਿਆਕਰਣ.utils import postprocesseur
from எண்ணிக்கை import உரைக்கு, வழவெளி


class ਸੰਖਯਾ_ਅਨੁਵਾਦਵਾਲਾ(postprocesseur):
    def __init__(ਖੁਦ, ਭਾਸ਼ਾ, ਨਾਮ):
        ਖੁਦ.ਭਾਸ਼ਾ = ਭਾਸ਼ਾ
        if isinstance(ਨਾਮ, str):
            ਨਾਮ = [ਨਾਮ]
        ਖੁਦ.ਨਾਮ = ਨਾਮ
        super().__init__()

    def regexp(ਖੁਦ):
        return வழவெளி(ਖੁਦ.ਭਾਸ਼ਾ)

    def proc(ਖੁਦ, ਪਾਠ):
        for x in ਪਾਠ:
            if hasattr(x, 'type') and x.type in ਖੁਦ.ਨਾਮ:
                yield traduire(x, ਖੁਦ.ਭਾਸ਼ਾ)
            else:
                yield x


def traduire(x, ਭਾਸ਼ਾ):
    try:
        return உரைக்கு(str(x), ਭਾਸ਼ਾ)
    except ValueError:
        return str(x)
