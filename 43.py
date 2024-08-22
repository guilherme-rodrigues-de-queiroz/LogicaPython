#Escreva um programa de ajuda para vendedores. A partir de um valor total lido, mostre:
#- o total a pagar com 10% de desconto;
#- o valor de cada parcela, no parcelamento de 3x sem juros;
#- a comissão do vendedor, no caso da venda ser a vista (5% sobre o valor com desconto)
#- a comissão do vendedor, no caso da venda ser parcelada (5% sobre o valor total)

valor = float(input("Digite o valor do produto: "))

desc = valor - (valor*0.1)
parcela = valor/3
comissaoDesc = desc*0.05
comissaoParcela = valor*0.05

print(f"Caso queira pagar à vista, o valor total a pagar com desconto de 10% será de R$ {desc}")
print(f"Caso queira parcelar, o valor de cada parcela será de R$ {parcela}")
print(f"A comissão do vendedor, após venda à vista será de R$ {comissaoDesc}")
print(f"A comissão do vendedor, após venda parcelada será de R$ {comissaoParcela}")