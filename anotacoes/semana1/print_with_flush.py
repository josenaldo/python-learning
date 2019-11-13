# Programa que mostra uma contagem na tela. 
import time

num_seconds = 3

print ('Contagem bufferizada aparece toda de uma vez')
for countdown in reversed(range(num_seconds + 1)):
    if countdown > 0:
        print(countdown, end='...')
        time.sleep(1)
    else:
        print('Go!')


print ('Contagem não bufferizada aparece graualmente')
for countdown in reversed(range(num_seconds + 1)):
    if countdown > 0:
        print(countdown, end='...', flush=True)
        time.sleep(1)
    else:
        print('Go!')