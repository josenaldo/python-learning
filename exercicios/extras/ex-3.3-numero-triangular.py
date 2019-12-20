# Exercício 3.3
# Nota: Exercício 10 da lista sobre inteiros.
#
# Dizemos que um número inteiro positivo é triangular se ele é o produto de
# três numeros inteiros consecutivos. Por exemplo, 120 é triangular, pois
#
#  >>> 4 * 5 * 6 
# 120
# 
# Dado um número inteiro positivo n, verificar se n é triangular.
# Link: https://panda.ime.usp.br/aulasPython/static/aulasPython/aula03.html

def main():
    n = 336
    i = 1
    resultado = i * (i + 1) * (i + 2)
    ehTriangular = False

    while resultado <= n:
        if resultado == n:
            ehTriangular = True
            break
        else:
            ehTriangular = False
        
        i += 1
        resultado = i * (i + 1) * (i + 2)

    if(ehTriangular):
        print(f'O número {n} é triangular e é resultado de {i} * {i + 1} * {i + 2}')
    else:
        print(f'O número {n} não é triangular')

#-----------------------------------------------
# a linha a seguir inicia a execução do programa
main()