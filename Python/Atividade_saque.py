saldo = 5000
print("Seu saldo atual é:", saldo)

sacar = int(input("Digite o valor que deseja sacar: "))

if sacar <= saldo:
    print("O saque foi realizado com sucesso!")
    print("Seu novo saldo é:", saldo - sacar)
else:
    print("Saldo insuficiente para realizar o saque.")
    print("Seu saldo atual é:", saldo)
    print("Tente novamente com um valor menor ou igual ao seu saldo.")