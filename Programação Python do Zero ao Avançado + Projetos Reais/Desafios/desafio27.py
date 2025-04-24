def fatorial_recursivo(n):
    if n < 0:
        raise ValueError("Fatorial não existe para números negativos.")
    if n == 0 or n == 1:
        return 1
    return n * fatorial_recursivo(n - 1)

try:
    numero = int(input("Digite um número inteiro não negativo: "))
    print(f"Fatorial de {numero} é {fatorial_recursivo(numero)}")
except ValueError as e:
    print(f"Erro: {e}")
