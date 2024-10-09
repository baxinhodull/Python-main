def soma (*numeros):
    resultado = 0
    for num in numeros:
        resultado += num
    return resultado


s = soma(2,4,3,7)

print(s)