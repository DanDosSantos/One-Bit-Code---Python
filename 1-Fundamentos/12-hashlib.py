# Criptografia
import hashlib

# # 1 - Verificar os algoritmos disponíveis
# print(hashlib.algorithms_available)

# # 2 - Algoritmos disponíveis de acordo com o SO
# print(hashlib.algorithms_guaranteed)

# 3 - Utilizando o Sha256
algoritmo = hashlib.sha256()
print(algoritmo.digest())
mensagem = 'Essa mensagem irá ser criptografada'.encode()
algoritmo.update(mensagem)
print(algoritmo.hexdigest()) # Aqui exibirá a mensagem criptografada em hexadecimal


