def verificar_paridade(inicio, fim):
 
    
    for i in range(inicio, fim + 1):
    
        if i % 2 == 0:
            print(f"O número {i} é par.")
        else:
            print(f"O número {i} é ímpar.")

verificar_paridade(1, 10)
