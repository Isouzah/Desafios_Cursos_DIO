#def password_generator(lenght, upper_case, lower_case, numbers, special_characters):
#    length = int(input("Quantos digitos deseja que a senha tenha? "))
#    upper_case = bool(input("deseja adiconar letras maiusculas? (S/N) "))
#    lower_case = bool(input("deseja adiconar letras minusculas? (S/N) "))
#    numbers = bool(input("deseja adiconar numeros? (S/N)) "))
#    special_characters = bool(input("deseja adiconar caracteres especiais? (S/N) "))

print("Bem vindo ao gerador de senhas!")
input("Pressione enter para continuar...")
print(int(input("Qual o tamanho da senha? ")))
upper_case = bool(input("deseja adiconar letras maiusculas? (S/N) "))
if upper_case == "s.upper().strip()":
    upper_case = True
else:
    upper_case = False

lower_case = bool(input("deseja adiconar letras minusculas? (S/N) "))
if lower_case == "s.upper().strip()":
    lower_case = True
else:
    lower_case = False

numbers = bool(input("deseja adiconar numeros? (S/N)) "))
if numbers == "s.upper().strip()":
    numbers = True
else:
    numbers = False

special_characters = bool(input("deseja adiconar caracteres especiais? (S/N) "))
if special_characters == "s.upper().strip()":
    special_characters = True
else:
    special_characters = False