import ast
import os
from warnings import warn as avertir
from collections import OrderedDict

from lassi.ਕੂਟਨ.ਕੂਟਨ import ਕੂਟਨ


class ਕੂਟਨ_ਪੈਧਾਨ(ਕੂਟਨ):

    def _ਅਨੁਵਾਦ_ਲਿਖਣਾ(ਖੁਦ, ਮਾਰਗ, ਭਾਸ਼ਾ, ਕੋਸ਼_ਅਨੁ):
        ਕੂਟਨ_ਲਿਖਣਾ(dic=ਖੁਦ.ਕੋਸ਼, d_t=ਕੋਸ਼_ਅਨੁ, ਮਾਰਗ=ਮਾਰਗ, ਭਾਸ਼ਾ=ਭਾਸ਼ਾ, pq=os.path.split(ਖੁਦ.ਮਾਰਗ)[1])

    def ਪੜ੍ਹਨਾ(ਖੁਦ):
        ਖੁਦ.ਕੋਸ਼.clear()
        ਖੁਦ.ਕੋਸ਼['ਪ੍ਰਕਾਰ'] = 'ਕੂਟਨ'
        ਖੁਦ.ਕੋਸ਼['ਸੱਮਗਰੀ'] = OrderedDict()

        for ਮ, ਨਤ੍ਥੀ, ਦਸ੍ਤ in os.walk(ਖੁਦ.ਮਾਰਗ):

            ਕੋਸ਼ = ਖੁਦ.ਕੋਸ਼['ਸੱਮਗਰੀ']
            chemin_rel = os.path.relpath(ਮ, ਖੁਦ.ਮਾਰਗ)
            if not vérifier(chemin_rel, ਖੁਦ.ignore):
                continue

            for ਰ in ਮਾਰਗ_ਟੂਠਨਾ(chemin_rel):
                if ਰ != '.' and ਰ != '' and ਰ[0] != '_':
                    ਕੋਸ਼ = ਕੋਸ਼[ਰ]['ਸੱਮਗਰੀ']

            for ਨ in ਨਤ੍ਥੀ:
                if ਨ[0] != '_' and vérifier(ਨ, ਖੁਦ.ignore):
                    ਕੋਸ਼[ਨ] = {
                        'ਪ੍ਰਕਾਰ': 'ਨਤ੍ਥੀ', 'ਸੱਮਗਰੀ': OrderedDict()
                    }
            for ਦ in ਦਸ੍ਤ:
                if vérifier(ਦ, ਖੁਦ.ignore):
                    if (ਦ[0] != '_' or ਦ == '__init__.py') and os.path.splitext(ਦ)[1] == '.py':
                        ਸੱਮਗਰੀ = ਦਸ੍ਤ_ਸੱਮਗਰੀ_ਪਾਣਾ(ਦ, ਮ)
                        if len(ਸੱਮਗਰੀ):
                            ਕੋਸ਼[ਦ] = {
                                'ਪ੍ਰਕਾਰ': 'ਦਸ੍ਤ', 'ਸੱਮਗਰੀ': ਸੱਮਗਰੀ
                            }


def ਕੂਟਨ_ਲਿਖਣਾ(dic, d_t, ਮਾਰਗ, pq, ਭਾਸ਼ਾ, ch=None, ch_orig=None):
    if ch is None:
        ch = []
    if ch_orig is None:
        ch_orig = []

    for ll, v in dic['ਸੱਮਗਰੀ'].items():
        ਪ੍ਰਕਾਰ = v['ਪ੍ਰਕਾਰ']
        n = v['num']
        ਨਾਮ = d_t[n][ਭਾਸ਼ਾ] if ਭਾਸ਼ਾ in d_t[n] and len(d_t[n][ਭਾਸ਼ਾ]) else ll
        if ਪ੍ਰਕਾਰ == 'ਕੂਟਨ':
            pass
        elif ਪ੍ਰਕਾਰ == 'ਨਤ੍ਥੀ':
            ch.append(ਨਾਮ)
            ch_orig.append(ll)
            ਕੂਟਨ_ਲਿਖਣਾ(dic=v, d_t=d_t, ਮਾਰਗ=ਮਾਰਗ, pq=pq, ਭਾਸ਼ਾ=ਭਾਸ਼ਾ, ch=ch, ch_orig=ch_orig)
            ch.pop()
            ch_orig.pop()
        elif ਪ੍ਰਕਾਰ == 'ਦਸ੍ਤ':
            chemin = os.path.join(ਮਾਰਗ, *ch)
            if not os.path.isdir(chemin):
                os.makedirs(chemin)
            ch.append(ਨਾਮ)
            ch_orig.append(ll)
            with open(os.path.join(ਮਾਰਗ, *ch), 'w', encoding='UTF8') as d:
                d.writelines('\n'.join(écrire_doc(dic=v, d_t=d_t, ਭਾਸ਼ਾ=ਭਾਸ਼ਾ, pq=pq, ch=ch, ch_orig=ch_orig)))
            ch.pop()
            ch_orig.pop()
        else:
            raise ValueError(''.format(ਪ੍ਰਕਾਰ))


