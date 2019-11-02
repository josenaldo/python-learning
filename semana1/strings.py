###############################################################################
# Para usar aspas duplas em uma string, você pode uar váriuas formas.count
# 1) Você pode colocar a string em aspas simples e usar as aspas duplas 
# como se fosse um caracter normal. O mesmo serve para aspas simples.
aspasNaoEscapadas = 'My favorite book is "Python Tricks"'
print(aspasNaoEscapadas)

# 2) Você pode escapar as aspas. O mesmo serve para aspas simples.
aspasEscapadas = "My favorite book is \"Python Tricks\""
print(aspasEscapadas)


###############################################################################
# Para remover o caracter de nova linha, no fim de uma string, você pode usar 
# a função .rstrip()
texto = 'A line of text.\n'
print("###############################################################################")
print (texto)
print("###############################################################################")
print (texto.rstrip())
print("###############################################################################")
print (texto)
print("###############################################################################")
print (texto.rstrip())  

###############################################################################
# Se for preciso desligar o escape de caracteres, você pode usar as 
# raw-string literals. Basta preceder a aspa de abertura da string com um r ou R
rawText = r"C:\windows\system32\drivers\etc\hosts"
print (rawText)

###############################################################################
# Para saber o tamanho de uma string, devemos usar a função len
print ("\n========== Função Len ==========")
texto = "Olha só esse texto"
print("O texto\"", texto, "\"tem", len(texto), "caracteres." )

###############################################################################
# Como Python é uma linguagem fortemente tipada, pra poder concatenar um número
# a uma string, é necessário usar a função str(), que converte objetos em sua
# representação string
concatenacao1 =  "Eu tenho " + str(42) + " anos"
print(concatenacao1)

###############################################################################
# Imprimindo um inteiro
print(42)                            # <class 'int'>

# Imprimindo um float
print(3.14)                          # <class 'float'>

# Imprimindo um complex
print(1 + 2j)                        # <class 'complex'>

# Imprimindo um booleano
print(True)                          # <class 'bool'>

# Imprimindo uma lista
print([1, 2, 3])                     # <class 'list'>

# Imprimindo uma tupla
print((1, 2, 3))                     # <class 'tuple'>

# Imprimindo um conjunto
print({'red', 'green', 'blue'})      # <class 'set'>

# Imprimindo um dicionário
print({'name': 'Alice', 'age': 42})  # <class 'dict'>

# Imprimindo uma string
print('hello')                       # <class 'str'>

# Imprimindo a constante None
print(None)