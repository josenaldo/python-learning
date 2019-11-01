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


