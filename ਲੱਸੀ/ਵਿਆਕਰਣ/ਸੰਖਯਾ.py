from எண்ணிக்கை import உரைக்கு, regex


class ਸੰਖਯਾ_ਅਨੁਵਾਦਵਾਲਾ(object):
    def __init__(ਖੁਦ, ਭਾਸ਼ਾ, ਨਾਮ, autre=None):
        ਖੁਦ.ਭਾਸ਼ਾ = ਭਾਸ਼ਾ
        ਖੁਦ.ਨਾਮ = ਨਾਮ
        ਖੁਦ.autre = autre if autre is not None else (lambda x: x)

    def regexp(ਖੁਦ):
        return regex(ਖੁਦ.ਭਾਸ਼ਾ)

    def __call__(ਖੁਦ, ਪਾਠ):
        for x in ਖੁਦ.autre(ਖੁਦ.proc(ਪਾਠ)):
            yield x

    def proc(ਖੁਦ, ਪਾਠ):
        for x in ਪਾਠ:
            if hasattr(x, 'type') and x.type == ਖੁਦ.ਨਾਮ:
                yield traduire(x, ਖੁਦ.ਭਾਸ਼ਾ)
            else:
                yield x


def traduire(x, ਭਾਸ਼ਾ):
    return உரைக்கு(x, ਭਾਸ਼ਾ)
