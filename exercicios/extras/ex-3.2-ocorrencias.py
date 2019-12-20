# Dados um número inteiro n, n > 0, e um dígito d. 0 <= d <= 9, determinar 
# quantas vezes d ocorre em n.
# Link: https://panda.ime.usp.br/aulasPython/static/aulasPython/aula03.html

def main():
    ocorrencias = 0
    
    n = int(input('Informe o número: '))
    d = int(input('Informe o dígito (0-9): '))
    resto = n

    while d < 0 or d > 9:
        d = int(input('Informe o dígito (0-9): '))

    numeroDeDigitos = 1

    while (10 ** numeroDeDigitos < n ):
        numeroDeDigitos += 1
    
    numeroDeDigitos -= 1

    while(numeroDeDigitos >0):
        digito = resto // (10 ** numeroDeDigitos)
        resto = resto % (10 ** numeroDeDigitos)
        if digito == d:
            ocorrencias += 1
        
        numeroDeDigitos -= 1
    
    print(f'Número de vezes em que o dígito {d} aparece em {n}: {ocorrencias}')   

#-----------------------------------------------
# a linha a seguir inicia a execução do programa
main()