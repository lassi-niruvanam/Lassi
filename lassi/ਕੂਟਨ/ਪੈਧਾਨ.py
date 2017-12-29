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
                if ਦ[0] != '_' or ਦ == '__init__.py' and os.path.splitext(ਦ)[1] == '.py':
                    ਸੱਮਗਰੀ = ਦਸ੍ਤ_ਸੱਮਗਰੀ_ਪਾਣਾ(ਦ, ਰਾ)
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
    re_val = r'(%s)|[\p{N}]+(\.?[\p{N}])?' % re_ident
    re_dict = r'\{[\s]*{id}[\s]*:[\s]*{vl}([\s]*,[\s]*{id}[\s]*:[\s]*{vl})*[\s]*,?[\s]*\}'
    re_ens = r'\{[\s]*{vl}([\s]*,[\s]*{vl})*[\s]*,?[\s]*\}'
    re_liste = r''
    re_appel_fonc = r''


    re_arg_val = r'({})[\s]*=[\s]*({})'.format(re_ident, re_val)
    re_args = r'\([\s]*({av}([\s]*,[\s]*{av})*)|({id}([\s]*,[\s]*{id})*)([\s]*,[\s]*{av})*[\s]*\)'.format(av=re_arg_val, id=re_ident)
    regex.match(re_args, '(ਰਾਸ੍ਤਾ=2):')
    regex.match(re_args, '(ਦਸ੍ਤ, ਰਾਸ੍ਤਾ=3):')
    regex.match(re_args, '(ਦਸ੍ਤ, ਰਾਸ੍ਤਾ):')
    re_func_comp = r'def[\s]+(?P<ਨਾਮ>{})[\s]*\([\s]*(?P<args>{})[\s]*\)[\s]*:'.format(re_ident, re_args)
    re_clase_comp = r'class[\s]+(?P<ਨਾਮ>{id})\([\s]*(?P<par>{id})[\s]*\)[\s]*:'.format(id=re_ident)

    re_no_term = r'.*\\'
    re_emp_decl = r'(def)|(class)[\s]+\('
    re_fin_decl = r'.*\)[\s]*:'

    s = 'def ਦਸ੍ਤਾ_ਸੱਮਗਰੀ_ਪਾਣਾ2੧੨(ਦਸ੍ਤ, ਰਾਸ੍ਤਾ=2):'
    s_emp = 'def ਦਸ੍ਤਾ_ਸੱਮਗਰੀ_ਪਾਣਾ2੧੨(ਦਸ੍ਤ,'
    # print(regex.fullmatch(re_func_comp, s).groupdict())
    # print(regex.fullmatch(re_func_emp, s_emp).groupdict())

    ਫ_ਦਸ੍ਤ = []
    with open(os.path.join(ਰਾਸ੍ਤਾ, ਦਸ੍ਤ), encoding='UTF8') as ਦ:
        ਰੇ = ਦ.readline().rstrip('\n ')

        while ਰੇ is not None:
            while regex.fullmatch(ਰੇ, re_no_term):
                ਰੇ += ' ' + ਦ.readline().rstrip('\n \\').lstrip('\t ')

            if regex.fullmatch(ਰੇ, re_emp_decl):
                while not regex.fullmatch(ਰੇ, re_fin_decl):
                    ਰੇ += ' ' + ਦ.readline().rstrip('\n \\').lstrip('\t ')

            ਫ_ਦਸ੍ਤ.append(ਰੇ)

            ਰੇ = ਦ.readline().rstrip('\n ')

    m = regex.fullmatch(ਰੇ, re_func_comp)
    if m:
        ਕੋਸ਼ = m.groupdict()
        ਸੱਮਗਰੀ[ਕੋਸ਼['ਨਾਮ']] = {
            'ਪ੍ਰਕਾਰ': 'fonction',
            'ਸੱਮਗਰੀ': {ਨ: {'ਪ੍ਰਕਾਰ': 'param', 'val': NotImplemented} for ਨ in ਕੋਸ਼['args']}
        }


    return ਸੱਮਗਰੀ


ਨਮੁਨਹ = ਕੂਟਨ_ਪੈਧਾਨ(ਕੂਟਨ_ਨਾਮ='tinamit', ਰਾਸ੍ਤਾ='C:\\Users\\USERS1\PycharmProjects\Tinamit')
import pprint

pprint.pprint(ਨਮੁਨਹ.ਕੋਸ਼, indent=2)
