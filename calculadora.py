# Função para somar dois números
def soma(num1, num2):
    return num1 + num2

# Função para subtrair dois números
def subtracao(num1, num2):
    return num1 - num2

# Função para multiplicar dois números
def multiplicacao(num1, num2):
    return num1 * num2

# Função para dividir dois números
def divisao(num1, num2):
    if num2 == 0:
        return "Erro: divisão por zero!"
    else:
        return num1 / num2

# Função para calcular a potência de um número
def potencia(num, exp):
    return num ** exp

# Função para calcular a raiz quadrada de um número
def raiz_quadrada(num):
    if num < 0:
        return "Erro: não existe raiz quadrada de número negativo!"
    else:
        return num ** 0.5

# Menu principal da calculadora
while True:
    print("Escolha uma operação:")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Potência")
    print("6 - Raiz Quadrada")
    print("0 - Sair")

    opcao = input("Digite sua escolha: ")

    if opcao == "0":
        print("Obrigado por usar a calculadora!")
        break

    elif opcao in ["1", "2", "3", "4", "5", "6"]:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        if opcao == "1":
            resultado = soma(num1, num2)
        elif opcao == "2":
            resultado = subtracao(num1, num2)
        elif opcao == "3":
            resultado = multiplicacao(num1, num2)
        elif opcao == "4":
            resultado = divisao(num1, num2)
        elif opcao == "5":
            resultado = potencia(num1, num2)
        elif opcao == "6":
            resultado = raiz_quadrada(num1)

        print("Resultado: ", resultado)

    else:
        print("Opção inválida! Tente novamente.")
