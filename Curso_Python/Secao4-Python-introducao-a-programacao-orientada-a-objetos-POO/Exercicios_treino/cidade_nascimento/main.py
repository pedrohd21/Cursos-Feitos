from dados.dados import *

cliente1 = Pessoais('Pedro', 23)
cliente1.insere_endereco('Belo Horizonte', 'MG')
print(cliente1.nome)
cliente1.lista()
# del cliente1
print()

cliente2 = Pessoais('Maria', 55)
cliente2.insere_endereco('Belo Salvador', 'BA')
cliente2.insere_endereco('Rio de Janeiro', 'RJ')
print(cliente2.nome)
cliente2.lista()
# del cliente2
print()

cliente3 = Pessoais('João', 19)
cliente3.insere_endereco('São Paulo', 'SP')
print(cliente3.nome)
cliente3.lista()
# del cliente3
print()

print('#' * 40)