from microondas.opcoes.configuracao import MicroondasOpcoes, Funcionamento

print('Microondas')
print('Potencia de 1 a 9 e tempo')
print('Opções: \n(1) Almoço \n(2) Descongelar \n(3) Macarrão Instantâneo \n(4) Arroz \n(5) Strogonoff ')
print()
print()


teste = Funcionamento()
teste.ligar()
teste = MicroondasOpcoes(10, 9, False)


