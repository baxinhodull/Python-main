estoque = ["BMW X6", "BMW I5", "BMW I8"]

pesquisa_carro = input("Informe o carro desejado: ").strip()

if not pesquisa_carro:
    print("Por favor, informe o nome de um carro.")
else:
   
    if pesquisa_carro.title() in [carro.title() for carro in estoque]:
        print("O carro está disponível em estoque.")
    else:
        print("O carro não está disponível em estoque.")
