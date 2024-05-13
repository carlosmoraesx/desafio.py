nome = "carlos"
idade = 20
profissão = "programador"
linguagem = "python"

dados = {"nome": "carlos", "idade": 20}

print("nome: %s idade: %d" % (nome,idade))
print("nome: {} idade: {}".format(nome, idade))
print("nome: {1} idade: {0}".format(idade, nome))

print("nome: {nome} idade: {idade}".format(**dados))