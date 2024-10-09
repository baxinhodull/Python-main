#Array (Matriz)
    # similar a listas 
    # Melhor performance 


from array import array 


letras = ['a','b','c','d']
numeros_i = [ 10,20,30,40]
numero_f = [1.2,2.2,3.2]

print(letras)
print(numeros_i)
print(numero_f)
print()

letras = array('u',['a','b','c','d'])
numeros_i = array('i',[ 10,20,30,40])
numero_f = array('f',[1.2,2.2,3.2])

print(letras)
print(numeros_i)
print(numero_f)