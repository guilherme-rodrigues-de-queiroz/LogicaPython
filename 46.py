#Faça um programa que leia um número inteiro positivo de três dígitos (de 100 a 999). Gere outro número formado pelos dígitos invertidos do número lido.

n = int(input("Digite um valor positivo entre 100 e 999: "))

if n <= 999 and n >= 100:
  lerN = str(n)
  print(lerN[::-1])
else:
  print("Digite o valor corretamente!")