prod = float(input('Qual é o valor do produto? '))
desc = prod-((prod*5)/100)
print('O produto que custava R${:.2f}, na promoção com desconto de 5% vai custar R${:.2f}'.format(prod, desc))