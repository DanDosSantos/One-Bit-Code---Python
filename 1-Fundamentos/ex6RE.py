import re

# Verificar se uma string contém apenas um determinado conjunto de caracteres (neste case, a-z, A-Z e 0-9)
def check_character(string):
    rule = re.compile(r'[^a-zA-Z0-9]') # Definir caracteres aceitos
    string = rule.search(string)
    return not bool(string)

print(check_character('SDSFDheduhdeueADNCKEPORNFfciwef3452314567'))
print(check_character('$%¨^^{};.<>'))  # Não aceitos