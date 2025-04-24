def potencia(base, expoente=2):
    return base ** expoente

def multiplicacao_de_potencias(a, m, n):
    return a ** (m + n)

def divisao_de_potencias(a, m, n):
    return a ** (m - n)

def potencia_de_potencia(a, m, n):
    return a ** (m * n)

def potencia_de_fracao(a, b, m):
    if b == 0:
        raise ZeroDivisionError("O denominador não pode ser zero.")
    return (a ** m) / (b ** m)

def potencia_negativa(a, m):
    return 1 / (a ** m)

def potencia_fracionaria(a, x, y):
    if y == 0:
        raise ZeroDivisionError("O denominador da fração não pode ser zero.")
    return (a ** x) ** (1 / y)

print("Escolha a regra de exponenciação:")
print("1. a^m × a^n = a^(m+n)")
print("2. a^m ÷ a^n = a^(m-n)")
print("3. (a^m)^n = a^(m×n)")
print("4. (a/b)^m = a^m / b^m")
print("5. a^(-m) = 1/a^m")
print("6. a^(x/y) = y√(a^x)")
print("7. a^0 = 1")
print("8. a^1 = a")

opcao = input("Digite a opção (1-8): ")

try:
    if opcao == "1":
        a = float(input("Base a: "))
        m = int(input("Expoente m: "))
        n = int(input("Expoente n: "))
        print("Resultado:", multiplicacao_de_potencias(a, m, n))

    elif opcao == "2":
        a = float(input("Base a: "))
        m = int(input("Expoente m: "))
        n = int(input("Expoente n: "))
        print("Resultado:", divisao_de_potencias(a, m, n))

    elif opcao == "3":
        a = float(input("Base a: "))
        m = int(input("Expoente interno m: "))
        n = int(input("Expoente externo n: "))
        print("Resultado:", potencia_de_potencia(a, m, n))

    elif opcao == "4":
        a = float(input("Numerador da fração: "))
        b = float(input("Denominador da fração: "))
        m = int(input("Expoente m: "))
        print("Resultado:", potencia_de_fracao(a, b, m))

    elif opcao == "5":
        a = float(input("Base a: "))
        m = int(input("Expoente positivo m (será convertido em -m): "))
        print("Resultado:", potencia_negativa(a, m))

    elif opcao == "6":
        a = float(input("Base a: "))
        x = int(input("Expoente x (numerador): "))
        y = int(input("Raiz y (denominador): "))
        print("Resultado:", potencia_fracionaria(a, x, y))

    elif opcao == "7":
        a = float(input("Base a: "))
        print("Resultado:", a ** 0)

    elif opcao == "8":
        a = float(input("Base a: "))
        print("Resultado:", a ** 1)

    else:
        print("Opção inválida!")

except ValueError:
    print("Erro: por favor, digite apenas números válidos.")
except ZeroDivisionError as e:
    print(f"Erro: {e}")
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")
