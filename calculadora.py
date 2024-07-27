import operacoes

while True:
    print("Selecione a operação:")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Sair")

    escolha = input("Digite sua escolha (1/2/3/4/5): ")
    if escolha == '5':
        break

    num1 = float(input("Digite um numero:"))
    num2 = float(input("Digite um numero:"))    

    if escolha == '1':
        print(num1, "+", num2, "=", operacoes.soma(num1, num2))
    elif escolha == '2':
        print(num1, "-", num2, "=", operacoes.subtracao(num1, num2))
    elif escolha == '3':
        print(num1, "*", num2, "=", operacoes.multiplicacao(num1, num2))
    elif escolha == '4':
        print(num1, "/", num2, "=", operacoes.divisao(num1, num2))
    else:
        print("Escolha inválida.")
