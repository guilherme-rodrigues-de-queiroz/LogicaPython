#Leia um valor real e a cotação do dólar. Em seguida, imprima o valor correspondente em dólares

n1 = float(input("Digite o valor em R$: "))
n2 = float(input("Digite a cotação do dólar: "))

cambio = (n1/n2)

print(f"O valor em dólares é {cambio}")