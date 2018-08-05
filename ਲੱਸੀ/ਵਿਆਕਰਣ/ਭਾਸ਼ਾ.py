import json
import os

from lark import Lark, Tree
from lark.reconstruct import Reconstructor

from ਲੱਸੀ.ਵਿਆਕਰਣ.ਸੰਖਯਾ import ਸੰਖਯਾ_ਅਨੁਵਾਦਵਾਲਾ


class ਵਿਆਕਰਣ_ਵਾਧਾ(object):
    ਵਿਆ = NotImplemented
    ਵਾਧਾ = NotImplemented
    ਸਰੋਤ_ਭਾ = NotImplemented
    dir = NotImplemented

    ਸ਼ਬਦ_ਵਿਸ਼_ਬਦਲ = {'parser': 'lalr'}
    ਮੁੜ_ਉਸਾਰੀ_ਬਦਲ = {}

    doc_src_trads = 'ਵਿਆ_ਅਨੁ/_ਸਰੋਤ.json'
    dir_trads = 'ਵਿਆ_ਅਨੁ'
    dir_comp = 'ਸੰਕਲਿਤ'

    spéciaux = {}

    reconstr = {}
    analyseurs = {}

    def gén_arch_trads(ਥੁਦ):
        from ..ਵਾਧਾ.ਲਾਰਕ.ਵਿਆਕਰਣ import ਲਾਰਕ_ਵਿਆਕਰਣ
        with open(ਥੁਦ.ਵਿਆ, encoding='UTF-8') as ਦ:
            g = ਦ.read()
        ਰੁੱਖ = ਲਾਰਕ_ਵਿਆਕਰਣ().créer_arbre(g, langue='en')

        ਅਨੁ_ਕੋਸ਼ = {
            'ਵਾਧਾ': ਥੁਦ.ਵਾਧਾ,
            'ਸਰੋਤ_ਭਾ': ਥੁਦ.ਸਰੋਤ_ਭਾ,
            'ਨਿਯਮ': [
                {'ਸਰੋਤ': ਲਾਰਕ_ਵਿਆਕਰਣ().reconstre_code(ਅ, ਥੁਦ.ਸਰੋਤ_ਭਾ), 'ਅਨੁ': '', 'ਰੁਤਬਾ': 'ਕਰਨੀ ਹੈ'}
                for ਅ in ਰੁੱਖ.children if isinstance(ਅ, Tree)
            ]
        }

        if not os.path.isdir(os.path.dirname(ਥੁਦ.doc_src_trads)):
            os.makedirs(os.path.dirname(ਥੁਦ.doc_src_trads))
        with open(ਥੁਦ.doc_src_trads, mode='w', encoding='UTF-8') as ਦ:
            json.dump(ਅਨੁ_ਕੋਸ਼, ਦ, ensure_ascii=False, indent=2)

    def gén_trads(ਖੁਦ, langues):
        with open(ਖੁਦ.doc_src_trads, 'r', encoding='UTF-8') as d:
            dic_l = json.load(d)
        for l in langues:
            dic_l['ਭਾਸ਼ਾ'] = l
            with open(os.path.join(ਖੁਦ.dir_trads, l + '.json'), 'w', encoding='UTF-8') as d:
                json.dump(dic_l, d, ensure_ascii=False, indent=2)

    def ਬਾਅਦ_ਕਾਰਵਾਈ(ਖੁਦ, ਦਸਤ, ਭਾਸ਼ਾ):
        return ਦਸਤ

    def créer_arbre(ਖੁਦ, c, langue=None):
        analyseur = ਖੁਦ.obt_analyseur(langue)
        return analyseur.parse(c)

    def reconstre_code(ਖੁਦ, arbre, langue):
        reconstr = ਖੁਦ.obt_reconstr(langue)
        ਮੁੜ_ਉਸਾਰੀ_ਬਦਲ = ਖੁਦ.ਮੁੜ_ਉਸਾਰੀ_ਬਦਲ
        if 'postproc' not in ਮੁੜ_ਉਸਾਰੀ_ਬਦਲ:
            ਮੁੜ_ਉਸਾਰੀ_ਬਦਲ['postproc'] = None
        if 'ENT' in ਖੁਦ.spéciaux:
            ਮੁੜ_ਉਸਾਰੀ_ਬਦਲ['postproc'] = ਸੰਖਯਾ_ਅਨੁਵਾਦਵਾਲਾ(langue,  ਖੁਦ.spéciaux['ENT'], ਮੁੜ_ਉਸਾਰੀ_ਬਦਲ['postproc'])
        return ਖੁਦ.ਬਾਅਦ_ਕਾਰਵਾਈ(reconstr.reconstruct(arbre, **ਮੁੜ_ਉਸਾਰੀ_ਬਦਲ), langue)

    def obt_doc_trad_gram(ਖੁਦ, langue):
        if langue == ਖੁਦ.ਸਰੋਤ_ਭਾ:
            return ਖੁਦ.ਵਿਆ
        with open(os.path.join(ਖੁਦ.dir, ਖੁਦ.dir_trads, langue + '.json'), encoding='UTF-8') as d:
            spec_gram = json.load(d)
        if not os.path.isdir(os.path.join(ਖੁਦ.dir, ਖੁਦ.dir_comp)):
            os.mkdir(os.path.join(ਖੁਦ.dir, ਖੁਦ.dir_comp))
        with open(os.path.join(ਖੁਦ.dir, ਖੁਦ.dir_comp, langue + '.lark'), 'w', encoding='UTF-8') as d:
            d.writelines([x['ਅਨੁ'] if len(x['ਅਨੁ']) else x["ਸਰੋਤ"] for x in spec_gram['ਨਿਯਮ']])
        return os.path.join(ਖੁਦ.dir, ਖੁਦ.dir_comp, langue + '.lark')

    def obt_analyseur(ਖੁਦ, langue):

        if langue not in ਖੁਦ.analyseurs:
            ਖੁਦ.analyseurs[langue] = Lark.open(ਖੁਦ.obt_doc_trad_gram(langue), **ਖੁਦ.ਸ਼ਬਦ_ਵਿਸ਼_ਬਦਲ)

        return ਖੁਦ.analyseurs[langue]

    def obt_reconstr(ਖੁਦ, langue):
        if langue not in ਖੁਦ.reconstr:
            ਖੁਦ.reconstr[langue] = Reconstructor(ਖੁਦ.obt_analyseur(langue))

        return ਖੁਦ.reconstr[langue]

    def obt_ext(ਖੁਦ, langue):
        with open(os.path.join(ਖੁਦ.dir_trads, langue + '.json'), encoding='UTF-8') as d:
            ਵਾਧਾ = json.load(d)['ਵਾਧਾ']
        return ਵਾਧਾ

    def langue_de_ext(ਖੁਦ, ext):
        for f in ਖੁਦ.dir_trads:
            if os.path.split(f)[1] != ਖੁਦ.doc_src_trads:
                with open(f, encoding='UTF-8') as d:
                    dic = json.load(d)
                if dic['ਵਾਧਾ'] == ext:
                    return dic['ਭਾਸ਼ਾ']
        raise ValueError

    def traduire_code(ਖੁਦ, c, langue_finale, langue_orig=None):

        arbre = ਖੁਦ.créer_arbre(c, langue_orig)
        reconstre = ਖੁਦ.reconstre_code(arbre, langue_finale)

        return reconstre

    def traduire_document(ਖੁਦ, f, langue=None):
        with open(f, encoding='UTF-8') as d:
            c = d.read()
        if langue is None:
            langue = ਖੁਦ.langue_de_ext(os.path.splitext(f)[1])
        t = ਖੁਦ.traduire_code(c, langue)
        ਵਧਾ = ਖੁਦ.obt_ext(langue)
        with open(os.path.splitext(f) + ਵਧਾ, 'w', encoding='UTF-8') as d:
            d.write(t)
