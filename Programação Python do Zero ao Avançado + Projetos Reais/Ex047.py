# Filter Function 
    # Muito itlizado com listas 
    # Aplicar uma função a um Iterable, filtrandos os items. (list, tuple,dic etc)
import os 

os.system("cls") or None


valores = [10,12,34,44,57]
'''def remover20(x):

    return x > 20


print (list(filter(remover20, valores)))
'''
print(list(filter(lambda x: x>20, valores)))