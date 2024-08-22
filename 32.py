#Leia um número inteiro e imprima a soma do sucessor de seu triplo com o antecessor de seu dono

n1 = float(input("Insira um número: "))

suc = n1 * 3 + 1
ant = n1 * 2 - 1
res = suc + ant

print(f"O resultado é igual a {res}.")