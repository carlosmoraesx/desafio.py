MAIOR_IDADE = 18
IDADE_ESPECIAL = 17
idade = int(input("informe sua idade"))

if idade >= MAIOR_IDADE:
    print("Maior idade, pode tirar CNH.")

if idade < MAIOR_IDADE:
    print("ainda não pode tirar CNH.")



if idade >= MAIOR_IDADE:
    print("Maior idade, pode tirar CNH.")
else:
    print("Ainda não pode tirar CNH.")


if idade >= MAIOR_IDADE:
    print("Maior idade, pode tirar CNH.")
elif idade == IDADE_ESPECIAL:
    print("pode fazer as aulas teóricas, porém não as práticas.")
else:
    print("Ainda não pode tirar CNH.")