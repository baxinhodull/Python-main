a = 'Gabriel'
b = "Seja bem vindo"
c = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
d = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""

# print(d)

e = "Ola Mundo !"

# print(e[0])

# for x in "Gabriel":
#     print(x)

# x = len(e)
# print(len(e))

txt = "Seja bem vindo ao curso de Python."

x = "vindo" in txt
print(x)
print("carro" in txt)

if "vindo" in txt:
    print("Sim, 'vindo' está presente.")

if "lucas" not in txt:
    print("'lucas' não está presente.")
