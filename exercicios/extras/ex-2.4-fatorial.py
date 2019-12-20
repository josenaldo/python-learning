# Dado um número inteiro n >= 0, calcular n!.
# Link: https://panda.ime.usp.br/aulasPython/static/aulasPython/aula02.html

def main():
    n = int(input('Informe o valor de n: '))

    while(n < 0):
        print(f'Valor informado ({n}) é inválido. Favor informar um número maior ou igual a 0')
        n = int(input('Informe o valor de n: '))

    i = 1
    fatorial = 1

    while (i <= n):
        fatorial = fatorial * i
        i = i + 1

    print('%d!=%d' %(n, fatorial))


#-----------------------------------------------
# a linha a seguir inicia a execução do programa
main()