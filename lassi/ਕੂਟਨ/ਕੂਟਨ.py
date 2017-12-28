import site as ਜਗਹ
import os


class ਕੂਟਨ_ਘਟ(object):
    def __init__(ਖੁਦ, ਕੂਟਨ_ਨਾਮ, ਰਾਸ੍ਤਾ=None, ਅਨੁਵਾਦ_ਦਸ੍ਤਾਵੇਜ਼='ਅਨੁ'):

        if ਰਾਸ੍ਤਾ is None:
            for ਜ in ਜਗਹ.getsitepackages():
                if os.path.isdir(os.path.join(ਜ, ਕੂਟਨ_ਨਾਮ)):
                    ਰਾਸ੍ਤਾ = ਜ
                    break

            if ਰਾਸ੍ਤਾ is None:
                raise ValueError('"{}" ਦਾ ਹਾਸ੍ਤਾ ਮਿਲੀ ਨਹੀਂ।'.format(ਕੂਟਨ_ਨਾਮ))
        else:
            if not os.path.isdir(os.path.join(ਰਾਸ੍ਤਾ, ਕੂਟਨ_ਨਾਮ)):
                raise ValueError('"{}" ਹਾਸ੍ਤਾ ਵਿਚ "{}" ਨਾਮ ਦਾ ਕੂਟਨ ਮਿਲੀ ਨਹੀਂ।'.format(ਰਾਸ੍ਤਾ, ਕੂਟਨ_ਨਾਮ))

        ਖੁਦ.ਕੂਟਨ = ਕੂਟਨ_ਨਾਮ
        ਖੁਦ.ਰਾਸ੍ਤਾ = ਰਾਸ੍ਤਾ
        ਖੁਦ.ਰਾਸ੍ਤਾ_ਪੂਰੀ = os.path.join(ਰਾਸ੍ਤਾ, ਕੂਟਨ_ਨਾਮ)
        ਖੁਦ.ਅਨੁਵਾਦ_ਦਸ੍ਤਾਵੇਜ਼ = ਅਨੁਵਾਦ_ਦਸ੍ਤਾਵੇਜ਼

        ਖੁਦ.ਕੋਸ਼ = {}

        ਖੁਦ.ਪਢਨਾ()

    def ਪਢਨਾ(ਖੁਦ):
        raise NotImplementedError

    def ਲਿਖਣਾ(ਖੁਦ, ਰਾਸ੍ਤਾ):
        raise NotImplementedError

