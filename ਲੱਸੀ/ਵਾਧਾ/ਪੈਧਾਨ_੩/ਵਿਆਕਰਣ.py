try:
    import black
except ImportError:
    pass

from lark.indenter import Indenter
from ਲੱਸੀ.ਵਿਆ.ਭਾ import ਵਿਆਕਰਣ_ਵਾਧਾ


class PythonIndenter(Indenter):
    NL_type = 'NEWLINE'
    OPEN_PAREN_types = ['LPAR', 'LSQB', 'LBRACE']
    CLOSE_PAREN_types = ['RPAR', 'RSQB', 'RBRACE']
    INDENT_type = 'INDENT'
    DEDENT_type = 'DEDENT'
    tab_len = 8


def ਮੁੜ_ਉਸਾਰੀ_ਬਾਅਦ_ਕਾਰ(ਪਾਠ):
    for ਅ in ਪਾਠ:
        if not hasattr(ਅ, 'type') or not ਅ.type in ['INDENT', 'DEDENT']:
            yield '{} '.format(ਅ) if len(ਅ.strip()) and not ਅ.strip(' \t').endswith('\n') else ਅ


class ਪੈਧਾਨ_੩_ਵਿਆ(ਵਿਆਕਰਣ_ਵਾਧਾ):
    ਵਿਆ = 'ਪੈਧਾਨ ੩.lark'
    ਵਾਧਾ = '.py'
    ਸਰੋਤ_ਭਾ = 'en'

    ਸ਼ਬਦ_ਵਿਸ਼_ਬਦਲ = dict(postlex=PythonIndenter(), start='file_input', parser='lalr')

    spéciaux = {'ENT': 'DEC_NUMBER',
                'DEC': 'FLOAT_NUMBER',
                'ਨਾਮ': 'NAME'}

    def __init__(ਖੁਦ):
        super().__init__()
        ਖੁਦ.ਮੁੜ_ਉਸਾਰੀ_ਬਦਲ = dict(postproc=ਮੁੜ_ਉਸਾਰੀ_ਬਾਅਦ_ਕਾਰ)

    def ਬਾਅਦ_ਕਾਰਵਾਈ(ਖੁਦ, ਦਸਤ, ਭਾਸ਼ਾ):
        if ਭਾਸ਼ਾ == 'en' and black is not None:
            return black.format_file_contents(ਦਸਤ, fast=True, mode=black.FileMode())
        else:
            return ਦਸਤ

    def gén_mots_intégrés(soimême):
        # noinspection PyTypeChecker
        return [str(x) for x in __builtins__  if x not in ["None", "True", "False"]] + list(object.__dict__) + ['self', 'cls']
