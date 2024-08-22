#Leia a altura e o raio de cum cilindro circular e imprima o volume do cilindro. O volume de um cilindro circular é calculado por meio da seguinte fórmula: V = π * raio² * altura, onde π = 3.141592

alt = float(input("Insira a altura do cilindro: "))
raio = float(input("Insira o raio do cilindro: "))

volume = 3.14 * (raio ** 2) * alt

print(f"O volume do cilindro é {volume}.")