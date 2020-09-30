"""
https://openpyxl.readthedocs.io/en/stable/
pip install openpyxl
pipenv install openpyxl
"""
import openpyxl

pedidos = openpyxl.load_workbook('pedidos.xlsx')
nomes_planilhas = pedidos.sheetnames
planilha1 = pedidos['Página1']
# print(planilha1['b4'].value)  # mostra oq tem na coluna b 4

# mostra tudo da coluna b
# for campo in planilha1['b']:
#     print(campo.value)

# Mostra oq tem de a1 a c2
# for campo in planilha1['a1:c2']:
#     for coluna in campo:
#         print(coluna.value)


for linha in planilha1:
    print(linha[0].value, linha[1].value, linha[2].value, linha[3].value, )

# PAreiii 13:14