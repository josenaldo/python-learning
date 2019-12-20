# Exercício 3.1
# Dados um número inteiro n, n > 0, e uma sequência com n números inteiros, 
# determinar quantos números da sequência são pares e quantos são ímpares. Por
# exemplo, para a sequência
# 
# 6   -2   7   0  -5   8  4
#
# o seu programa deve escrever o número 4 para o número de pares e 2 para o de ímpares.
#
# Dica: para resolver esse exercício utilize o operador “%”, que retorna o resto da divisão. Assim:
#
# 1 % 3 é 1
# 2 % 3 é 2
# 3 % 3 é 0
# 4 % 3 é 1
# https://panda.ime.usp.br/aulasPython/static/aulasPython/aula03.html

def main():
    numero = int(input('Informe um número: '))
    pares = 0
    impares = 0

    while numero != 0:
        if numero % 2 == 0:
            pares += 1
        else:
            impares += 1
        numero = int(input('Informe um número: '))

    print(f'número de pares:{pares} | número de ímpares: {impares}')

#-----------------------------------------------
# a linha a seguir inicia a execução do programa
main()
