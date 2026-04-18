#Contar cuántas casillas tiene el recorrido
print("\nEjercicio 2")
FilaInicial= int(input("\nIngrese el valor de la fila inicial: "))
ColumnaInicial= int(input("Ingrese el valor de la columna inicial: "))
FilaFinal= int(input("Ingrese el valor de la fila final: "))
ColumnaFinal= int(input("Ingrese el valor de la columna final: "))
recorrido = 0

if FilaInicial == FilaFinal and ColumnaInicial != ColumnaFinal:
    msj1 = "El desplazamiento es horizontal"

    if ColumnaInicial != ColumnaFinal and ColumnaInicial <= ColumnaFinal:

        while ColumnaInicial <= ColumnaFinal:
            ColumnaInicial+=1
            recorrido+=1

    else:

        while ColumnaInicial >= ColumnaFinal:
            ColumnaInicial-=1
            recorrido+=1
                    
elif ColumnaInicial == ColumnaFinal and FilaInicial != FilaFinal:
    msj1 = "El desplazamiento es vertical"

    if FilaInicial != FilaFinal and FilaInicial <= FilaFinal:        

        while FilaInicial <= FilaFinal:
            FilaInicial+=1
            recorrido+=1

    else:

        while FilaInicial >= FilaFinal:
            FilaInicial-=1
            recorrido+=1
                                    
elif FilaInicial == FilaFinal and ColumnaInicial == ColumnaFinal:
    msj1 = "El usuario no seleccionó ninguna celda"

else:
    msj1 = "El recorrido realizado no es válido para este avance"

print(f"{msj1}\nEl desplazamiento fue de {recorrido} casillas")