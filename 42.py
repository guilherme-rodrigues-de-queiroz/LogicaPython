#Receba o salário-base de um funcionário. Calcule e imprima o salário a receber, sabendo-se que esse funcionário tem uma gratificação de 5% sobre o salário-base. Além disso, ele paga 7% de imposto sobre o salário-base

salario = float(input("Digite o valor do salário-base: "))

receba = salario + (salario*0.05) - (salario*0.07)

print(f"O salário a receber será de R$ {receba}")