import site as ਜਗਹ
import os
import json
import random
from collections import OrderedDict
from types import ModuleType

from lassi.ਕੂਟਨ.ਪੈਧਾਨ import ਕੂਟਨ_ਪੈਧਾਨ


class ਕਾਰ੍ਯਕ੍ਰਮ(object):
    def __init__(ਖੁਦ, ਮਾਰਗ, ਕੂਟਨ_ਭਾਸ਼ਾ='ਪੈਥਾਨ'):

        if os.path.split(ਮਾਰਗ)[1] == '.config.json':
            ਖੁਦ.chemin_config = ਮਾਰਗ
            ਖੁਦ.chemin = os.path.split(ਮਾਰਗ)[0]
        else:
            ਖੁਦ.chemin_config = os.path.join(ਮਾਰਗ, '.config.json')
            ਖੁਦ.chemin = ਮਾਰਗ

        try:
            doc = _lire_json(ਖੁਦ.chemin_config)
        except FileNotFoundError:
            raise FileNotFoundError('{}'.format(ਖੁਦ.chemin_config))

        ਖੁਦ.ਖੁਦ_ਭਾਸ਼ਾ = doc['langue']
        ਖੁਦ.ਲੋੜੀਦਾ_ਭਾਸ਼ਾਵਾਂ = doc['ਲੋੜੀਦਾ_ਭਾਸ਼ਾਵਾਂ']
        ਖੁਦ.chemin_code_source = doc['chemin_code_source']
        ਖੁਦ.chemin_trads = doc['chemin_trads']
        ਖੁਦ.ignore = doc['ignore']

        ਖੁਦ.perdues = []
        
        try:
            ਖੁਦ.ਕੋਸ਼_ਅਨੁ = _lire_json(os.path.join(ਖੁਦ.chemin, 'ਅਨੁ.json'))
            for langue in ਖੁਦ.ਲੋੜੀਦਾ_ਭਾਸ਼ਾਵਾਂ:
                for ll, v in ਖੁਦ.ਕੋਸ਼_ਅਨੁ.items():
                    if langue not in v:
                        v[langue] = ''

        except FileNotFoundError:
            ਖੁਦ.ਕੋਸ਼_ਅਨੁ = {}
            
        try:
            ਖੁਦ.struct = _lire_json(os.path.join(ਖੁਦ.chemin, '.struct.json'))
        except FileNotFoundError:
            ਖੁਦ.struct = {'ਸੱਮਗਰੀ': OrderedDict(),
                          'ਪ੍ਰਕਾਰ': 'ਕੂਟਨ'}
            
        if ਕੂਟਨ_ਭਾਸ਼ਾ == 'ਪੈਥਾਨ':
            ਖੁਦ.ਕੂਟਨ = ਕੂਟਨ_ਪੈਧਾਨ(ਮਾਰਗ=ਖੁਦ.chemin_code_source, ਖੁਦ_ਭਾਸ਼ਾ=ਖੁਦ.ਖੁਦ_ਭਾਸ਼ਾ, ign=ਖੁਦ.ignore)
        else:
            raise ValueError('')

    def écrire_config(ਖੁਦ):
        dic = {
            'langue': ਖੁਦ.ਖੁਦ_ਭਾਸ਼ਾ,
            'ਲੋੜੀਦਾ_ਭਾਸ਼ਾਵਾਂ': ਖੁਦ.ਲੋੜੀਦਾ_ਭਾਸ਼ਾਵਾਂ,
            'chemin_code_source': ਖੁਦ.chemin_code_source,
            'chemin_trads': ਖੁਦ.chemin_trads,
            'ignore': ਖੁਦ.ignore
        }

        _écrire_json(dic=dic, doc=ਖੁਦ.chemin_config)
        
    def écrire_dic_trads(ਖੁਦ):
        _écrire_json(ਖੁਦ.ਕੋਸ਼_ਅਨੁ, os.path.join(ਖੁਦ.chemin, 'ਅਨੁ.json'))
        
    def écrire_dic_struct(ਖੁਦ):
        _écrire_json(ਖੁਦ.struct, os.path.join(ਖੁਦ.chemin, '.struct.json'))
    
    def sauvegarder(ਖੁਦ):
        ਖੁਦ.écrire_config()
        ਖੁਦ.écrire_dic_trads()
        ਖੁਦ.écrire_dic_struct()

    def ਭਾਸ਼ਾਵਾਂ_ਜੋੜਨਾ(ਖੁਦ, ਭਾਸ਼ਾਵਾਂ):
        if not isinstance(ਭਾਸ਼ਾਵਾਂ, list):
            ਭਾਸ਼ਾਵਾਂ = [ਭਾਸ਼ਾਵਾਂ]

        for ਭਾਸ਼ਾ in ਭਾਸ਼ਾਵਾਂ:
            if ਭਾਸ਼ਾ not in ਖੁਦ.ਲੋੜੀਦਾ_ਭਾਸ਼ਾਵਾਂ:
                ਖੁਦ.ਲੋੜੀਦਾ_ਭਾਸ਼ਾਵਾਂ.append(ਭਾਸ਼ਾ)

                for ਕੁੰ, ਮੁ in ਖੁਦ.ਕੋਸ਼_ਅਨੁ.items():
                    if ਭਾਸ਼ਾ not in ਮੁ:
                        ਮੁ[ਭਾਸ਼ਾ] = ''

    def actualiser(ਖੁਦ):

        perdues, nouvelles = mettre_struct_à_jour(ਖੁਦ.struct, ਖੁਦ.ਕੂਟਨ.ਕੋਸ਼)
        ਖੁਦ.perdues.append(perdues)

        ਖੁਦ.d_lin = {}

        lin_dic(ਖੁਦ.struct, d_l=ਖੁਦ.d_lin)
        ਖੁਦ.ਕੂਟਨ.ਕੋਸ਼ = ਖੁਦ.struct

        ਕੋਸ਼_ਅਨੁ = {ll: {ਖੁਦ.ਖੁਦ_ਭਾਸ਼ਾ: v['ਨਾਮ']} for ll, v in ਖੁਦ.d_lin.items()}

        mettre_trad_à_jour(ਖੁਦ.ਕੋਸ਼_ਅਨੁ, ਕੋਸ਼_ਅਨੁ)

        for v in ਖੁਦ.ਕੋਸ਼_ਅਨੁ.values():
            for l in ਖੁਦ.ਲੋੜੀਦਾ_ਭਾਸ਼ਾਵਾਂ:
                if l not in v:
                    v[l] = ''

    def ਅਨੁਵਾਦ_ਲਿਖਣਾ(ਖੁਦ, langues=None):
        ਖੁਦ.ਕੋਸ਼_ਅਨੁ.clear()
        ਖੁਦ.ਕੋਸ਼_ਅਨੁ.update(_lire_json(os.path.join(ਖੁਦ.chemin, 'ਅਨੁ.json')))
        if langues is None:
            langues = ਖੁਦ.ਲੋੜੀਦਾ_ਭਾਸ਼ਾਵਾਂ

        ਖੁਦ.ਕੂਟਨ.ਅਨੁਵਾਦ_ਲਿਖਣਾ(ਭਾਸ਼ਾ=langues, ਮਾਰਗ=ਖੁਦ.chemin_trads, ਕੋਸ਼_ਅਨੁ=ਖੁਦ.ਕੋਸ਼_ਅਨੁ)


