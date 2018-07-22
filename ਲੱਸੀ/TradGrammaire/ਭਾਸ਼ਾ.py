import json
import os

from lark import Lark
from lark.reconstruct import Reconstructor

with open('../ਲਾਰਕ/ਲਾਰਕ.lark') as d:
    gram_lark = d.read()
anlzr = Lark(grammar=gram_lark, parser='lalr', lexer='contextual')
reconstr = Reconstructor(anlzr)


class ExtGrammaire(object):
    gram = NotImplemented
    ext = NotImplemented
    langue_orig = NotImplemented
    arch_trads = './trads_g/_src.json'
    dir_trads = './trads_g'

    def gén_arch_trads(soimême):

        with open(soimême.gram, encoding='UTF-8') as d:
            g = d.read()
        arbre = anlzr.parse(g)

        d_trads = {
            'ext': soimême.ext,
            'langue': soimême.langue_orig,
            'règles': [{'orig': reconstr.reconstruct(x), 'trad': '', 'status': 'à faire'} for x in arbre.children]
        }

        if not os.path.isdir(os.path.dirname(soimême.arch_trads)):
            os.makedirs(os.path.dirname(soimême.arch_trads))
        with open(soimême.arch_trads, mode='w', encoding='UTF-8') as d:
            json.dump(d_trads, d, ensure_ascii=False, indent=2)

    def gén_trads(soimême, langues):
        with open(soimême.arch_trads, 'r', encoding='UTF-8') as d:
            dic_l = json.load(d)
        for l in langues:
            dic_l['langue'] = l
            with open(os.path.join(soimême.dir_trads, l + '.json'), 'w', encoding='UTF-8') as d:
                json.dump(dic_l, d, ensure_ascii=False, indent=2)

