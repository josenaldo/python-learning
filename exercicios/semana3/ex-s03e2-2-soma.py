# Exercício 2.2
# Dada uma sequência de números inteiros diferentes de zero, terminada por
# um zero, calcular a sua soma. Por exemplo, para a sequência:
# 12   17   4   -6   8   0
# o seu programa deve escrever o número 35.
# link: https://panda.ime.usp.br/aulasPython/static/aulasPython/aula02.html

def main():
    numero = int(input('Informe um número: '))
    soma = 0

    while numero != 0:
        soma += numero
        numero = int(input('Informe um número: '))

    print(f'A soma dos números informados é: {soma}')

#-----------------------------------------------
# a linha a seguir inicia a execução do programa
main()