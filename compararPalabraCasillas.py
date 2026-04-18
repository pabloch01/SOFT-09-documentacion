#Comparar la longitud de una palabra con la cantidad de casillas disponibles
print("\nEjercicio 3")
palabra = input("\nDigite la palabra: ")
casillas = int(input("ingrese la cantidad de casillas: "))

contador = 0

for letra in palabra:
    contador += 1

print(f"Longitud de la palabra: {contador}")    
print(f"Casillas disponibles: {casillas}")


if contador == casillas:
    print("Resultado:La palabra cabe exactamente en el recorrido.")

elif contador > casillas:
    print("Resultado: La palabra no cabe en el recorrido porque tiene más letras que casillas.")
    
else:
    print("Resultado: Sobran casillas para la palabra.")