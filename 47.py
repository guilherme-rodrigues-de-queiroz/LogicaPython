#Leia um número inteiro de 4 dígitos (de 1000 a 9999) e imprima 1 digito por linha.

n = int(input("Digite um valor positivo entre 1000 e 9999: "))

if n <= 9999 and n >= 1000:
  lerN = str(n)
  print(lerN[:1])
  print(lerN[1:2])
  print(lerN[2:3])
  print(lerN[3:4])
else:
  print("Digite o valor corretamente!")