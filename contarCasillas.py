#Contar cuántas casillas tiene el recorrido
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