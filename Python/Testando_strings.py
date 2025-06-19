string = "Avada Kedavra"
txt2 = "Expelliarmus"


# print(string.strip().center(20, "X"))
# for letra in txt2:
#    print(letra, end="~~")

nome = "Galio"
idade = 30
profissao = "guarda"
horario = "noturno"

# método porcentagem
print("Olá meu nome é %s. Eu tenho %d anos e trabalho como %s, no horário %s" % (nome, idade, profissao, horario))

# método format
print("Olá meu nome é {}. Eu tenho {} anos e trabalho como {}, no horário {}".format(nome, idade, profissao, horario))

# método f-string
print(f"Olá meu nome é {nome}. Eu tenho {idade} anos e trabalho como {profissao}, no horário {horario}")