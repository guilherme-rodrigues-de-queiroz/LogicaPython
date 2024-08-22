#Sejam a e b os catetos de um triângulo, onde a hipotenusa é obtida pela equação: hipotenusa = √a² + b². Faça um programa que receba os valores de a e b, e calcule o valor da hipotenusa através da equação. Imprima o resultado dessa operação

a = float(input("Insira o valor do cateto a: "))
b = float(input("Insira o valor do cateto b: "))

soma = a ** 2 + b ** 2
hip = soma ** (1/2)

print(f"O resultado é {hip}.")