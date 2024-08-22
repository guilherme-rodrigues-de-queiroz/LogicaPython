#Faça um programa que leia o valor da hora de trabalho (em reais) e número de horas trabalhadas no mês. Imprima o valor a ser pago ao funcionário, adicionando 10% sobre o valor calculado

valor = float(input("Digite o valor da hora de trabalho em R$: "))
horas = int(input("Digite o tanto de horas trabalhadas no mês: "))

salario = (valor*horas) + ((valor*horas)*0.1)

print(f"O valor a ser pago é de R$ {salario}")