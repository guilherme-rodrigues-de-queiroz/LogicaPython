#Implemente um programa que calcule o ano de nascimento de uma pessoa a partir de sua idade e do ano atual

idade = int(input("Digite sua idade: "))
ano = int(input("Que ano estamos: "))

anoNascimento = ano-idade

print(f"Estamos em {ano}, você tem {idade} anos e nasceu em {anoNascimento}.")