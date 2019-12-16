def main():
    numero = int(input('Informe um número: '))

    print(f'{"Buzz" if (numero % 5 == 0) else numero}')

#-----------------------------------------------
# a linha a seguir inicia a execução do programa
main()