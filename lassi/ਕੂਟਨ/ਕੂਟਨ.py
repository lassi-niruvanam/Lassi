import os
import json
import shutil

from lassi.ਭਾਸ਼ਾਵਾਂ import ਭਾਸ਼ਾਵਾਂ


class ਕੂਟਨ(object):
    def __init__(ਖੁਦ, ਮਾਰਗ, ਖੁਦ_ਭਾਸ਼ਾ, ign):

        ਖੁਦ.ਮਾਰਗ = ਮਾਰਗ

        ਖੁਦ.ignore = ign

        ਖੁਦ.ਖੁਦ_ਭਾਸ਼ਾ = ਖੁਦ_ਭਾਸ਼ਾ

        ਖੁਦ.ਕੋਸ਼ = {}

        ਖੁਦ.ਪੜ੍ਹਨਾ()

    def ਪੜ੍ਹਨਾ(ਖੁਦ):
        raise NotImplementedError

    def ਅਨੁਵਾਦ_ਲਿਖਣਾ(ਖੁਦ, ਭਾਸ਼ਾ, ਮਾਰਗ, ਕੋਸ਼_ਅਨੁ):

        if not isinstance(ਭਾਸ਼ਾ, list):
            ਭਾਸ਼ਾ = [ਭਾਸ਼ਾ]

        for ਜ਼ in ਭਾਸ਼ਾ:
            code = ਭਾਸ਼ਾਵਾਂ[ਜ਼]['code']
            ਮਾਰਗ_ਜ਼ = os.path.join(ਮਾਰਗ, code)

            if os.path.isdir(ਮਾਰਗ_ਜ਼):
                shutil.rmtree(ਮਾਰਗ_ਜ਼)
            ਖੁਦ._ਅਨੁਵਾਦ_ਲਿਖਣਾ(ਮਾਰਗ=ਮਾਰਗ_ਜ਼, ਭਾਸ਼ਾ=ਜ਼, ਕੋਸ਼_ਅਨੁ=ਕੋਸ਼_ਅਨੁ)

    def _ਅਨੁਵਾਦ_ਲਿਖਣਾ(ਖੁਦ, ਮਾਰਗ, ਭਾਸ਼ਾ, ਕੋਸ਼_ਅਨੁ):
        raise NotImplementedError


def écrire_json(dic, doc):
    if not os.path.isdir(os.path.split(doc)[0]):
        os.makedirs(os.path.split(doc)[0])

    with open(doc, 'w', encoding='utf8') as d:
        json.dump(dic, d, ensure_ascii=False, sort_keys=True, indent=2)
