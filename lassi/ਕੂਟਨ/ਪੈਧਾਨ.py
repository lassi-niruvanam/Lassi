import os
from warnings import warn as avertir


from lassi.ਕੂਟਨ.ਕੂਟਨ import ਕੂਟਨ_ਘਟ
import ast


class ਕੂਟਨ_ਪੈਧਾਨ(ਕੂਟਨ_ਘਟ):

    def _ਅਨੁਵਾਦ_ਲਿਖਣਾ(ਖੁਦ, ਰਾਸ੍ਤਾ, ਜ਼ਬਾਨ):
        ਕੂਟਨ_ਲਿਖਣਾ(dic=ਖੁਦ.ਕੋਸ਼, d_t=ਖੁਦ.ਕੋਸ਼_ਅਨੁ, ਰਾਸ੍ਤਾ=ਰਾਸ੍ਤਾ, ਜ਼ਬਾਨ=ਜ਼ਬਾਨ)

    def ਪਢਨਾ(ਖੁਦ):
        ਖੁਦ.ਕੋਸ਼.clear()
        ਖੁਦ.ਕੋਸ਼['ਪ੍ਰਕਾਰ'] = 'ਕੂਟਨ'
        ਖੁਦ.ਕੋਸ਼['ਸੱਮਗਰੀ'] = {}

        for ਰਾ, ਨਤ੍ਥੀ, ਦਸ੍ਤ in os.walk(ਖੁਦ.ਰਾਸ੍ਤਾ_ਪੂਰੀ):

            ਕੋਸ਼ = ਖੁਦ.ਕੋਸ਼['ਸੱਮਗਰੀ']
            chemin_rel = os.path.relpath(ਰਾ, ਖੁਦ.ਰਾਸ੍ਤਾ_ਪੂਰੀ)
            if any('.' in os.path.relpath(c, chemin_rel) for c in ਖੁਦ.ignore):
                continue
            for ਰ in ਰਾਸ੍ਤਾ_ਟੂਠਨਾ(chemin_rel):
                if ਰ != '.' and ਰ != '' and ਰ[0] != '_':
                    ਕੋਸ਼ = ਕੋਸ਼[ਰ]['ਸੱਮਗਰੀ']

            for ਨ in ਨਤ੍ਥੀ:
                if ਨ[0] != '_':
                    ਕੋਸ਼[ਨ] = {
                        'ਪ੍ਰਕਾਰ': 'ਨਤ੍ਥੀ', 'ਸੱਮਗਰੀ': {}
                    }
            for ਦ in ਦਸ੍ਤ:
                if (ਦ[0] != '_' or ਦ == '__init__.py') and os.path.splitext(ਦ)[1] == '.py':
                    ਸੱਮਗਰੀ = ਦਸ੍ਤ_ਸੱਮਗਰੀ_ਪਾਣਾ(ਦ, ਰਾ)
                    if len(ਸੱਮਗਰੀ):
                        ਕੋਸ਼[ਦ] = {
                            'ਪ੍ਰਕਾਰ': 'ਦਸ੍ਤ', 'ਸੱਮਗਰੀ': ਸੱਮਗਰੀ
                        }

def ਕੂਟਨ_ਲਿਖਣਾ(dic, d_t, ਰਾਸ੍ਤਾ, ਜ਼ਬਾਨ, ch=None):

    if ch is None:
        ch = []

    for ll, v in dic['ਸੱਮਗਰੀ'].items():
        ਪ੍ਰਕਾਰ = v['ਪ੍ਰਕਾਰ']
        n = v['code']
        ਨਾਮ = d_t[n][ਜ਼ਬਾਨ] if ਜ਼ਬਾਨ in d_t[n] and len(d_t[n]) else ll
        if ਪ੍ਰਕਾਰ == 'ਕੂਟਨ':
            pass
        elif ਪ੍ਰਕਾਰ == 'ਨਤ੍ਥੀ':
            ch.append(ਨਾਮ)
            ਕੂਟਨ_ਲਿਖਣਾ(dic=v, d_t=d_t, ਰਾਸ੍ਤਾ=ਰਾਸ੍ਤਾ, ਜ਼ਬਾਨ=ਜ਼ਬਾਨ, ch=ch)
            ch.pop()
        elif ਪ੍ਰਕਾਰ == 'ਦਸ੍ਤ':
            ch.append(ਨਾਮ)
            with open(os.path.join(ਰਾਸ੍ਤਾ, *ch), encoding='UTF8') as d:
                d.writelines(écrire_doc(dic=v, d_t=d_t, ਜ਼ਬਾਨ=ਜ਼ਬਾਨ))
            ch.pop()



        else:
            raise ValueError(''.format(ਪ੍ਰਕਾਰ))

