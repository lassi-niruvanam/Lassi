import json
import os

from lark import Lark, Transformer
from lark.reconstruct import Reconstructor

with open('../ਲਾਰਕ/ਲਾਰਕ.lark') as d:
    gram_lark = d.read()
anlzr = Lark(grammar=gram_lark, parser='lalr', lexer='contextual')
reconstr = Reconstructor(anlzr)


class à_txt(Transformer):
    @staticmethod
    def rule(x):
        return str(x[0])

    @staticmethod
    def name(x):
        return str(x[0])

    @staticmethod
    def alias(x):
        return x[0] + ' -> ' + x[1]

    @staticmethod
    def literal(x):
        return str(x[0])

    @staticmethod
    def expansions(x):
        return '\n\t|'.join(x)

    @staticmethod
    def expansion(x):
        return ' '.join(x)

    @staticmethod
    def expr(x):
        return ''.join(x)

    @staticmethod
    def maybe(x):
        return '[' + x[0] + ']'


class ExtGrammaire(object):
    gram = NotImplemented
    ext = NotImplemented
    langue_orig = NotImplemented
    arch_trads = './trads_g/trads.json'
    dir_trads = './trads_g'

    def gén_arch_trads(soimême):

        with open(soimême.gram, encoding='UTF-8') as d:
            g = d.read()
        arbre = anlzr.parse(g)

        règles = {
            x.children[0].value: à_txt().transform(x.children[1]) for x in arbre.children if x.data == 'rule'
        }
        d_trads = {
            'ext': soimême.ext,
            'langue': soimême.langue_orig,
            'règles': règles
        }
        with open(soimême.arch_trads, mode='w', encoding='UTF-8') as d:
            json.dump(d_trads, d, ensure_ascii=False, indent=2)
    def gén_trads(soimême, langues):
        with open(soimême.arch_trads, 'r', encoding='UTF-8') as d:
            dic_l = json.load(d)
        for l in langues:
            dic_l['langue'] = l
            with open(os.path.join(soimême.dir_trads, l + '.json'), 'w', encoding='UTF-8') as d:
                json.dump(dic_l, d, ensure_ascii=False, indent=2)

