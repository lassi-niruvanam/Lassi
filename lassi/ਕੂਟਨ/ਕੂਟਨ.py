import site as ਜਗਹ
import os
import json
import random

from lassi.ਜ਼ਬਾਨੋਂ import ਜ਼ਬਾਨੋਂ


class ਕੂਟਨ_ਘਟ(object):
    def __init__(ਖੁਦ, ਕੂਟਨ_ਨਾਮ, ਖੁਦ_ਜ਼ਬਾਨ, ਰਾਸ੍ਤਾ=None, ਅਨੁਵਾਦ_ਦਸ੍ਤਾਵੇਜ਼='ਅਨੁ', ign=None):

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
        if ign is None:
            ign = []
        if ਖੁਦ.ਅਨੁਵਾਦ_ਦਸ੍ਤਾਵੇਜ਼ not in ign:
            ign.append(ਖੁਦ.ਅਨੁਵਾਦ_ਦਸ੍ਤਾਵੇਜ਼)
        ਖੁਦ.ignore = ign

        ਖੁਦ.ਖੁਦ_ਜ਼ਬਾਨ = ਖੁਦ_ਜ਼ਬਾਨ

        ਖੁਦ.ਕੋਸ਼ = {}

        ਖੁਦ.ਪਢਨਾ()

    def ਪਢਨਾ(ਖੁਦ):
        raise NotImplementedError

    def gén_dict_trads(ਖੁਦ):
        ਖੁਦ.d_lin = {}

        lin_dic(ਖੁਦ.ਕੋਸ਼, d_l=ਖੁਦ.d_lin)

        ਖੁਦ.ਕੋਸ਼_ਅਨੁ = {ll: {ਖੁਦ.ਖੁਦ_ਜ਼ਬਾਨ: v['ਨਾਮ']} for ll, v in ਖੁਦ.d_lin.items()}

    def ajouter_langue(ਖੁਦ, langue):
        for ll, v in ਖੁਦ.ਕੋਸ਼_ਅਨੁ.items():
            if langue not in v:
                v[langue] = ''

    def écire_dic_pour_trad(ਖੁਦ):
        écrire_json(dic=ਖੁਦ.ਕੋਸ਼_ਅਨੁ, doc=os.path.join(ਖੁਦ.ਰਾਸ੍ਤਾ_ਪੂਰੀ, ਖੁਦ.ਅਨੁਵਾਦ_ਦਸ੍ਤਾਵੇਜ਼, ਖੁਦ.ਅਨੁਵਾਦ_ਦਸ੍ਤਾਵੇਜ਼ + '.json'))

    def ਅਨੁਵਾਦ_ਲਿਖਣਾ(ਖੁਦ, ਜ਼ਬਾਨ):
        code = ਜ਼ਬਾਨੋਂ[ਜ਼ਬਾਨ]['code']

        ਰਾਸ੍ਤਾ = os.path.join(ਖੁਦ.ਰਾਸ੍ਤਾ_ਪੂਰੀ, ਖੁਦ.ਅਨੁਵਾਦ_ਦਸ੍ਤਾਵੇਜ਼, code)

        ਖੁਦ._ਅਨੁਵਾਦ_ਲਿਖਣਾ(ਰਾਸ੍ਤਾ=ਰਾਸ੍ਤਾ, ਜ਼ਬਾਨ=ਜ਼ਬਾਨ)

    def _ਅਨੁਵਾਦ_ਲਿਖਣਾ(ਖੁਦ, ਰਾਸ੍ਤਾ, ਜ਼ਬਾਨ):
        raise NotImplementedError

def lin_dic(d, d_l, p=None):
    if p is None:
        p = []

    if 'ਸੱਮਗਰੀ' in d:
        for ll, v in d['ਸੱਮਗਰੀ'].items():
            ਪ੍ਰਕਾਰ = v['ਪ੍ਰਕਾਰ']
            if ਪ੍ਰਕਾਰ == 'import':
                continue

            nouv = {'ਨਾਮ': ll, 'ਪ੍ਰਕਾਰ': v['ਪ੍ਰਕਾਰ'], 'ਜਗਾਹ': p.copy()}
            n = gén_nombre(n_c=8, interdits=d_l.keys())
            d_l[n] = nouv
            v['num'] = n

            p.append(ll)

            lin_dic(d=v, d_l=d_l, p=p)

            p.pop()


def gén_nombre(n_c, interdits):

    máx = 10**n_c
    if len(set(interdits)) >= máx:
        raise ValueError

    m = random.randint(0, máx)

    while m in interdits:
        m = random.randint(0, máx)

    return str(m)


def écrire_json(dic, doc):
    if not os.path.isdir(os.path.split(doc)[0]):
        os.makedirs(os.path.split(doc)[0])

    with open(doc, 'w', encoding='utf8') as d:
        json.dump(dic, d, ensure_ascii=False, sort_keys=True, indent=2)