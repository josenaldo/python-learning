def main():
    
    n = int(input('Informe o número: '))
    k = int(input('Informe a potência: '))

    while( k < 1):
        print (f'O valor {k} é inválido. Informe um número maior ou igual a 1.')
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