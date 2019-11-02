###############################################################################
# Help da função print()
# print(...)
#     print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
#    
#     Prints the values to a stream, or to sys.stdout by default.
#     Optional keyword arguments:
#     file:  a file-like object (stream); defaults to the current sys.stdout.
#     sep:   string inserted between values, default a space.
#     end:   string appended after the last value, default a newline.
#     flush: whether to forcibly flush the stream.


###############################################################################
# A execução mais básica de uso da função print() é a chama sem argumentos.
# Essa chamada  produz um caracter de nova linha ("\n")
print()

###############################################################################
# Você pode, passar a literal da string diretamente na chamada
print("Olha só, uma string")

###############################################################################
# você pode passar uma ou mais variáveis pra função print
mensagem = "Parabéns"
nome = "Ermenegildo"
print(mensagem)
print(mensagem, nome)

###############################################################################
# Dá pra passar uma concatenação de strings
print('Oi, ' + nome + '! Como vai?')

###############################################################################
# Também é possível usar uma string formatada
print(f'Oi, {nome}! Como vai?')

###############################################################################
# A função print(), por padrão. imprime todos seus argumentos em sequência, 
# com um espaço entre cada argumento
print("maça", "banana", "batata", "laranja")

# Para mudar o separador, basta usar o keyword argument 'sep' (de separator)
# imprime 'hello world'
print('hello', 'world')

# Imprime 'hello,world'
print('hello', 'world', sep=',')

# Para suprimir o separador, deve-se passar uma string vazia ('') no keyword 
# argument sep
print('hello', 'world', sep='')

# É possível informar vários caracteres no separador
print('hello', 'world', 'people', sep='{Vários caracteres}')

# Imprimindo cada argumento em uma linha separada
print('hello', 'world', sep='\n')

# Imprimindo um caminho de diretório no Linux
print('/home', 'user', 'documents', sep='/')

# Uma alternativa para forçar a barra no início é fornecer uma string vazia no 
# primeiro argumento
print('', 'home', 'user', 'teste', 'documents', sep='/')

# Imprimindo um caminho de diretório no Windows
print('C:', 'Users', 'Josenaldo', 'Documents', sep='\\')

# Imprimindo uma URL
print('https:/','meudominiio.com','subpasta1','subpasta2','arquivo.html', sep='/')

# Para imprimir uma lista ou uma tupla, use o operador *. 
# Se você tentar imprimir os elementos de uma lista ou tupla 
# usando a função join, você pode acabar com um TypeError
# Não faça: 
#   print(' '.join(['jdoe is', 42, 'years old']))
# Faça:
print(*['jdoe is', 42, 'years old'])

# Você pode usar o prit para exportar dados par auma CSV, por exemplo
print(1, 'Python Tricks', 'Dan Bader', sep=',')

###############################################################################
# Para desabilitar a nova linha ao fim do texto impresso, você deve usar o 
# keyword argument 'end' com uma string vazia
print('Checando a integridade do arquivo...', end='')
# (...)
print('ok')

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
# pela função print. Para isso, basta setar o keyword argument 'end' para
# uma string vazia
with open('file.txt') as file_object:
     for line in file_object:
         print(line, end='')
