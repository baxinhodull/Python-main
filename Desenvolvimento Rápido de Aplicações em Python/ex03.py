# Define o nome do arquivo
nome_arquivo = "crescente.txt"

# Gera os números de 1 a 100
numeros = [str(i) for i in range(1, 101)]

# Junta os números com o separador ";"
conteudo = ";".join(numeros)

# Abre o arquivo para escrita e grava o conteúdo
with open(nome_arquivo, 'w') as arquivo:
    arquivo.write(conteudo)

print(f"Números de 1 a 100 foram escritos em '{nome_arquivo}'.")
