def main():
    numero = int(input('Informe um número: '))

    print(f'{"FizzBuzz" if (numero % 3 == 0 and numero % 5 == 0) else numero}')

#-----------------------------------------------
# a linha a seguir inicia a execução do programa
main()