#Uma empresa contrata um encanador a R$ 30,00 por dia. Faça um programa que solicite o número de dias trabalhados pelo encanador e imprima a quantia líquida que deverá ser paga, sabendo-se que são descontados 8% para imposto de renda

D = int(input("Digite quantos dias você trabalhou: "))

salario = (30*D) - ((30*D)*0.08)

print(f"Seu salário líquido será de R$ {salario}")