def ਕਰ੍ਯਕ੍ਰਮ_ਬਣਾਊ(chemin, ਖੁਦ_ਭਾਸ਼ਾ, langues_cibles=None, chemin_code_source=None, chemin_trads='ਅਨੁ', ign=None):
    if isinstance(chemin, ModuleType):
        chemin = os.path.split(os.path.split(chemin.__file__)[0])[0]
    if os.path.split(chemin)[0] == '':
        for ਜ in ਜਗਹ.getsitepackages():
            if os.path.isdir(os.path.join(ਜ, chemin)):
                chemin = os.path.join(ਜ, chemin)
                break

    if langues_cibles is None:
        langues_cibles = []
    if not isinstance(langues_cibles, list):
        langues_cibles = [langues_cibles]

    if chemin_code_source is None:
        nom = os.path.split(chemin)[1]
        if os.path.isdir(os.path.join(chemin, nom)):
            chemin_code_source = os.path.join(chemin, nom)
        else:
            chemin_code_source = chemin

    if ign is None:
        ign = []

    if chemin_trads not in ign:
        ign.append(chemin_trads)

    if os.path.splitdrive(chemin_trads)[0] == '':
        chemin = os.path.join(chemin, chemin_trads)
        chemin_trads = os.path.join(chemin_code_source, chemin_trads)

    dic_config = {
        'langue': ਖੁਦ_ਭਾਸ਼ਾ,
        'ਲੋੜੀਦਾ_ਭਾਸ਼ਾਵਾਂ': langues_cibles,
        'chemin_code_source': chemin_code_source,
        'chemin_trads': chemin_trads,
        'ignore': [] if ign is None else ign
    }

    _écrire_json(dic_config, os.path.join(chemin, '.config.json'))
    
    return ਕਾਰ੍ਯਕ੍ਰਮ(ਮਾਰਗ=chemin)


