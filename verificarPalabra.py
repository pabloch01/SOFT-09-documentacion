#Verificar si una palabra pertenece al conjunto de palabras del juego
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