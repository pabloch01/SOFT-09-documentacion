#Actividad 1 
print("Ejercicio 1")
filaInicial= int(input("\nIngrese el valor de la fila inicial: "))
columnaInicial= int(input("Ingrese el valor de la columna inicial: "))

filaFinal= int(input("Ingrese el valor de la fila final: "))
columnaFinal= int(input("Ingrese el valor de la columna final: "))


if filaInicial== filaFinal and columnaInicial != columnaFinal:
    print(f"\nEl recorrido es horizontal:\nCoordenadas recorridas:")
    
    if columnaInicial < columnaFinal:
        while columnaInicial <= columnaFinal:
            print(f"({filaInicial},{columnaInicial})")
            columnaInicial += 1
    else: 
        while columnaInicial >= columnaFinal:
            print(f"({filaInicial},{columnaInicial})")
            columnaInicial -= 1
            
elif columnaInicial == columnaFinal and filaInicial != filaFinal:
    print(f"\nEl desplazamiento es vertical:\nCoordenadas recorridas:")
    
    if filaInicial < filaFinal:
        while filaInicial <= filaFinal:
            print(f"({filaInicial},{columnaInicial})") 
            filaInicial += 1
    else:
        while filaInicial >= filaFinal:
            print(f"({filaInicial},{columnaInicial})") 
            filaInicial -= 1
else:
    print("El recorrido realizado no es válido para este avance")


#Actividad 2
print("\nEjercicio 2")
FilaInicial= int(input("\nIngrese el valor de la fila inicial: "))
ColumnaInicial= int(input("Ingrese el valor de la columna inicial: "))
FilaFinal= int(input("Ingrese el valor de la fila final: "))
ColumnaFinal= int(input("Ingrese el valor de la columna final: "))
recorrido = 0

if FilaInicial == FilaFinal and ColumnaInicial != ColumnaFinal:

    if ColumnaInicial != ColumnaFinal and ColumnaInicial <= ColumnaFinal:

        while ColumnaInicial <= ColumnaFinal:
            ColumnaInicial+=1
            recorrido+=1

    else:

        while ColumnaInicial >= ColumnaFinal:
            ColumnaInicial-=1
            recorrido+=1

    print(f"El desplazamiento es horizontal\nEl desplazamiento fue de {recorrido} casillas")
                    
elif ColumnaInicial == ColumnaFinal and FilaInicial != FilaFinal:

    if FilaInicial != FilaFinal and FilaInicial <= FilaFinal:        

        while FilaInicial <= FilaFinal:
            FilaInicial+=1
            recorrido+=1

    else:

        while FilaInicial >= FilaFinal:
            FilaInicial-=1
            recorrido+=1
    
    print(f"El desplazamiento es vertical\nEl desplazamiento fue de {recorrido} casillas")
                                    
elif FilaInicial == FilaFinal and ColumnaInicial == ColumnaFinal:
    print(f"El usuario no seleccionó ninguna celda\nEl desplazamiento fue de {recorrido} casillas")

else:
    print("El recorrido realizado no es válido para este avance")


#Actividad 3
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

#Actividad 4
print("\nEjercicio 4")
palabra1= "PYTHON"
palabra2= "CICLO"
palabra3= "CODIGO"
palabra4= "VARIABLE"
palabra5= "PROGRAMA"

continuar = "si"

while continuar.casefold() == "si":
    
    palabraUsuario= input("\nIngrese una palabra: ")
    palabraUsuario= palabraUsuario.upper()
    if (palabraUsuario.casefold() == palabra1.casefold() or palabraUsuario.casefold() == palabra2.casefold() or palabraUsuario.casefold() == palabra3.casefold() or palabraUsuario.casefold() == palabra4.casefold() or palabraUsuario.casefold() == palabra5.casefold() ):
        print("La palabra pertenece a la sopa de letras.")
        
    else:
        print("La palabra no pertenece a la sopa de letras.")
    
    
    print("¿Desea intentarlo nuevamente? (si/no)")
    continuar= input("Respuesta: ")
    continuar= continuar.upper() 

print("\nPrograma finalizado.")
