import hashlib

print(hashlib.algorithms_guaranteed)
algoritmo = hashlib.sha256()
mensagem = 'Palmeiras meu palmeiras meu palmeeeeeiras eu nao sei oq escrever mais por aqui hahahah nao sei mesmo ahahahahah'.encode()
algoritmo.update(mensagem)
print(algoritmo.hexdigest())
