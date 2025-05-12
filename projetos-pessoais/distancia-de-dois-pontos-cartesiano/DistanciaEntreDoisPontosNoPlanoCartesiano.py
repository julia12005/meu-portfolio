import math
print("_____________________________________")
print(" Calculadora de distância entre dois ")
print("     pontos no plano cartesiano.     ")
print("_____________________________________")
x1=float(input("Digite a coordenada x do primeiro ponto:"))
y1=float(input("Digite a coordenada y do primeiro ponto:"))
x2=float(input("Digite a coordenada x do segundo ponto:"))
y2=float(input("Digite a coordenada y do segundo ponto:"))
if x1==x2 and y1==y2:
    print("Os dois pontos são iguais, a distância é 0.")
else:
    distancia=math.sqrt((x2-x1)**2+(y2-y1)**2)
    print(f"A distância entre os dois pontos é:{distancia:.2f}.")




































