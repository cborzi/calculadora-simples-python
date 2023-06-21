import math

def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b != 0:
        return a / b
    else:
        return "Erro: divisão por zero"

def potencia(a, b):
    return a ** b

def raiz_quadrada(a):
    return math.sqrt(a)

def calcular():
    operacoes = {
        '+': soma,
        '-': subtracao,
        '*': multiplicacao,
        '/': divisao,
        '^': potencia,
        'sqrt': raiz_quadrada
    }

    operacao = input("Digite a operação desejada (+, -, *, /, ^, sqrt): ")

    if operacao not in operacoes:
        print("Operação inválida")
        return

    if operacao == 'sqrt':
        num = float(input("Digite o número: "))
        resultado = operacoes[operacao](num)
    else:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        resultado = operacoes[operacao](num1, num2)

    print("Resultado: ", resultado)

calcular()
