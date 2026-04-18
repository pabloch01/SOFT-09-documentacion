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

Qué debe hacer el programa

1. Leer las cuatro coordenadas.
2. Verificar si el recorrido es horizontal o vertical.
3. Si el recorrido es válido: recorrer paso a paso desde el inicio hasta el final, contar cada casilla
recorrida y mostrar la cantidad total de casillas recorridas.
4. Si el recorrido no es horizontal ni vertical, debe mostrar un mensaje que indique que no es
posible calcular la cantidad para este avance.

Ejemplo orientador 1
Entrada del usuario:
- fila inicial: 4
- columna inicial: 2
- fila final: 4
- columna final: 7
Salida esperada:
- El recorrido es horizontal.
- Cantidad de casillas recorridas: 6
Explicación del ejemplo:
Las coordenadas serían: (4,2), (4,3), (4,4), (4,5), (4,6), (4,7). Son 6 casillas en total. Es
importante recordar que se cuenta tanto la posición inicial como la final.

Ejemplo orientador 2
Entrada del usuario:
- fila inicial: 6
- columna inicial: 3
- fila final: 2
- columna final: 3
Salida esperada:
- El recorrido es vertical.
- Cantidad de casillas recorridas: 5
Explicación del ejemplo:
Las coordenadas serían: (6,3), (5,3), (4,3), (3,3), (2,3). Hay 5 casillas.

Ejemplo orientador 3
Entrada del usuario:
- fila inicial: 2
- columna inicial: 2
- fila final: 5
- columna final: 6
Salida esperada:
- El recorrido no es válido para este avance.
