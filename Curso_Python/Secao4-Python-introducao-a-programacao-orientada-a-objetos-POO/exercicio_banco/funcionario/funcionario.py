class Funcionario:
    def __init__(self, nome, cpf, salario):
        self.nome = nome
        self.cpf = cpf
        self.salario = salario


    def __init__(self, senha, qtd_funcionario):
        self.senha = senha
        self.qtd_funcionario = qtd_funcionario

    def autentica(self, senha):
        if self.senha == senha:
            print('Acesso
class Gerente(Funcionario):
 permitido')
            return True