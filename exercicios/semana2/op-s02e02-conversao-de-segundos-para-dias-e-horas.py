entrada = input("Por favor, entre com o número de segundos que deseja converter: ");
tempoEmSegundos = int(entrada)

dias = tempoEmSegundos // (24 * 3600)
segundosRestantes = tempoEmSegundos % (24 * 3600)

horas = segundosRestantes // 3600
segundosRestantes = segundosRestantes % 3600

minutos = segundosRestantes // 60
segundos = segundosRestantes % 60

print(f'{dias} dias, {horas} horas, {minutos} minutos e {segundos} segundos.')