import math

def main():
    print('Bem vindo ao programa de cálculo de raízes reais para uma equação de segundo grau')
    print('A equeção tem o formato "ax^2 + bx + c = 0')    
    a = float(input('Informe o "a" da equação: '))    
    b = float(input('Informe o "b" da equação: '))
    c = float(input('Informe o "c" da equação: '))

    # calcula o delta
    delta = b**2 - 4*a*c
    print(f'delta = {delta}')

    # se delta > 0    
    if delta > 0:        
        x1 = (-b + math.sqrt(delta))/(2*a)
        x2 = (-b - math.sqrt(delta))/(2*a)
        print(f'x1 = {x1} e x2={x2}')
    # senao se delta = 0
    elif delta == 0:
        x = (-b + math.sqrt(delta))/(2*a)
        print(f'x = {x}')        
    else:
        print(f'Essa equação não apresenta raízes reais')

#-----------------------------------------------
# a linha a seguir inicia a execução do programa
main()