#função para gravar dados no arquivo
def gerarListaOrdenada():
 quantidade = int(input('Informe a quantidade de elementos:'))
 arquivo=open('idsOrdenados.txt','w')
 #gerar registro com os números
 for elemento in range(quantidade):
    arquivo.write(str(elemento)+'\n')
 arquivo.close()
#executar a função
gerarListaOrdenada()