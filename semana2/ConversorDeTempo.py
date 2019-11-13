entrada = input("Informe o tempo, em segundos: ");
tempoEmSegundos = int(entrada)

dias = tempoEmSegundos // (24 * 3600)
segundosRestantes = tempoEmSegundos % (24 * 3600)

horas = segundosRestantes // 3600
segundosRestantes = segundosRestantes % 3600

minutos = segundosRestantes // 60
segundos = segundosRestantes % 60

print("%d dias, %02d:%02d:%02d" %(dias, horas, minutos, segundos))