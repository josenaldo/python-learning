# Dados números inteiros n e k, com k >= 0, calcular n elevado a k. Por exemplo, 
# dados os números 3 e 4 o seu programa deve escrever o número 81.
# Link: https://panda.ime.usp.br/aulasPython/static/aulasPython/aula02.html

def main():
    
    n = int(input('Informe o número: '))
    k = int(input('Informe a potência: '))

    while( k < 0):
        print (f'O valor {k} é inválido. Informe um número maior ou igual a 0.')
        k = int(input('Informe a potência: '))
    
    i = 0
    resultado = 1;

    while(i < k):
        resultado = resultado * n;
        i = i + 1;

    print(f'{n}^{k}={resultado}')


#-----------------------------------------------
# a linha a seguir inicia a execução do programa
main()