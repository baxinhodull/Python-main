# Set (Listas)
    # simular as lista 
    # Evitar itens duplicados 
    # Não utiliza Index

list1 = [10,20,30,40,50]
list2 = [10,20,60,70]

num1 = set(list1)
num2 = set(list2)

print(num1 | num2) # unifica as duas listas retirando o repetido 

print ( num1 - num2 ) # Difference pegas os valores diferentes 
print ( num2 - num1 ) # Difference pegas os valores diferentes 
print ( num1 ^ num2 ) # Symmetric Diiference tira os duplicados 
print ( num1 & num2 ) # Difference pegas os valores diferentes 