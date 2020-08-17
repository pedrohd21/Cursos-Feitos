class Endereco:
    def __init__(self, cidade, estado):
        self.__cidade = cidade
        self.__estado = estado

    @property
    def cidade(self):
        return self.__cidade

    @property
    def estado(self):
        return self.__estado

    def __del__(self):
        print(f'{self.cidade} {self.estado} FOI APAGADO!')


class Pessoais:
    def __init__(self, nome, idade):
        self.__nome = nome
        self.__idade = idade
        self.endereco = []

    @property
    def nome(self):
        return self.__nome

    def insere_endereco(self, cidade, estado):
        self.endereco.append(Endereco(cidade, estado))

    def lista(self):
        for end in self.endereco:
            print(f'{end.cidade} {end.estado}')

    def __del__(self):
        print(f'{self.nome} FOI APAGADO!')