def écrire_doc(dic, d_t, ਭਾਸ਼ਾ, pq, ch, ch_orig, l_f=None, ctx=None):
    if l_f is None:
        l_f = []

    for nom_orig, v in dic['ਸੱਮਗਰੀ'].items():
        ਪ੍ਰਕਾਰ = v['ਪ੍ਰਕਾਰ']
        try:
            n = v['num']
        except KeyError:
            continue
        ਨਾਮ = d_t[n][ਭਾਸ਼ਾ] if ਭਾਸ਼ਾ in d_t[n] and len(d_t[n][ਭਾਸ਼ਾ]) else nom_orig

        if ਪ੍ਰਕਾਰ == 'classe':
            ch_imp = obt_ch_imp(pq, ch_orig)

            l_f.append('\n')
            l_f.insert(0, 'from {ch} import {nom_orig}'.format(ch=ch_imp, nom_orig=nom_orig))
            l_f.append('class {ਨਾਮ}({nom_orig}):'.format(ਨਾਮ=ਨਾਮ, nom_orig=nom_orig))
            écrire_doc(dic=v, d_t=d_t, ਭਾਸ਼ਾ=ਭਾਸ਼ਾ, ch=ch, l_f=l_f, pq=pq, ctx='classe', ch_orig=ch_orig)

        elif ਪ੍ਰਕਾਰ == 'fonction':
            t = '    ' * (1 if ctx == 'classe' else 0)
            if ctx != 'classe':
                ch_imp = obt_ch_imp(pq, ch_orig)
                l_f.insert(0, 'from {ch} import {nom_orig}'.format(ch=ch_imp, nom_orig=nom_orig))
                if ਨਾਮ == nom_orig:
                    continue

            l_params = []
            for x, d_x in v['ਸੱਮਗਰੀ'].items():
                if d_x['ਪ੍ਰਕਾਰ'] == 'param':
                    if 'val' in d_x:
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
                    p = d_t[n][ਭਾਸ਼ਾ] if ਭਾਸ਼ਾ in d_t[n] and len(d_t[n][ਭਾਸ਼ਾ]) else x

                    if 'val' not in d_x:
                        params_conv.append(p)
                    else:
                        if isinstance(d_x['val'], str):
                            params_conv.append('{}="{}"'.format(p, d_x['val']))
                        else:
                            params_conv.append('{}={}'.format(p, d_x['val']))
            paráms_val = [x for x in params_conv if '=' in x]
            paráms_sin_val = [x for x in params_conv if x not in paráms_val]
            params_conv = paráms_sin_val + paráms_val

            conv_params = []
            for x, d_x in v['ਸੱਮਗਰੀ'].items():
                if d_x['ਪ੍ਰਕਾਰ'] == 'param':
                    n = d_x['num']
                    p = d_t[n][ਭਾਸ਼ਾ] if ਭਾਸ਼ਾ in d_t[n] and len(d_t[n][ਭਾਸ਼ਾ]) else x
                    conv_params.append('{}={}'.format(x, p))
            if ctx == 'classe':
                l_f.append('')
                l_f.append('{t}def {ਨਾਮ}({params}):'.format(t=t, ਨਾਮ=ਨਾਮ, params=', '.join(params_conv)))
                if ਨਾਮ != '__init__':
                    if ਨਾਮ == nom_orig:
                        soi_même = 'super()'

                    else:
                        soi_même = params_conv[0]
                    l_f.append('{t}return {soi_même}.{nom_orig}({conv_params})'.format(
                        t=t + '    ', soi_même=soi_même, nom_orig=nom_orig,
                        conv_params=', '.join(conv_params[1:]))
                    )
                else:
                    l_f.append('{t}super().{nom_orig}({conv_params})'.format(
                        t=t + '    ', soi_même=params_conv[0], nom_orig=nom_orig,
                        conv_params=', '.join(conv_params[1:]))
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
                ch_imp = obt_ch_imp(pq, ch_orig)
                l_f.insert(0, 'from {ch} import {nom_orig}'.format(ch=ch_imp, nom_orig=nom_orig))
            l_f.append('{t}{ਨਾਮ} = {nom_orig}'.format(t=t, ਨਾਮ=ਨਾਮ, nom_orig=nom_orig))
        else:
            raise ValueError('{}'.format(ਪ੍ਰਕਾਰ))

    if ctx != 'classe':
        l_f.append('')
    return l_f


def ਮਾਰਗ_ਟੂਠਨਾ(ਮਾਰਗ, ਫ=None):
    if ਫ is None:
        ਫ = []
    ਟੂਠੀ = os.path.split(ਮਾਰਗ)
    ਫ.insert(0, ਟੂਠੀ[1])
    if len(ਟੂਠੀ[0]):
        ਮਾਰਗ_ਟੂਠਨਾ(ਟੂਠੀ[0], ਫ=ਫ)

    return ਫ


def ਦਸ੍ਤ_ਸੱਮਗਰੀ_ਪਾਣਾ(ਦਸ੍ਤ, ਮਾਰਗ):
    ਸੱਮਗਰੀ = OrderedDict()

    with open(os.path.join(ਮਾਰਗ, ਦਸ੍ਤ), encoding='UTF8') as ਦ:
        try:
            obj_ast = ast.parse(ਦ.read())
        except SyntaxError:
            avertir(''.format(os.path.join(ਮਾਰਗ, ਦਸ੍ਤ)))
            return ਸੱਮਗਰੀ

    for o in obj_ast.body:
        if isinstance(o, ast.Import):
            name = o.names[0].name
            asname = o.names[0].asname
            ਸੱਮਗਰੀ[name if asname is None else asname] = {
                'ਪ੍ਰਕਾਰ': 'import',
                'ਸੱਮਗਰੀ': OrderedDict(),
                'parent': name

            }
        elif isinstance(o, ast.ImportFrom):
            mod = o.module
            name = o.names[0].name
            asname = o.names[0].asname

            ਸੱਮਗਰੀ[name if asname is None else asname] = {
                'ਪ੍ਰਕਾਰ': 'import',
                'ਸੱਮਗਰੀ': OrderedDict(),
                'parent': name,
                'mod': mod
            }

        elif isinstance(o, ast.ClassDef):
            name = o.name

            ਸੱਮਗਰੀ[name] = {
                'ਪ੍ਰਕਾਰ': 'classe',
                'ਸੱਮਗਰੀ': OrderedDict()
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
                    'ਸੱਮਗਰੀ': OrderedDict()
                }
        elif isinstance(o, ast.Expr):
            pass
        else:
            avertir('{}'.format(type(o)))

    return ਸੱਮਗਰੀ


def lire_fonc(o, d):
    name = o.name
    if name[0] == '_' and not (name[:1] == '__' and name[-2:] == '__'):
        return
    args = o.args.args
    df = o.args.defaults
    d[name] = {
        'ਪ੍ਰਕਾਰ': 'fonction',
        'ਸੱਮਗਰੀ': OrderedDict(
            {a.arg: {'ਪ੍ਰਕਾਰ': 'param'} if i < (len(args) - len(df)) else
            {'ਪ੍ਰਕਾਰ': 'param', 'val': val(df[i - (len(args) - len(df))])} for i, a in enumerate(args)}
        )
    }


def val(o, depurar=True):
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
        if depurar:
            avertir('{}'.format(type(o)))
        else:
            raise TypeError(''.format(type(o)))


def vérifier(obj, ignore):
    if any(len(os.path.commonpath((obj, c))) for c in ignore):
        return False
    else:
        return True


def obt_ch_imp(pq, ch_orig):
    ch = '.'.join([pq] + ch_orig[:-1] + [ch_orig[-1][:-3]])
    if ch.rsplit('.')[1] == '__init__':
        ch = ch.rsplit('.')[0]
    return ch
