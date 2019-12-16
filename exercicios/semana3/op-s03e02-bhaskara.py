import math

# Programa que calcula as raízes reais de uma equação de segundo grau usando a fórmula de bhaskara
# Referência para o método: https://brasilescola.uol.com.br/matematica/formula-bhaskara.htm
def main():
    print('Bem vindo ao programa de cálculo de raízes reais para uma equação de segundo grau')
    print('A equeção tem o formato "ax^2 + bx + c = 0')    
    a = float(input('Informe o "a" da equação: '))    
    b = float(input('Informe o "b" da equação: '))
    c = float(input('Informe o "c" da equação: '))

    # calcula o delta
    delta = b**2 - 4*a*c
    
    # se delta > 0    
    if delta > 0:        
        x1 = (-b + math.sqrt(delta))/(2*a)
        x2 = (-b - math.sqrt(delta))/(2*a)
        if x1 <= x2:
            print(f'as raízes da equação são {x1:.1f} e {x2:.1f}')
        else:
            print(f'as raízes da equação são {x2:.1f} e {x1:.1f}')    
    elif delta == 0:
        x = (-b + math.sqrt(delta))/(2*a)
        print(f'a raiz desta equação é {x}')        
    else:
        print(f'esta equação não possui raízes reais')

#-----------------------------------------------
# a linha a seguir inicia a execução do programa
main()