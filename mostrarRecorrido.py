#Mostrar el recorrido completo entre dos puntos
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