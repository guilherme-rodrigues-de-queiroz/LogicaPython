#Leia um valor inteiro em segundos, e imprima-o em horas, minutos e segundos

t = int(input("Digite um valor em segundos: "))

# // para divisão inteira
h = t//3600

# pegando o valor de t e colocando dentro da variável 's'
s = t

# %= para pegar o resto da divisão
s %= 3600

m = s//60

s %= 60

print(f"{h} hora(s), {m} minuto(s) e {s} segundo(s)")