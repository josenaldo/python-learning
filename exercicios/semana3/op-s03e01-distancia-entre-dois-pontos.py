import math

def main():
    x1 = float(input('Informe o x1: '))
    y1 = float(input('Informe o y1: '))
    x2 = float(input('Informe o x2: '))
    y2 = float(input('Informe o y2: '))

    distancia = math.sqrt(((x1 - x2) ** 2) + ((y1 - y2) ** 2))

    if(distancia > 10):
        print('longe')
    else:
        print('perto')

#-----------------------------------------------
# a linha a seguir inicia a execução do programa
main()