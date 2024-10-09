x = "incrível"

def myFunc():
    global x
    x = "inacreditavel"
    y = "fantastico"
    global z
    z = "Bem vindo ao curso"
    print("Python é " + x + " e " + y)
    print(z)

myFunc()

print("============================")
print("Você é " + x)
print(z)