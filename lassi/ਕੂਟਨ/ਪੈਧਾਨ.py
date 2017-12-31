import ast
import os
from warnings import warn as avertir

from lassi.ਕੂਟਨ.ਕੂਟਨ import ਕੂਟਨ_ਘਟ


class ਕੂਟਨ_ਪੈਧਾਨ(ਕੂਟਨ_ਘਟ):

    def _ਅਨੁਵਾਦ_ਲਿਖਣਾ(ਖੁਦ, ਰਾਸ੍ਤਾ, ਜ਼ਬਾਨ):
        ਕੂਟਨ_ਲਿਖਣਾ(dic=ਖੁਦ.ਕੋਸ਼, d_t=ਖੁਦ.ਕੋਸ਼_ਅਨੁ, ਰਾਸ੍ਤਾ=ਰਾਸ੍ਤਾ, ਜ਼ਬਾਨ=ਜ਼ਬਾਨ, pq=os.path.split(ਖੁਦ.ਰਾਸ੍ਤਾ_ਪੂਰੀ)[1])

    def ਪਢਨਾ(ਖੁਦ):
        ਖੁਦ.ਕੋਸ਼.clear()
        ਖੁਦ.ਕੋਸ਼['ਪ੍ਰਕਾਰ'] = 'ਕੂਟਨ'
        ਖੁਦ.ਕੋਸ਼['ਸੱਮਗਰੀ'] = {}

        for ਰਾ, ਨਤ੍ਥੀ, ਦਸ੍ਤ in os.walk(ਖੁਦ.ਰਾਸ੍ਤਾ_ਪੂਰੀ):

            ਕੋਸ਼ = ਖੁਦ.ਕੋਸ਼['ਸੱਮਗਰੀ']
            chemin_rel = os.path.relpath(ਰਾ, ਖੁਦ.ਰਾਸ੍ਤਾ_ਪੂਰੀ)
            if not vérifier(chemin_rel, ਖੁਦ.ignore):
                continue

            for ਰ in ਰਾਸ੍ਤਾ_ਟੂਠਨਾ(chemin_rel):
                if ਰ != '.' and ਰ != '' and ਰ[0] != '_':
                    ਕੋਸ਼ = ਕੋਸ਼[ਰ]['ਸੱਮਗਰੀ']

            for ਨ in ਨਤ੍ਥੀ:
                if ਨ[0] != '_' and vérifier(ਨ, ਖੁਦ.ignore):
                    ਕੋਸ਼[ਨ] = {
                        'ਪ੍ਰਕਾਰ': 'ਨਤ੍ਥੀ', 'ਸੱਮਗਰੀ': {}
                    }
            for ਦ in ਦਸ੍ਤ:
                if vérifier(ਦ, ਖੁਦ.ignore):
                    if (ਦ[0] != '_' or ਦ == '__init__.py') and os.path.splitext(ਦ)[1] == '.py':
                        ਸੱਮਗਰੀ = ਦਸ੍ਤ_ਸੱਮਗਰੀ_ਪਾਣਾ(ਦ, ਰਾ)
                        if len(ਸੱਮਗਰੀ):
                            ਕੋਸ਼[ਦ] = {
                                'ਪ੍ਰਕਾਰ': 'ਦਸ੍ਤ', 'ਸੱਮਗਰੀ': ਸੱਮਗਰੀ
                            }


def ਕੂਟਨ_ਲਿਖਣਾ(dic, d_t, ਰਾਸ੍ਤਾ, pq, ਜ਼ਬਾਨ, ch=None):
    if ch is None:
        ch = []

    for ll, v in dic['ਸੱਮਗਰੀ'].items():
        ਪ੍ਰਕਾਰ = v['ਪ੍ਰਕਾਰ']
        n = v['num']
        ਨਾਮ = d_t[n][ਜ਼ਬਾਨ] if ਜ਼ਬਾਨ in d_t[n] and len(d_t[n][ਜ਼ਬਾਨ]) else ll
        if ਪ੍ਰਕਾਰ == 'ਕੂਟਨ':
            pass
        elif ਪ੍ਰਕਾਰ == 'ਨਤ੍ਥੀ':
            ch.append(ਨਾਮ)
            ਕੂਟਨ_ਲਿਖਣਾ(dic=v, d_t=d_t, ਰਾਸ੍ਤਾ=ਰਾਸ੍ਤਾ, pq=pq, ਜ਼ਬਾਨ=ਜ਼ਬਾਨ, ch=ch)
            ch.pop()
        elif ਪ੍ਰਕਾਰ == 'ਦਸ੍ਤ':
            chemin = os.path.join(ਰਾਸ੍ਤਾ, *ch)
            if not os.path.isdir(chemin):
                os.makedirs(chemin)
            ch.append(ਨਾਮ)
            with open(os.path.join(ਰਾਸ੍ਤਾ, *ch), 'w', encoding='UTF8') as d:
                d.writelines('\n'.join(écrire_doc(dic=v, d_t=d_t, ਜ਼ਬਾਨ=ਜ਼ਬਾਨ, pq=pq, ch=ch)))
            ch.pop()
        else:
            raise ValueError(''.format(ਪ੍ਰਕਾਰ))


