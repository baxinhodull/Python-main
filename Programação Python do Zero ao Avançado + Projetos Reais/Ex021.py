valor = int (input("Digite o valor do produto em R$"))

while valor >= 20:
    valor = (valor*0.10)+valor
    print(f'O valor final do seu produto serrá de R$ {valor}')
    break