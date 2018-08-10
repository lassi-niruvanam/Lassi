import inspect
import json
import os

from lark import Lark, Tree
from lark.reconstruct import Reconstructor
from ਲੱਸੀ.ਵਿਆਕਰਣ.utils import proc_mots_spéciaux
from ਲੱਸੀ.ਵਿਆਕਰਣ.ਸੰਖਯਾ import ਸੰਖਯਾ_ਅਨੁਵਾਦਵਾਲਾ


class ਵਿਆਕਰਣ_ਵਾਧਾ(object):
    ਵਿਆ = NotImplemented
    ਵਾਧਾ = NotImplemented
    ਸਰੋਤ_ਭਾ = NotImplemented
    ਰਾਸਤਾ = None

    ਸ਼ਬਦ_ਵਿਸ਼_ਬਦਲ = {'parser': 'lalr'}

    ਦਸਤ_ਸਰੋਤ_ਅਨੁ = 'ਵਿਆ_ਅਨੁ/_ਸਰੋਤ.json'
    ਅਨੂ_ਰਾਸਤਾ = 'ਵਿਆ_ਅਨੁ'

    spéciaux = {}

    def __init__(ਖੁਦ):
        if ਖੁਦ.ਰਾਸਤਾ is None:
            ਖੁਦ.ਰਾਸਤਾ = os.path.split(inspect.getfile(ਖੁਦ.__class__))[0]
        ਖੁਦ._ਵਿਸ਼ਲੇਸ਼ਣ = {}
        ਖੁਦ._ਮੁੜ_ਉਸਾਰੀ = {}
        ਖੁਦ.ਕੋਸ਼_ਵਿਆ = {}
        ਖੁਦ.ਮੁੜ_ਉਸਾਰੀ_ਬਦਲ = {}

    def actualizar_trads(ਖੁਦ, ਭਾਸ਼ਾਵਾਂ):

        ਖੁਦ.ਦਸਤ_ਸਰੋਤ_ਅਨੁ_ਬੲਾਉ()

        for ਭਾ in ਭਾਸ਼ਾਵਾਂ:
            ਨਵੀਂ_ਕੋਸ਼ = ਖੁਦ._ਦਸਤਾਵੇਜ਼_ਖੋਲ੍ਹਨਾ(ਖੁਦ.ਦਸਤ_ਸਰੋਤ_ਅਨੁ, ਜੇਸਾਨ_ਤੋਂ=True)
            ਨਵੀਂ_ਕੋਸ਼['ਭਾਸ਼ਾ'] = ਭਾ
            ਦ = [ਖੁਦ.ਅਨੂ_ਰਾਸਤਾ, ਭਾ + '.json']

            try:
                ਙਾਸ਼ਾ_ਕੋਸ਼ = ਖੁਦ._ਦਸਤਾਵੇਜ਼_ਖੋਲ੍ਹਨਾ(ਦ, ਜੇਸਾਨ_ਤੋਂ=True)
                ਖੁਦ.mettre_à_jour(ਙਾਸ਼ਾ_ਕੋਸ਼, ਨਵੀਂ_ਕੋਸ਼)
            except FileNotFoundError:
                pass

            ਖੁਦ._ਦਸਤਾਵੇਜ਼_ਲਿਖਣਾ(ਦ, ਨਵੀਂ_ਕੋਸ਼)

    def mettre_à_jour(soimême, d_orig, d_nouv):
        règles_nouvelles = d_nouv['ਨਿਯਮ']
        règles_anciennes = d_orig['ਨਿਯਮ']
        for i, d in enumerate(list(règles_nouvelles)):
            ancienne = next((d_a for d_a in règles_anciennes if d_a['ਸਰੋਤ'] in d['ਸਰੋਤ']), None)
            if ancienne is not None and len(ancienne['ਅਨੁ']):
                règles_nouvelles[i] = ancienne
                règles_anciennes.remove(ancienne)
        if 'ਪੂਰਾਨੀ ਨਿਯਮ' not in d_nouv:
            d_nouv['ਪੂਰਾਨੀ ਨਿਯਮ'] = []
        d_nouv['ਪੂਰਾਨੀ ਨਿਯਮ'] = d_orig['ਪੂਰਾਨੀ ਨਿਯਮ']
        d_nouv['ਪੂਰਾਨੀ ਨਿਯਮ'] += [r for r in règles_anciennes if len(r['ਅਨੁ'])]

        règles_nouvelles = d_nouv['ਵੇਸ਼ੇਸ਼ ਸ਼ਬਦ']
        règles_anciennes = d_orig['ਵੇਸ਼ੇਸ਼ ਸ਼ਬਦ'] if 'ਵੇਸ਼ੇਸ਼ ਸ਼ਬਦ' in d_orig else []
        for i, d in enumerate(list(règles_nouvelles)):
            ancienne = next((d_a for d_a in règles_anciennes if d_a['ਸਰੋਤ'] in d['ਸਰੋਤ']), None)
            if ancienne is not None and len(ancienne['ਅਨੁ']):
                règles_nouvelles[i] = ancienne
                règles_anciennes.remove(ancienne)
        if 'ਪੂਰਾਨੇ ਵੇਸ਼ੇਸ਼ ਸ਼ਬਦ' not in d_nouv:
            d_nouv['ਪੂਰਾਨੇ ਵੇਸ਼ੇਸ਼ ਸ਼ਬਦ'] = []
        d_nouv['ਪੂਰਾਨੇ ਵੇਸ਼ੇਸ਼ ਸ਼ਬਦ'] = d_orig['ਪੂਰਾਨੇ ਵੇਸ਼ੇਸ਼ ਸ਼ਬਦ']
        d_nouv['ਪੂਰਾਨੇ ਵੇਸ਼ੇਸ਼ ਸ਼ਬਦ'] += [r for r in règles_anciennes if len(r['ਅਨੁ'])]

    def ਦਸਤ_ਸਰੋਤ_ਅਨੁ_ਬੲਾਉ(ਥੁਦ):
        from ..ਵਾਧਾ.ਲਾਰਕ.ਵਿਆਕਰਣ import ਲਾਰਕ_ਵਿਆਕਰਣ
        ਵਿਆ = ਥੁਦ._ਦਸਤਾਵੇਜ਼_ਖੋਲ੍ਹਨਾ(ਥੁਦ.ਵਿਆ)
        ਲਾਰਕ = ਲਾਰਕ_ਵਿਆਕਰਣ()
        ਰੁੱਖ = ਲਾਰਕ.ਰੁੱਖ_ਬਣਾਉ(ਵਿਆ, ਭਾਸ਼ਾ='en')

        ਅਨੁ_ਕੋਸ਼ = {
            'ਵਾਧਾ': ਥੁਦ.ਵਾਧਾ,
            'ਸਰੋਤ_ਭਾ': ਥੁਦ.ਸਰੋਤ_ਭਾ,
            'ਨਿਯਮ': [
                {'ਸਰੋਤ': ਲਾਰਕ.ਸੰਕੇਤ_ਮੁੜ_ਉਸਾਰੀ(ਅ, ਥੁਦ.ਸਰੋਤ_ਭਾ), 'ਅਨੁ': '', 'ਰੁਤਬਾ': 'ਕਰਨੀ ਹੈ'}
                for ਅ in ਰੁੱਖ.children if isinstance(ਅ, Tree)
            ],
            'ਵੇਸ਼ੇਸ਼ ਸ਼ਬਦ': [
                {'ਸਰੋਤ': ਅ, 'ਅਨੁ': '', 'ਰੁਤਬਾ': 'ਕਰਨੀ ਹੈ'} for ਅ in ਥੁਦ.gén_mots_intégrés()],
        }

        if not os.path.isdir(os.path.dirname(ਥੁਦ.ਦਸਤ_ਸਰੋਤ_ਅਨੁ)):
            os.makedirs(os.path.dirname(ਥੁਦ.ਦਸਤ_ਸਰੋਤ_ਅਨੁ))
        ਥੁਦ._ਦਸਤਾਵੇਜ਼_ਲਿਖਣਾ(ਥੁਦ.ਦਸਤ_ਸਰੋਤ_ਅਨੁ, ਅਨੁ_ਕੋਸ਼)

    def gén_mots_intégrés(ਖੁਦ):
        return []

    def ਬਾਅਦ_ਕਾਰਵਾਈ(ਖੁਦ, ਦਸਤ, ਭਾਸ਼ਾ):
        return ਦਸਤ

    def ਰੁੱਖ_ਬਣਾਉ(ਖੁਦ, ਸੰ, ਭਾਸ਼ਾ=None):
        ਵਿਸ਼ਲੇਸ਼ਣ = ਖੁਦ.ਵਿਸ਼ਲੇਸ਼ਣ_ਪ੍ਰਾਪਤ_ਕਰਨਾ(ਭਾਸ਼ਾ)
        return ਵਿਸ਼ਲੇਸ਼ਣ.parse(ਸੰ)

    def ਸੰਕੇਤ_ਮੁੜ_ਉਸਾਰੀ(ਖੁਦ, ਰੁੱਖ, ਭਾਸ਼ਾ):
        ਮੁੜ_ਉਸਾਰੀ = ਖੁਦ.ਪ੍ਮੁੜ_ਉਸਾਰੀ_ਪ੍ਰਾਪਤ_ਕਰਨਾ(ਭਾਸ਼ਾ)

        ਮੁੜ_ਉਸਾਰੀ_ਬਦਲ = ਖੁਦ.ਮੁੜ_ਉਸਾਰੀ_ਬਦਲ.copy()
        try:
            postproc = ਖੁਦ.ਮੁੜ_ਉਸਾਰੀ_ਬਦਲ['postproc']
        except KeyError:
            postproc = None
        if len(ਖੁਦ.ਕੋਸ਼_ਵਿਆ):
            if len(ਖੁਦ.ਕੋਸ਼_ਵਿਆ[ਭਾਸ਼ਾ]['ਵੇਸ਼ੇਸ਼ ਸ਼ਬਦ']):
                postproc = proc_mots_spéciaux(ਖੁਦ.ਕੋਸ਼_ਵਿਆ[ਭਾਸ਼ਾ]['ਵੇਸ਼ੇਸ਼ ਸ਼ਬਦ']) * postproc

            chiffres = [ਖੁਦ.spéciaux[x] for x in ['ENT', 'DEC'] if x in ਖੁਦ.spéciaux]
            if len(chiffres):
                postproc = ਸੰਖਯਾ_ਅਨੁਵਾਦਵਾਲਾ(ਭਾਸ਼ਾ, chiffres) * postproc

        ਮੁੜ_ਉਸਾਰੀ_ਬਦਲ['postproc'] = postproc

        return ਖੁਦ.ਬਾਅਦ_ਕਾਰਵਾਈ(ਮੁੜ_ਉਸਾਰੀ.reconstruct(ਰੁੱਖ, **ਮੁੜ_ਉਸਾਰੀ_ਬਦਲ), ਭਾਸ਼ਾ)

    def ਦਸਤ_ਅਨੁ_ਪ੍ਰਾਪਤ_ਕਰਨਾ(ਖੁਦ, ਭਾਸ਼ਾ):
        try:
            ਕੋਸ਼_ਵਿਆ = ਖੁਦ.ਕੋਸ਼_ਵਿਆ[ਭਾਸ਼ਾ]
        except KeyError:
            if ਭਾਸ਼ਾ == ਖੁਦ.ਸਰੋਤ_ਭਾ:
                ਰਾਸਤਾ = ਖੁਦ.ਦਸਤ_ਸਰੋਤ_ਅਨੁ
                if not os.path.isfile(ਖੁਦ._ਰਾਸਤਾ_ਰਿਕਾਰਡ_ਬਣਾਉ(ਰਾਸਤਾ)):
                    return ਖੁਦ._ਦਸਤਾਵੇਜ਼_ਖੋਲ੍ਹਨਾ([ਖੁਦ.ਵਿਆ])
            else:
                ਰਾਸਤਾ = [ਖੁਦ.ਅਨੂ_ਰਾਸਤਾ, ਭਾਸ਼ਾ + '.json']

            ਕੋਸ਼_ਵਿਆ = ਖੁਦ._ਦਸਤਾਵੇਜ਼_ਖੋਲ੍ਹਨਾ(ਰਾਸਤਾ, ਜੇਸਾਨ_ਤੋਂ=True)  # type: dict
            ਖੁਦ.ਕੋਸ਼_ਵਿਆ[ਭਾਸ਼ਾ] = ਕੋਸ਼_ਵਿਆ

        return ''.join([x['ਅਨੁ'] if len(x['ਅਨੁ']) else x["ਸਰੋਤ"] for x in ਕੋਸ਼_ਵਿਆ['ਨਿਯਮ']])

    def ਵਿਸ਼ਲੇਸ਼ਣ_ਪ੍ਰਾਪਤ_ਕਰਨਾ(ਖੁਦ, ਭਾਸ਼ਾ):

        if ਭਾਸ਼ਾ not in ਖੁਦ._ਵਿਸ਼ਲੇਸ਼ਣ:
            ਖੁਦ._ਵਿਸ਼ਲੇਸ਼ਣ[ਭਾਸ਼ਾ] = Lark(ਖੁਦ.ਦਸਤ_ਅਨੁ_ਪ੍ਰਾਪਤ_ਕਰਨਾ(ਭਾਸ਼ਾ), **ਖੁਦ.ਸ਼ਬਦ_ਵਿਸ਼_ਬਦਲ)

        return ਖੁਦ._ਵਿਸ਼ਲੇਸ਼ਣ[ਭਾਸ਼ਾ]

    def ਪ੍ਮੁੜ_ਉਸਾਰੀ_ਪ੍ਰਾਪਤ_ਕਰਨਾ(ਖੁਦ, ਭਾਸ਼ਾ):
        if ਭਾਸ਼ਾ not in ਖੁਦ._ਮੁੜ_ਉਸਾਰੀ:
            ਖੁਦ._ਮੁੜ_ਉਸਾਰੀ[ਭਾਸ਼ਾ] = Reconstructor(ਖੁਦ.ਵਿਸ਼ਲੇਸ਼ਣ_ਪ੍ਰਾਪਤ_ਕਰਨਾ(ਭਾਸ਼ਾ))

        return ਖੁਦ._ਮੁੜ_ਉਸਾਰੀ[ਭਾਸ਼ਾ]

    def ਵਾਧਾ_ਪ੍ਰਾਪਤ_ਕਰਨਾ(ਖੁਦ, ਭਾਸ਼ਾ):
        return ਖੁਦ._ਦਸਤਾਵੇਜ਼_ਖੋਲ੍ਹਨਾ([ਖੁਦ.ਅਨੂ_ਰਾਸਤਾ, ਭਾਸ਼ਾ + '.json'], ਜੇਸਾਨ_ਤੋਂ=True)['ਵਾਧਾ']

    def ਵਾਧਾ_ਤੋਂ_ਭਾਸ਼ਾ(ਖੁਦ, ਵਾਧਾ):
        for ਦ in ਖੁਦ.ਅਨੂ_ਰਾਸਤਾ:
            if os.path.split(ਦ)[1] != ਖੁਦ.ਦਸਤ_ਸਰੋਤ_ਅਨੁ:
                ਕੋਸ਼ = ਖੁਦ._ਦਸਤਾਵੇਜ਼_ਖੋਲ੍ਹਨਾ(ਦ)
                if ਕੋਸ਼['ਵਾਧਾ'] == ਵਾਧਾ:
                    return ਕੋਸ਼['ਭਾਸ਼ਾ']
        raise ValueError

    def _ਰਾਸਤਾ_ਰਿਕਾਰਡ_ਬਣਾਉ(ਖੁਦ, ਰਾਸਤਾ):
        if isinstance(ਰਾਸਤਾ, list):
            ਰਾਸਤਾ = os.path.join(*ਰਾਸਤਾ)
        if not len(os.path.splitdrive(ਰਾਸਤਾ)[0]):
            ਰਾਸਤਾ = os.path.join(ਖੁਦ.ਰਾਸਤਾ, ਰਾਸਤਾ)

        return ਰਾਸਤਾ

    def _ਦਸਤਾਵੇਜ਼_ਲਿਖਣਾ(ਖੁਦ, ਰਾਸਤਾ, ਵਸਤੂ):
        ਰਾਸਤਾ = ਖੁਦ._ਰਾਸਤਾ_ਰਿਕਾਰਡ_ਬਣਾਉ(ਰਾਸਤਾ)
        if not os.path.isdir(os.path.split(ਰਾਸਤਾ)[0]):
            os.mkdir(os.path.split(ਰਾਸਤਾ)[0])
        with open(ਰਾਸਤਾ, 'w', encoding='UTF-8') as d:
            if isinstance(ਵਸਤੂ, dict):
                json.dump(ਵਸਤੂ, d, ensure_ascii=False, indent=2)
            elif isinstance(ਵਸਤੂ, list):
                d.writelines(ਵਸਤੂ)
            elif isinstance(ਵਸਤੂ, str):
                d.write(ਵਸਤੂ)
            else:
                raise TypeError

    def _ਦਸਤਾਵੇਜ਼_ਖੋਲ੍ਹਨਾ(ਖੁਦ, ਰਾਸਤਾ, ਜੇਸਾਨ_ਤੋਂ=False):
        """

        :param ਰਾਸਤਾ:
        :type ਰਾਸਤਾ:
        :param ਜੇਸਾਨ_ਤੋਂ:
        :type ਜੇਸਾਨ_ਤੋਂ:
        :return:
        :rtype: str | dict
        """
        ਰਾਸਤਾ = ਖੁਦ._ਰਾਸਤਾ_ਰਿਕਾਰਡ_ਬਣਾਉ(ਰਾਸਤਾ)
        with open(ਰਾਸਤਾ, encoding='UTF-8') as ਦ:
            if ਜੇਸਾਨ_ਤੋਂ:
                return json.load(ਦ)
            else:
                return ਦ.read()

    def ਸੰਕੇਤ_ਅਨੁਵਾਦ(ਖੁਦ, ਸੰ, ਭਾਸ਼ਾ, ਸਰੋਤ_ਭਾਸ਼ਾ=None):

        ਰੁੱਖ = ਖੁਦ.ਰੁੱਖ_ਬਣਾਉ(ਸੰ, ਸਰੋਤ_ਭਾਸ਼ਾ)
        ਮੁੜ_ਉਸਾਰੀ = ਖੁਦ.ਸੰਕੇਤ_ਮੁੜ_ਉਸਾਰੀ(ਰੁੱਖ, ਭਾਸ਼ਾ)

        return ਮੁੜ_ਉਸਾਰੀ

    def ਦਸਤਾਵੇਜ਼_ਅਨੁਵਾਦ(ਖੁਦ, f, ਭਾਸ਼ਾ, ਸਰੋਤ_ਭਾਸ਼ਾ=None):
        ਸੰ = ਖੁਦ._ਦਸਤਾਵੇਜ਼_ਖੋਲ੍ਹਨਾ(f)

        if ਸਰੋਤ_ਭਾਸ਼ਾ is None:
            ਸਰੋਤ_ਭਾਸ਼ਾ = ਖੁਦ.ਵਾਧਾ_ਤੋਂ_ਭਾਸ਼ਾ(os.path.splitext(f)[1])
        ਅਨੁ = ਖੁਦ.ਸੰਕੇਤ_ਅਨੁਵਾਦ(ਸੰ, ਭਾਸ਼ਾ, ਸਰੋਤ_ਭਾਸ਼ਾ)
        ਵਾਧਾ = ਖੁਦ.ਵਾਧਾ_ਪ੍ਰਾਪਤ_ਕਰਨਾ(ਭਾਸ਼ਾ)

        ਖੁਦ._ਦਸਤਾਵੇਜ਼_ਲਿਖਣਾ(os.path.splitext(f)[0] + ਵਾਧਾ, ਅਨੁ)
