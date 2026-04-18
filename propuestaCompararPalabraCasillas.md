Actividad 3. Comparar la longitud de una palabra con la cantidad de casillas disponibles

Descripción de la actividad
El programa debe pedir una palabra y la cantidad de casillas disponibles en un recorrido.
Esta cantidad de casillas debe ingresarla el usuario.
El objetivo de esta actividad es que el programa determine si la palabra cabe exactamente
en ese recorrido.
En esta actividad no se calcula el recorrido porque ese problema ya fue resuelto en una
actividad anterior. Aquí solo se analiza si la longitud de la palabra coincide con el número de
casillas disponibles.
Esta actividad permite practicar estructuras iterativas para contar las letras de una palabra.

Datos de entrada
● palabra a buscar
● cantidad de casillas del recorrido

Qué debe hacer el programa
1. Leer la palabra ingresada.
2. Calcular cuántas letras tiene la palabra recorriéndola con un ciclo y un contador. No se permite
usar la función len().
3. Leer la cantidad de casillas disponibles.
4. Comparar ambos valores.
5. Mostrar uno de los siguientes resultados: la palabra cabe exactamente en el recorrido, tiene más
letras que casillas o tiene menos letras que casillas.

Ejemplo orientador 1
Entrada del usuario:
palabra: CASA
casillas disponibles: 4
Salida esperada:
Longitud de la palabra: 4
Casillas disponibles: 4
Resultado: la palabra cabe exactamente en el recorrido.

Ejemplo orientador 2
Entrada del usuario:
palabra: COMPUTADORA
casillas disponibles: 5
Salida esperada:
Longitud de la palabra: 11
Casillas disponibles: 5
Resultado: la palabra no cabe en el recorrido porque tiene más letras que casillas.

Ejemplo orientador 3
Entrada del usuario:
palabra: SOL
casillas disponibles: 5
Salida esperada:
Longitud de la palabra: 3
Casillas disponibles: 5
Resultado: sobran casillas para la palabra.