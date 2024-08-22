#Receba a altura do degrau de uma escada e a altura que o usuário deseja alcançar subindo a escada. Calcule e mostre quantos degraus o usuário deverá subir para atingir seu objetivo

H = float(input("Digite a altura do degrau em metros: "))
A = float(input("Digite a altura que você deseja subir em metros: "))

calculo = A/H

print(f"Você deverá subir {int(calculo)} degraus para chegar a altura de {A} metros.")