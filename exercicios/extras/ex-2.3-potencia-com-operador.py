# Dados números inteiros n e k, com k >= 0, calcular n elevado a k. Por exemplo,
# dados os números 3 e 4 o seu programa deve escrever o número 81.
# Link: https://panda.ime.usp.br/aulasPython/static/aulasPython/aula02.html

def main():
    n = int(input('Informe um número inteiro: '))
    k = int(input('Informe a potência (um valor inteiro maior ou igual a 0): '))

    potencia = n ** k

    print(f'Pontência é igual a {potencia}')


#-----------------------------------------------
# a linha a seguir inicia a execução do programa
main()