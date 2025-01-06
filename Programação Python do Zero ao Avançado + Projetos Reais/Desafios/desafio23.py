def find_common_friends(set1, set2):
    """Função para encontrar amigos em comum entre dois conjuntos"""
    return set1.intersection(set2)

def print_common_friends(friends_set):
    """Função para imprimir os amigos em comum de forma legível"""
    if friends_set:
        print("Amigos em comum:", ", ".join(friends_set))
    else:
        print("Não há amigos em comum.")

# Definindo os conjuntos de amigos
friends1 = {"Dulcimar", "Carlos", "Lucimar", "João", "Lorena"}
friends2 = {"Dulcimar", "Carlos", "Sergio", "Fatima", "Lorena"}

# Encontrando os amigos em comum
common_friends = find_common_friends(friends1, friends2)

# Imprimindo os amigos em comum
print_common_friends(common_friends)