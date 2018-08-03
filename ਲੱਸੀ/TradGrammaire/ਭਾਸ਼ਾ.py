import json
import os

from lark import Lark, Tree
from lark.reconstruct import Reconstructor

with open('../ਲਾਰਕ/ਲਾਰਕ.lark') as d:
    gram_lark = d.read()
ਵਿਸ਼ਲੇਸ਼ਣ = Lark(grammar=gram_lark, parser='lalr', lexer='contextual')


class ਵਿਆਕਰਣ_ਵਧਾ(object):
    ਵਿਆ = NotImplemented
    ਵਾਧਾ = NotImplemented
    ਸਰੋਤ_ਭਾ = NotImplemented

    ਸ਼ਬਦ_ਵਿਸ਼_ਬਦਲ = {'parser': 'lalr'}
    ਮੁੜ_ਉਸਾਰੀ_ਬਦਲ = {}

    doc_src_trads = './trads_g/_src.json'
    dir_trads = './trads_g'
    dir_comp = './comp'

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

    def ਬਾਅਦ_ਕਾਰਵਾਈ(ਖੁਦ, ਦਸਤ):
        return ਦਸਤ

    def créer_arbre(ਖੁਦ, c, langue=None):
        analyseur = ਖੁਦ.obt_analyseur(langue)
        return analyseur.parse(c)

    def reconstre_code(ਖੁਦ, arbre, langue):
        reconstr = ਖੁਦ.obt_reconstr(langue)
        return ਖੁਦ.ਬਾਅਦ_ਕਾਰਵਾਈ(reconstr.reconstruct(arbre, **ਖੁਦ.ਮੁੜ_ਉਸਾਰੀ_ਬਦਲ))

    def obt_doc_trad_gram(ਖੁਦ, langue):
        if langue == ਖੁਦ.ਸਰੋਤ_ਭਾ:
            return ਖੁਦ.ਵਿਆ

        if not os.path.isdir(ਖੁਦ.dir_comp):
            os.mkdir(ਖੁਦ.dir_comp)
        raise NotImplementedError

    def obt_analyseur(ਖੁਦ, langue):

        if langue not in ਖੁਦ.analyseurs:
            ਖੁਦ.analyseurs[langue] = Lark.open(ਖੁਦ.obt_doc_trad_gram(langue), **ਖੁਦ.ਸ਼ਬਦ_ਵਿਸ਼_ਬਦਲ)

        return ਖੁਦ.analyseurs[langue]

    def obt_reconstr(ਖੁਦ, langue):
        if langue not in ਖੁਦ.reconstr:
            ਖੁਦ.reconstr[langue] = Reconstructor(ਖੁਦ.obt_analyseur(langue))

        return ਖੁਦ.reconstr[langue]

    def obt_ext(ਖੁਦ, langue):
        with open(os.path.join(ਖੁਦ.dir_trads, langue + '.json')) as d:
            ਵਾਧਾ = json.load(d)['ਵਾਧਾ']
        return ਵਾਧਾ

    def langue_de_ext(ਖੁਦ, ext):
        for f in ਖੁਦ.dir_trads:
            if os.path.split(f)[1] != ਖੁਦ.doc_src_trads:
                with open(f) as d:
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
