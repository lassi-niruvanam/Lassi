import os
import regex

from lassi.ਕੂਟਨ.ਕੂਟਨ import ਕੂਟਨ_ਘਟ


class ਕੂਟਨ_ਪੈਧਾਨ(ਕੂਟਨ_ਘਟ):

    def ਲਿਖਣਾ(ਖੁਦ, ਰਾਸ੍ਤਾ):
        raise NotImplementedError

    def ਪਢਨਾ(ਖੁਦ):
        ਖੁਦ.ਕੋਸ਼.clear()
        ਖੁਦ.ਕੋਸ਼['ਪ੍ਰਕਾਰ'] = 'ਕੂਟਨ'
        ਖੁਦ.ਕੋਸ਼['ਸੱਮਗਰੀ'] = {}

        for ਰਾ, ਨਤ੍ਥੀ, ਦਸ੍ਤ in os.walk(ਖੁਦ.ਰਾਸ੍ਤਾ_ਪੂਰੀ):

            ਕੋਸ਼ = ਖੁਦ.ਕੋਸ਼['ਸੱਮਗਰੀ']
            for ਰ in ਰਾਸ੍ਤਾ_ਟੂਠਨਾ(os.path.relpath(ਰਾ, ਖੁਦ.ਰਾਸ੍ਤਾ_ਪੂਰੀ)):
                if ਰ != '.' and ਰ != '' and ਰ[0] != '_':
                    ਕੋਸ਼ = ਕੋਸ਼[ਰ]['ਸੱਮਗਰੀ']

            for ਨ in ਨਤ੍ਥੀ:
                if ਨ[0] != '_':
                    ਕੋਸ਼[ਨ] = {
                        'ਪ੍ਰਕਾਰ': 'ਨਤ੍ਥੀ', 'ਸੱਮਗਰੀ': {}
                    }
            for ਦ in ਦਸ੍ਤ:
                if ਦ[0] != '_' and os.path.splitext(ਦ)[1] == '.py':
                    ਸੱਮਗਰੀ = ਦਸ੍ਤ_ਸੱਮਗਰੀ_ਪਾਣਾ(ਦਸ੍ਤ, ਰਾ)
                    if len(ਸੱਮਗਰੀ):
                        ਕੋਸ਼[ਦ] = {
                            'ਪ੍ਰਕਾਰ': 'ਦਸ੍ਤ', 'ਸੱਮਗਰੀ': ਸੱਮਗਰੀ
                        }


def ਰਾਸ੍ਤਾ_ਟੂਠਨਾ(ਰਾਸ੍ਤਾ, ਫ=None):
    if ਫ is None:
        ਫ = []
    ਟੂਠੀ = os.path.split(ਰਾਸ੍ਤਾ)
    ਫ.insert(0, ਟੂਠੀ[1])
    if len(ਟੂਠੀ[0]):
        ਰਾਸ੍ਤਾ_ਟੂਠਨਾ(ਟੂਠੀ[0], ਫ=ਫ)

    return ਫ


def ਦਸ੍ਤ_ਸੱਮਗਰੀ_ਪਾਣਾ(ਦਸ੍ਤ, ਰਾਸ੍ਤਾ):
    ਸੱਮਗਰੀ = {}

    re_ident = r'[\p{M}\p{L}_]+[\p{M}\p{L}\p{N}_]*'
    re_args = r'{}'
    re_func_comp = r'def[\s]+{}({}):'.format(re_ident, re_args)
    re_clase = r''
    with open(os.path.join(ਰਾਸ੍ਤਾ, ਦਸ੍ਤ)) as ਦ:
        ਰੇ = ਦ.readline()


    return ਸੱਮਗਰੀ


ਨਮੁਨਹ = ਕੂਟਨ_ਪੈਧਾਨ(ਕੂਟਨ_ਨਾਮ='tinamit', ਰਾਸ੍ਤਾ='C:\\Users\\USERS1\PycharmProjects\Tinamit')
import pprint

pprint.pprint(ਨਮੁਨਹ.ਕੋਸ਼, indent=2)
