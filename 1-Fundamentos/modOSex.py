import os

# # 1 - Desligar PC
# shutdown = input('Voce deseja desligar o computador? (sim / nao): ')

# if shutdown == 'nao':
#     exit()
# else:
#     os.system('shutdown /s') # em 1 min


# # 2 - Cancelar desligamento do PC
# os.system('shutdown /a')



def desligar_uma_hora():
    os.system('shutdown /s /t 3600')

def desligar_em_meia_hora():
    os.system('shutdown /s /t 1800')

def cancelar_desligamento():
    os.system('shutdown /a')

# desligar_uma_hora()
# cancelar_desligamento()
# desligar_em_meia_hora()
cancelar_desligamento()