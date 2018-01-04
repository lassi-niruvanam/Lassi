import os
import json
import shutil

from lassi.ਜ਼ਬਾਨੋਂ import ਜ਼ਬਾਨੋਂ


class ਕੂਟਨ(object):
    def __init__(ਖੁਦ, ਰਾਸ੍ਤਾ, ਖੁਦ_ਜ਼ਬਾਨ, ign):

        ਖੁਦ.ਰਾਸ੍ਤਾ = ਰਾਸ੍ਤਾ

        ਖੁਦ.ignore = ign

        ਖੁਦ.ਖੁਦ_ਜ਼ਬਾਨ = ਖੁਦ_ਜ਼ਬਾਨ

        ਖੁਦ.ਕੋਸ਼ = {}

        ਖੁਦ.ਪਢਨਾ()

    def ਪਢਨਾ(ਖੁਦ):
        raise NotImplementedError

    def ਅਨੁਵਾਦ_ਲਿਖਣਾ(ਖੁਦ, ਜ਼ਬਾਨ, ਰਾਸ੍ਤਾ, ਕੋਸ਼_ਅਨੁ):

        if not isinstance(ਜ਼ਬਾਨ, list):
            ਜ਼ਬਾਨ = [ਜ਼ਬਾਨ]

        for ਜ਼ in ਜ਼ਬਾਨ:
            code = ਜ਼ਬਾਨੋਂ[ਜ਼]['code']
            ਰਾਸ੍ਤਾ_ਜ਼ = os.path.join(ਰਾਸ੍ਤਾ, code)

            if os.path.isdir(ਰਾਸ੍ਤਾ_ਜ਼):
                shutil.rmtree(ਰਾਸ੍ਤਾ_ਜ਼)
            ਖੁਦ._ਅਨੁਵਾਦ_ਲਿਖਣਾ(ਰਾਸ੍ਤਾ=ਰਾਸ੍ਤਾ_ਜ਼, ਜ਼ਬਾਨ=ਜ਼, ਕੋਸ਼_ਅਨੁ=ਕੋਸ਼_ਅਨੁ)

    def _ਅਨੁਵਾਦ_ਲਿਖਣਾ(ਖੁਦ, ਰਾਸ੍ਤਾ, ਜ਼ਬਾਨ, ਕੋਸ਼_ਅਨੁ):
        raise NotImplementedError


def écrire_json(dic, doc):
    if not os.path.isdir(os.path.split(doc)[0]):
        os.makedirs(os.path.split(doc)[0])

    with open(doc, 'w', encoding='utf8') as d:
        json.dump(dic, d, ensure_ascii=False, sort_keys=True, indent=2)
