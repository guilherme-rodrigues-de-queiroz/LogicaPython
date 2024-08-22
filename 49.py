#Faça um programa que leia o horário (hr, min, seg) de inicio e a duração, em segundos, de uma experiência biológica. O programa deve resultar com o novo horário (hr, min, seg) do término da mesma

h = int(input("Digite o tempo em horas de inicio da experiência: "))
m = int(input("Digite o tempo em minutos de inicio da experiência: "))
s = int(input("Digite o tempo sem segundos de inicio da experiência: "))
duracao = int(input("Digite o tempo de duração em segundos da experiência: "))

# somando a hora com a conversão de segundos em horas utilizando divisão inteira
h = h + (duracao//3600)

# pegando o resto
duracao %= 3600

# somando os minutos com a conversão de segundos para minutos utilizando divisão inteira
m = m + (duracao//60)

# somando os segundos com o resto
duracao %= 60
s = s + duracao

print(f"O horário do término da experiência é de {h} hora(s), {m} minuto(s) e {s} segundo(s)")