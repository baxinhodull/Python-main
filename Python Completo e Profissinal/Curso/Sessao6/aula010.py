# Tipo de Dados 
'''
    Texto: STR 
    Númericos: Int, Float, Complex
    Sequencia: list, tuple, range 
    mapeamento: dict
    conjuntos: set,frozenset 
    Booleano: bool
    Binários: bytes, bytearray, memoryview

'''

# Definir o tipo de Dados 

x = "Hello World"
x = 20
x = 20.5
x = 1j
x =["Maçã", "banana", "Cereja "]
x = ("Maçã", "banana", "Cereja")
x = range(6)
x = {"name" : "Carlos" , "age" : 23} 
X = frozenset({"Maçã", "banana" , "Cereja"})
x = True
x = b"Hello"
x = bytearray (5)
x = memoryview(bytes(5))


# Configurando o Tipo de Dados Específico
# Utizamos a função predefinidas que nós temos 

x = str("Hello World") # str
x = int(20)	# int
x = float(20.5) # float
x = complex(1j)	# complex
x = list(("apple", "banana", "cherry"))	# list
x = tuple(("apple", "banana", "cherry")) # tuple
x = range(6) # range
x = dict(name="John", age=36) # dict
x = set(("apple", "banana", "cherry")) # set
x = frozenset(("apple", "banana", "cherry")) # frozenset
x = bool(5) # bool
x = bytes(5) # bytes
x = bytearray(5) # bytearray
x = memoryview(bytes(5)) # memoryview


