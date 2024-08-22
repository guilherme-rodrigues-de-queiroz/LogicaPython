#Faça um programa que leia o valor de um produto e imprima o valor do novo salário, tendo em vista que o desconto foi de 12%

produto = float(input("Insira o valor do produto: "))

valDesc = produto * 0.12
valorTotal = produto - valDesc

print(f"O valor do produto com desconto aplicado é igual a {valorTotal}.")