def écrire_doc(dic, d_t, ਜ਼ਬਾਨ, l_f=None, ctx=None):

    if l_f is None:
        l_f = []

    for nom_orig, v in dic['ਸੱਮਗਰੀ'].items():
        ਪ੍ਰਕਾਰ = v['ਪ੍ਰਕਾਰ']
        n = v['code']
        ਨਾਮ = d_t[n][ਜ਼ਬਾਨ] if ਜ਼ਬਾਨ in d_t[n] and len(d_t[n]) else nom_orig

        if ਪ੍ਰਕਾਰ == 'classe':
            l_f.append('class {ਨਾਮ}({nom_orig}):'.format(ਨਾਮ=ਨਾਮ, nom_orig=nom_orig))
            écrire_doc(dic=v, d_t=d_t, ਜ਼ਬਾਨ=ਜ਼ਬਾਨ, l_f=l_f, ctx='classe')

        elif ਪ੍ਰਕਾਰ == 'fonction':
            t = '\t' * (1 if ctx == 'classe' else 0)
            params = NotImplemented
            l_f.append('{t}def {ਨਾਮ}({params}):'.format(t=t, ਨਾਮ=ਨਾਮ, params=params))

            params_conv = NotImplemented
            l_f.append('{t}{nom_orig}(params_conv)'.format(t=t+'\t', nom_orig=nom_orig, params_conv=params_conv))

        elif ਪ੍ਰਕਾਰ == 'param':
            pass  # Rien à faire

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

    with open(os.path.join(ਰਾਸ੍ਤਾ, ਦਸ੍ਤ), encoding='UTF8') as ਦ:
        try:
            obj_ast = ast.parse(ਦ.read())
        except:
            avertir(''.format(os.path.join(ਰਾਸ੍ਤਾ, ਦਸ੍ਤ)))
            return ਸੱਮਗਰੀ

    for o in obj_ast.body:
        if isinstance(o, ast.Import):
            name = o.names[0].name
            asname = o.names[0].asname
            ਸੱਮਗਰੀ[name if asname is None else asname] = {
                'ਪ੍ਰਕਾਰ': 'import',
                'ਸੱਮਗਰੀ': {},
                'parent': name

            }
        elif isinstance(o, ast.ImportFrom):
            mod = o.module
            name = o.names[0].name
            asname = o.names[0].asname

            ਸੱਮਗਰੀ[name if asname is None else asname] = {
                'ਪ੍ਰਕਾਰ': 'import',
                'ਸੱਮਗਰੀ': {},
                'parent': name,
                'mod': mod
            }

        elif isinstance(o, ast.ClassDef):
            name = o.name

            ਸੱਮਗਰੀ[name] = {
                'ਪ੍ਰਕਾਰ': 'classe',
                'ਸੱਮਗਰੀ': {}
            }
            for s_o in o.body:
                if isinstance(s_o, ast.FunctionDef):
                    lire_fonc(s_o, ਸੱਮਗਰੀ[name]['ਸੱਮਗਰੀ'])

        elif isinstance(o, ast.FunctionDef):
            lire_fonc(o, ਸੱਮਗਰੀ)

        elif isinstance(o, ast.Assign):
            cibles = o.targets
            for c in cibles:
                ਸੱਮਗਰੀ[c.id] = {
                    'ਪ੍ਰਕਾਰ': 'attr',
                    'ਸੱਮਗਰੀ': {}
                }
        elif isinstance(o, ast.Expr):
            pass
        else:
            avertir('{}'.format(type(o)))

    return ਸੱਮਗਰੀ


def lire_fonc(o, d):
    name = o.name
    args = o.args.args
    df = o.args.defaults
    d[name] = {
        'ਪ੍ਰਕਾਰ': 'fonction',
        'ਸੱਮਗਰੀ': {a.arg: {'ਪ੍ਰਕਾਰ': 'param'} if i < (len(args) - len(df))
            else {'ਪ੍ਰਕਾਰ': 'param', 'val': val(df[len(args) -1 - i])} for i, a in enumerate(args)}
    }

def val(o):
    if isinstance(o, ast.Num):
        return o.n
    elif isinstance(o, ast.Name):
        return o.id
    elif isinstance(o, ast.Str):
        return o.s
    elif isinstance(o, ast.NameConstant):
        return o.value
    elif isinstance(o, ast.Attribute):
        return
    elif isinstance(o, ast.Dict):
        raise NotImplementedError
    elif isinstance(o, ast.List):
        raise NotImplementedError
    elif isinstance(o, ast.ListComp):
        raise NotImplementedError
    elif isinstance(o, ast.DictComp):
        raise NotImplementedError
    elif isinstance(o, ast.Set):
        raise NotImplementedError
    elif isinstance(o, ast.SetComp):
        raise NotImplementedError
    else:
        raise TypeError(''.format(type(o)))

ਨਮੁਨਹ = ਕੂਟਨ_ਪੈਧਾਨ(ਕੂਟਨ_ਨਾਮ='tinamit', ਰਾਸ੍ਤਾ='C:\\Users\\USERS1\PycharmProjects\Tinamit',
                   ign=['Interfaz', 'Incertidumbre', 'Ejemplos'])
import pprint

pprint.pprint(ਨਮੁਨਹ.ਕੋਸ਼, indent=2)

ਨਮੁਨਹ.gén_dict_trads()

ਨਮੁਨਹ.ajouter_langue('தமிழ்')
ਨਮੁਨਹ.écire_dic_pour_trad()