class Aluno:
    def __init__(self, total, nome):
        self.total = total
        self.nome = nome


class Resultado(Aluno):
    def __init__(self, total, nome):
        super().__init__(total, nome)

    def media(self):
        med = self.total
        print(f'{self.nome} media: {med / 4:.2f}')
        return

    def situacao(self):
        media = self.total / 4
        if media >= 7:
            print('Aprovado!!')
        elif media >= 5:
            print('Recuperação!!')
        else:
            print('Reprovado!!')


nota = 0
for c in range(1, 5):
    nota += float(input(f'Nota {c}°: '))


a1 = Resultado(nota, 'Pedro')
a1.media()
a1.situacao()
