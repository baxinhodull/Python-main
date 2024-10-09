#limpa o terminal quando é executado automáticamente 

import os

os.system("cls") or None

# Entrada de dados
num1 = input("Digite o primeiro número: ")
num1 = int(num1)

num2 = input("Digite o segundo número.: ")
num2 = int(num2)

# Processamento
mult = num1 * num2

# Saída da informação
print()
print("A multiplicação de", num1, "por", num2, "é", mult)
