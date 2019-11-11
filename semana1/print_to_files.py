###############################################################################
# Ao iterar sobre as linhas de um arquivo e imprimir essas linhas, devemos 
# tomar cuidado com os caracteres de nova linha. A linha já possui um 
# caracter e imprimir essa linha usando print(), sem nenhum tratamento, 
# ocasionará na impressão de uma linha em branco extra.  
with open('file.txt') as file_object:
     for line in file_object:
         print(line)

# Para evitar isso, podemos usar dois métodos. 
# 1) usar a função rstrip() para apagar o caractere de nova linha 
# da linha lida, antes de imprimir
with open('file.txt') as file_object:
     for line in file_object:
         print(line.rstrip())

# 2) Manter o caracter de nova linha, mas suprimir o caracter adicionado 
# pela função print. Para isso, basta setar o parâmetro nomeado 'end' para
# uma string vazia
with open('file.txt') as file_object:
     for line in file_object:
         print(line, end='')

###############################################################################
# Para imprimir um texto em um arquivo
print("Imprimindo texto em um arquivo")
with open('file2.txt', mode='w') as file_object:
    print('hello world', file=file_object)

###############################################################################
# Se for preciso mudar o encoding do arquivo, devemos usar o parâmetro 
# nomeado 'encoding'
with open('file3.txt', mode='w', encoding='iso-8859-1') as file_object:
    print('über naïve café', file=file_object)

###############################################################################
# Ao invés de usar um arquivo real, armazenado no seu sistema 
# de arquivos, você pode usar um arquivo falso, um arquivo na memória.
# Essa técnica pode ser usada em testes de unidades, pra simular a função
# print(). 
import io
fake_file = io.StringIO()
print('hello world', file=fake_file)
fake_file.getvalue()