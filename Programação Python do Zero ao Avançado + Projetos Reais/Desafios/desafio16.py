def verificar_numero():
    try:
        
        numero = int(input("Digite um número: "))
        
        if numero > 10:
            print("O número é maior que 10.")
        elif numero < 10:
            print("O número é menor que 10.")
        else:
            print("O número é igual a 10.")
    except ValueError:
        print("Entrada inválida! Por favor, digite um número inteiro válido.")

verificar_numero()
