par_ou_impar = lambda num: "Par" if num % 2 == 0 else "Ímpar"

user_number = int(input("Digite um número: "))

print(f"O número {user_number} é {par_ou_impar(user_number)}.")
