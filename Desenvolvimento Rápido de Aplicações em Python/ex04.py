# Define o nome do arquivo
nome_arquivo = "crescente_pulando_linha.txt"

# Abre o arquivo para escrita
with open(nome_arquivo, 'w') as arquivo:
    # Escreve os números de 1 a 100, cada um em uma nova linha
    for i in range(1, 101):
        arquivo.write(f"{i};\n")

print(f"Números de 1 a 100 foram escritos em '{nome_arquivo}'.")
