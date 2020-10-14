class Microondas:
    def __init__(self, ligar=True):
        self.ligar = ligar

    def ligando(self):
        self.ligar = True
        print('Ligando')
        return

    def arroz(self):
        pass

    def descongelar(self):
        pass

    def pizza(self):
        pass

    def lasanha(self):
        pass

    def desligando(self):
        self.ligar = False
        print('Desligando')
        return
