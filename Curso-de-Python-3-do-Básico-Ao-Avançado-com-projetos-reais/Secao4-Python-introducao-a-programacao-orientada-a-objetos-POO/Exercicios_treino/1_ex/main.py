from banco import *

c1 = Conta('Pedro', 5897-1, 500, 2000)
c1.saca(100)
print(c1.extrato())
c1.transfere('454-7', 400)
print(c1.extrato())
c1.deposita(500)
c1.deposita(500)
c1.deposita(500)
c1.deposita(500)
c1.deposita(500)
print(c1.extrato())
c1.saca(100)
c1.saca(100)
c1.saca(100)
c1.deposita(200)
print(c1.extrato())


