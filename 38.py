#Leia o salário de um funcionário. Calcule e imprima o valor do novo salário, sabendo que ele recebeu um aumento de 25%

salario = float(input("Insira seu salário atual: R$"))

valAumento = salario * 0.25
novoSalario = salario + valAumento

print(f"Seu novo salário é de R$ {novoSalario}.")