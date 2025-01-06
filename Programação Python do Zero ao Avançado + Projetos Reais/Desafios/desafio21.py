cidades = ("rio de janeiro", "são paulo", "salvador")

cidade_usuario = input("Digite o nome da cidade: ").strip().lower()

if cidade_usuario in cidades:
    print(f"A cidade '{cidade_usuario.title()}' está na lista.")
else:
    print(f"Não encontramos sua cidade '{cidade_usuario.title()}'.")
