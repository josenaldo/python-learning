# Programa de teste de operações matemáticas

x = 25
y = 5
z = 3
w = -4

###############################################################################
# A soma é feita com o operador +
print("========== SOMA ==========")
soma1 = x + y
soma2 = x + z
print ( x, " + ", y, " = ", soma1 )
print ( x, " + ", z, " = ", soma2 )

###############################################################################
# A subtração é feita com o operador -
print("\n========== SUBTRAÇÃO ==========")
subtracao1 = x - y
subtracao2 = z - x
print ( x, " - ", y, " = ", subtracao1 )
print ( z, " - ", x, " = ", subtracao2 )

###############################################################################
# A multiplicação é feita com o operador *
print("\n========== MULTIPLICAÇÃO ==========")
multiplicacao1 = x * y
multiplicacao2 = x * w
print ( x, " * ", y, " = ", multiplicacao1 )
print ( x, " * ", w, " = ", multiplicacao2 )

###############################################################################
# A divisão é feita com o operador /
# note que a divisão retora um número de ponto flutuante
print("\n========== DIVISÃO ==========")
divisao1 = x / y
divisao2 = x / z
print ( x, " / ", y, " = ", divisao1 )
print ( x, " / ", z, " = ", divisao2 )

###############################################################################
# A divisão inteira é feita com o operador //
print("\n========== DIVISÃO INTEIRA ==========")
divisaoInteira1 = x // y
divisaoInteira2 = x // z
print ( x, " // ", y, " = ", divisaoInteira1 )
print ( x, " // ", z, " = ", divisaoInteira2 )

###############################################################################
# O resto é feito com o operador %
print("\n========== RESTO ==========")
resto1 = x % y
resto2 = x % z
print ( x, " % ", y, " = ", resto1 )
print ( x, " % ", z, " = ", resto2 )

###############################################################################
# A potência é feita com o operador **
print("\n========== POTÊNCIA ==========")
potencia1 = x ** y
potencia2 = y ** w
print ( x, " ** ", y, " = ", potencia1 )
print ( y, " ** ", w, " = ", potencia2 )