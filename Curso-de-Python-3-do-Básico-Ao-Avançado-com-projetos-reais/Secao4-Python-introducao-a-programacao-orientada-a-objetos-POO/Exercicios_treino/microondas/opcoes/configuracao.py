from time import sleep


class Funcionamento:
    def __init__(self, estado=False):
        self.estado = estado

    def ligar(self, ligando=False):
        if not ligando:
            self.estado = True
            print('Ligando Microondas')
            return
        else:
            self.estado = False
            return

    def funcionamento(self, valor=False):
        valor = self.estado
        if valor:
            print('Microondas em funcionamento')
        else:
            print('Micoondas Desligado')

    def desligar(self, valor=False):
        if not valor:
            self.estado = False
            print('Desligando Microondas')
            return
        else:
            self.estado = True
            self.ligar(False)
            return


class MicroondasOpcoes:
    def __init__(self, tempo=0, potencia=0):
        self.tempo = tempo
        self.potencia = potencia

    def tempo(self, valor):
        print(f'{self.tempo()}')

    def opcao(self, valor):
        if valor == 1:
            print(f'Opção {valor} \nTempo de Espera 1 minuto')
            self.temporizador(20)
            print('Almoço Pronto!!')

        elif valor == 2:
            print(f'Opção {valor} \nTempo de Espera 10 minuto')
            self.temporizador(20)
            print('Descongelamento Completo!!')

        elif valor == 3:
            print(f'Opção {valor} \nTempo de Espera 5 minuto')
            self.temporizador(20)
            print('Macarrão Instantâneo Pronto!!')

        elif valor == 4:
            print(f'Opção {valor} \nTempo de Espera 20 minuto')
            self.temporizador(20)
            print('Arroz Pronto!!')

        elif valor == 5:
            print(f'Opção {valor} \nTempo de Espera 15 minuto')
            self.temporizador(20)
            print('Strogonoff Pronto!!')

    def temporizador(self, valor):
        for c in range(valor):
            sleep(.10)



