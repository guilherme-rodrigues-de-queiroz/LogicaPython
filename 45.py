#Faça um programa para converter uma letra maiúscula em minúscula

letra = input("Digite uma letra maiúscula: ")

if letra == letra.lower():
  print("Digite uma letra maiúscula!")
else:
  print(letra.lower()[:1])