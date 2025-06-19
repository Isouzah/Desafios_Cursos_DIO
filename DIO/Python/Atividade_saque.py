saldo = 500
print("Seu saldo atual é:", saldo)

sacar = int(input("Digite o valor que deseja sacar: "))

if sacar <= saldo:
    print("O saque foi realizado com sucesso!")
    print("Seu novo saldo é:", saldo - sacar)
else:
    print("Saldo insuficiente para realizar o saque.")
    print("Seu saldo atual é:", saldo)
    print("gostaria de usar o cheque especial? (S/N)")
    cheque_especial = input().strip().upper()
    if cheque_especial == 'S':
        print("realmente deseja usar o cheque especial? (S/N)")
        confirmacao = input().strip().upper()
        if confirmacao == 'S':
            print("Cheque especial ativado.")
            print("Seu novo saldo é:", saldo - sacar)
        else:
            print("Cheque especial não ativado. Saque cancelado.")
            print("Saque não realizado. Seu saldo permanece:", saldo)
    print("Saque não realizado. Seu saldo permanece:", saldo)