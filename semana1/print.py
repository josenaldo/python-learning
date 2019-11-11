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
# Também é possível usar uma string formatada. Não se esqueça do f na frente 
# da string!
print(f'Oi, {nome}! Como vai?')

###############################################################################
# A função print(), por padrão. imprime todos seus argumentos em sequência, 
# com um espaço entre cada argumento
print("maça", "banana", "batata", "laranja")

# Para mudar o separador, basta usar o parâmetro nomeado 'sep' (de separator)
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
# parâmetro nomeado 'end' com uma string vazia
print('Checando a integridade do arquivo...', end='')
# (...)
print('ok')


###############################################################################
# Para formatar um número, no print, vocÊ precisa usar o operador % no local 
# onde o número formatado será inserido. Exemplo: queremos exibir um float com 
# 2 casas decimais. Para isso, usamos o operador de módulo (%).

# Imprime a temperatura celsius com 2 casas decimais
temperaturaCelcius = 25.76252734236
print("A temperatura em celsius é %.2f" % (temperaturaCelcius), "graus celsius")

# imprime um inteiro, com 5 colunas, e um float com 6 colunas e 2 casas decimais
print("Aluno: %5d, Nota : % 6.2f" %(9, 05.333))  
print("Aluno: %5d, Nota : % 6.2f" %(10, 67.89278328))  
print("Aluno: %5d, Nota : % 6.2f" %(151, 3.444444))  
print("Aluno: %5d, Nota : % 6.2f" %(467, 12.09827382736))  
  
# imprime 1 inteiro, com 3 colunas, e 1 inteiro, com 2 colunas
print("Total de alunos: %3d, Meninos : %2d" %(240, 120)) 
  
# imprime um valor em octal
print("% 7.3o"% (25)) 
  
# imprime um valor em notação científica
print("% 10.3E"% (356.08977)) 