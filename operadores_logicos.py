# And = para ser true tudo tem que ser true
# OR = para ser true apenas um tem que ser true

print(true and true and true)
print(true and false and true)
print(false and false and false)
print(true or true or true)
print(true or false or false)
print(false or false or false)



saldo = 1000
saque = 250
limite = 200
conta_especial = true

exp = saldo >= saque and saque <= limite or conta_especial and saldo >= saque
print(exp)

exp_2 = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)
print(exp_2)