def écrire_doc(dic, d_t, ਜ਼ਬਾਨ, pq, ch, l_f=None, ctx=None):
    if l_f is None:
        l_f = []

    for nom_orig, v in dic['ਸੱਮਗਰੀ'].items():
        ਪ੍ਰਕਾਰ = v['ਪ੍ਰਕਾਰ']
        try:
            n = v['num']
        except KeyError:
            continue
        ਨਾਮ = d_t[n][ਜ਼ਬਾਨ] if ਜ਼ਬਾਨ in d_t[n] and len(d_t[n][ਜ਼ਬਾਨ]) else nom_orig

        if ਪ੍ਰਕਾਰ == 'classe':
            ch_imp = '.'.join([pq] + ch[:-1] + [ch[-1][:-3]])
            l_f.append('\n')
            l_f.insert(0, 'from {ch} import {nom_orig}'.format(ch=ch_imp, nom_orig=nom_orig))
            l_f.append('class {ਨਾਮ}({nom_orig}):'.format(ਨਾਮ=ਨਾਮ, nom_orig=nom_orig))
            écrire_doc(dic=v, d_t=d_t, ਜ਼ਬਾਨ=ਜ਼ਬਾਨ, ch=ch, l_f=l_f, pq=pq, ctx='classe')

        elif ਪ੍ਰਕਾਰ == 'fonction':
            t = '    ' * (1 if ctx == 'classe' else 0)
            if ctx != 'classe':
                ch_imp = '.'.join([pq] + ch[:-1] + [ch[-1][:-3]])
                l_f.insert(0, 'from {ch} import {nom_orig}'.format(ch=ch_imp, nom_orig=nom_orig))

            l_params = []
            for x, d_x in v['ਸੱਮਗਰੀ'].items():
                if d_x['ਪ੍ਰਕਾਰ'] == 'param':
                    if 'val' in d_x and d_x['val'] is not None:
                        if isinstance(d_x['val'], str):
                            l_params.append('{}="{}"'.format(x, d_x['val']))
                        else:
                            l_params.append('{}={}'.format(x, d_x['val']))
                    else:
                        l_params.append(x)

            params_conv = []
            for x, d_x in v['ਸੱਮਗਰੀ'].items():
                if d_x['ਪ੍ਰਕਾਰ'] == 'param':
                    n = d_x['num']
                    p = d_t[n][ਜ਼ਬਾਨ] if ਜ਼ਬਾਨ in d_t[n] and len(d_t[n][ਜ਼ਬਾਨ]) else x

                    if 'val' not in d_x or d_x['val'] is None:
                        params_conv.append(p)
                    else:
                        if isinstance(d_x['val'], str):
                            params_conv.append('{}="{}"'.format(p, d_x['val']))
                        else:
                            params_conv.append('{}={}'.format(p, d_x['val']))
            conv_params = []
            for x, d_x in v['ਸੱਮਗਰੀ'].items():
                if d_x['ਪ੍ਰਕਾਰ'] == 'param':
                    n = d_x['num']
                    p = d_t[n][ਜ਼ਬਾਨ] if ਜ਼ਬਾਨ in d_t[n] and len(d_t[n][ਜ਼ਬਾਨ]) else x
                    conv_params.append('{}={}'.format(x, p))
            if ctx == 'classe':
                l_f.append('')
                l_f.append('{t}def {ਨਾਮ}({params}):'.format(t=t, ਨਾਮ=ਨਾਮ, params=', '.join(params_conv)))
                if ਨਾਮ != '__init__':
                    l_f.append('{t}return {soi_même}.{nom_orig}({params_conv})'.format(
                        t=t + '    ', soi_même=params_conv[0], nom_orig=nom_orig, params_conv=', '.join(l_params[1:]))
                    )
                else:
                    l_f.append('{t}super().{nom_orig}({conv_params})'.format(
                        t=t + '    ', soi_même=params_conv[0], nom_orig=nom_orig, conv_params=', '.join(conv_params[1:]))
                    )
            else:
                l_f.append('\n')
                l_f.append('{t}def {ਨਾਮ}({params}):'.format(t=t, ਨਾਮ=ਨਾਮ, params=', '.join(params_conv)))
                l_f.append('{t}return {nom_orig}({conv_params})'.format(
                    t=t + '    ', nom_orig=nom_orig, conv_params=', '.join(conv_params))
                )

        elif ਪ੍ਰਕਾਰ == 'attr':
            t = '    ' * (1 if ctx == 'classe' else 0)
            if ctx != 'classe':
                l_f.append('')
                ch_imp = '.'.join([pq] + ch[:-1] + [ch[-1][:-3]])
                l_f.insert(0, 'from {ch} import {nom_orig}'.format(ch=ch_imp, nom_orig=nom_orig))
            l_f.append('{t}{ਨਾਮ} = {nom_orig}'.format(t=t, ਨਾਮ=ਨਾਮ, nom_orig=nom_orig))
        else:
            raise ValueError('{}'.format(ਪ੍ਰਕਾਰ))

        l_f.append('')
        return l_f


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
        except SyntaxError:
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
        else {'ਪ੍ਰਕਾਰ': 'param', 'val': val(df[len(args) - 1 - i])} for i, a in enumerate(args)}
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

def vérifier(obj, ignore):
    if any(len(os.path.commonpath((obj, c))) for c in ignore):
        return False
    else:
        return True