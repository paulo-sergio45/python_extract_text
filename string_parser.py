import re
import string

def processa_string(string_raw: string):
    result: string = re.sub(padrao, substituir_string, string_raw, flags=re.VERBOSE)
    return result

def substituir_string(match):
    if match.group("email"):
        return "[EMAIL]"
    elif match.group("data"):
        return "[DATA]"
    elif match.group("telefone"):
        return "[TELEFONE]"
    else:
        return match.group(0)

padrao = r"""
    (?P<email>[\w.-]+@[\w.-]+\.\w+) |
    (?P<data>\d{2}/\d{2}/\d{4})     |
    (?P<telefone>\b\d{11}\b)
"""
