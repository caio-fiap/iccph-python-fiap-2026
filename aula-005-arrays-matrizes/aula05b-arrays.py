lista_frutas = ["Maca", "Pera", "Tomate"]

print(lista_frutas[0])

lista_frutas.append("Laranja")
print(lista_frutas[3])
print()

for i in range(len(lista_frutas)):
    print(lista_frutas[i])

print()

for fruta in lista_frutas:
    print(fruta)

print()

for i, fruta in enumerate(lista_frutas):
    print(i, fruta)
