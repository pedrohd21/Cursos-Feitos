from abc import ABC, abstractmethod


class Cliente:
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade

    @property
    def nome(self):
        return self._nome

    @property
    def idade(self):
        return self._idade


class Bank(ABC):
    def __init__(self, saldo, limite=2000):
        self.saldo = saldo
        self._limite = limite

    @property
    def limite(self):
        return self._limite

    @limite.getter
    def limite(self):
        return self._limite

    @abstractmethod
    def depositar(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError('Valor do deposito precisa ser numerico.')

    @abstractmethod
    def sacar(self, valor):
        pass

