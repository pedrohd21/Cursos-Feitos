# arquivo = open('abc.txt', 'w')
# arquivo.write('Alguma coisa')
# arquivo.close()


class Arquivo:
    def __init__(self, arquivo, modo):
        self.arquivo = open(arquivo, modo)

    def __enter__(self):
        return self.arquivo


with open('abc.txt', 'w') as arquivo:
    arquivo.write('Alguma coisa')
