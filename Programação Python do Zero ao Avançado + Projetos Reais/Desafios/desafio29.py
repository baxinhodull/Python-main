triplo = lambda x: x * 3
cubo_do_triplo = lambda x: (triplo(x)) ** 3

num = int(input("Digite um número: "))
print(f"O cubo do triplo do número {num} é {cubo_do_triplo(num)}")
