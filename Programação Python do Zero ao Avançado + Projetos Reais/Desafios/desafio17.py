def verificar_idade():
    try:
        
        idade = int(input("Digite sua idade: "))
        
        if idade < 13:
            print("Você é uma criança ")
        elif 13 <= idade <=20 :
            print("Você é uma adolencente ")
        else:
            print("Você é um adulto.")
    except ValueError:
        print("Entrada inválida! Por favor, digite um número inteiro válido.")

verificar_idade()
