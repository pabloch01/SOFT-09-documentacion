Actividad 1. Mostrar el recorrido completo entre dos puntos

Descripción de la actividad
El programa debe solicitar al usuario una posición inicial y otra final dentro de
una sopa de letras. Con esos datos, el programa debe determinar si el recorrido es
horizontal o vertical. Si lo es, debe mostrar todas las coordenadas recorridas, una por
una, desde el punto inicial hasta el punto final. Si el recorrido no es horizontal ni vertical,
el programa debe indicar que no es válido para este avance.

Datos de entrada
● fila inicial
● columna inicial
● fila final
● columna final

Qué debe hacer el programa
1. Leer las cuatro coordenadas.
2. Verificar si el recorrido es horizontal o vertical.
3. Si el recorrido es horizontal: la fila inicial y la fila final deben ser iguales, y el programa debe
recorrer las columnas desde el inicio hasta el final.
4. Si el recorrido es vertical: la columna inicial y la columna final deben ser iguales, y el programa
debe recorrer las filas desde el inicio hasta el final.
5. En cada paso debe mostrar la coordenada que se está recorriendo.
6. Si el recorrido no es horizontal ni vertical, debe mostrar un mensaje de error.

Ejemplo orientador 1
Entrada del usuario:
- fila inicial: 2
- columna inicial: 3
- fila final: 2
- columna final: 6
Salida esperada:
- El recorrido es horizontal.
- Coordenadas recorridas:
(2,3)
(2,4)
(2,5)
(2,6)
Explicación del ejemplo:
La fila no cambia; siempre es 2. Lo único que cambia es la columna, que va de 3 hasta 6.
Por eso el programa debe ir avanzando columna por columna e imprimir cada posición.

Ejemplo orientador 2
Entrada del usuario:
- fila inicial: 5
- columna inicial: 4
- fila final: 2
- columna final: 4
Salida esperada:
- El recorrido es vertical.
- Coordenadas recorridas:
(5,4)
(4,4)
(3,4)
(2,4)
Explicación del ejemplo:
La columna no cambia; siempre es 4. Lo que cambia es la fila, que en este caso va bajando
de 5 a 2. Por eso el programa debe avanzar fila por fila hasta llegar al destino.

Ejemplo orientador 3
Entrada del usuario:
- fila inicial: 1
- columna inicial: 1
- fila final: 3
- columna final: 4
Salida esperada:
- El recorrido no es válido para este avance.