def mettre_struct_à_jour(d_o, d_n, p=None, n=None):
    if p is None:
        p = []
        _obt_perdues(d_o=d_o, d_n=d_n, p=p)

    if n is None:
        n = []
    for ll in list(d_o.keys()):
        if ll not in d_n and ll != 'num':
            d_o.pop(ll)
    for ll, v in d_n.items():
        if ll not in ['ਸੱਮਗਰੀ', 'num']:
            d_o[ll] = v

    if 'ਸੱਮਗਰੀ' in d_n:
        for ll, v in d_n['ਸੱਮਗਰੀ'].items():
            if ll not in d_o['ਸੱਮਗਰੀ']:
                d_o['ਸੱਮਗਰੀ'][ll] = v
                n.append(v)
            else:
                mettre_struct_à_jour(d_o=d_o['ਸੱਮਗਰੀ'][ll], d_n=v, p=p, n=n)

    return p, n


def mettre_trad_à_jour(d1, d2):
    for ll, v in d2.items():
        if ll not in d1:
            d1[ll] = v


def _obt_perdues(d_o, d_n, p):
    if 'ਸੱਮਗਰੀ' in d_o:
        for ll in list(d_o['ਸੱਮਗਰੀ'].keys()):
            if ll not in d_n['ਸੱਮਗਰੀ']:
                p.append(d_o['ਸੱਮਗਰੀ'][ll])
                d_o['ਸੱਮਗਰੀ'].pop(ll)
            else:
                _obt_perdues(d_o=d_o['ਸੱਮਗਰੀ'][ll], d_n=d_n['ਸੱਮਗਰੀ'][ll], p=p)


def _écrire_json(dic, doc):
    if not os.path.isdir(os.path.split(doc)[0]):
        os.makedirs(os.path.split(doc)[0])

    with open(doc, 'w', encoding='utf8') as d:
        json.dump(dic, d, ensure_ascii=False, sort_keys=False, indent=2)


def _lire_json(doc, ordre=False):
    with open(doc, encoding='utf8') as d:
        if ordre:
            return json.load(d, object_pairs_hook=OrderedDict)
        else:
            return json.load(d)


def lin_dic(d, d_l, p=None):
    if p is None:
        p = []

    if 'ਸੱਮਗਰੀ' in d:
        for ll, v in d['ਸੱਮਗਰੀ'].items():
            ਪ੍ਰਕਾਰ = v['ਪ੍ਰਕਾਰ']
            if ਪ੍ਰਕਾਰ == 'import':
                continue

            nouv = {'ਨਾਮ': ll, 'ਪ੍ਰਕਾਰ': v['ਪ੍ਰਕਾਰ'], 'ਜਗਾਹ': p.copy()}
            if 'num' not in v:
                n = gén_nombre(n_c=8, interdits=d_l.keys())
                v['num'] = n
            else:
                n = v['num']
            d_l[n] = nouv

            p.append(ll)

            lin_dic(d=v, d_l=d_l, p=p)

            p.pop()


def gén_nombre(n_c, interdits):
    máx = 10 ** n_c
    if len(set(interdits)) >= máx:
        raise ValueError

    m = random.randint(0, máx)

    while str(m) in interdits or m in interdits:
        m = random.randint(0, máx)

    return str(m)