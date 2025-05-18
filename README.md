# ProyectoArboles
###Universidad industrial de Santander
**Materia:**Estructura de datos y analisis de algoritmos
**Fecha de entrega:**15/04/2025

## Integrantes:

- Kevin David Basto Quintero 2222974
- Andres Santiago Culman Sanchez 2241929

## Contexto del problema
El proyecto consiste en modelar el recorrido de un camión de valores por diferentes direcciones(bancos  y cajeros). En la primera entrega, se utiizó una lista doblemente enlazada para representar las rutas. En la segunda entrega, se optimizó el sistema usando árboles, lo cual permite una estructura más jerárquica y eficiente para representar y gestionar las rutas a partir de la posición inicial del camión como nodo raíz.

## Primera entrega
En esta entrega se desarrolló un programa con listas doblemente enlazadas, donde cada nodo representa una dirección. Estas fueron las funciones que fueron implementadas:
*Insertar direcciones
*Eliminar direcciones
*Contar elementos
*Buscar una dirección
*Imprimir lista

## Limitaciones
*No es posible establecer jerarquías
*No hay una forma clara de representar rutas o niveles
*Requiere  más maneejo manual de los punteros para operaciones complejas

## Segunda entrega
Se migró la lógica de rutas a una estructura de arbol no binario, lo que permite una mejor organización jejerárquica a partir de la raíz (posición del camión). Para esto se usó a libería bigtree

### Funciones implementadas
*calcularPadre(): Asigna nodos (bancos/cajeros) como hijos e la raíz según la distancia desde el camión. Esta función structura el arbol dinamicamente.
*contarElementos(): Devuelve la cantidad de direcciones (nodos) que debe visitar el camión.
*contarNiveles(): Agrupa las direcciones por nivel(es decir, distancia) y muestra cuántas hay por cada uno
*rutaDireccion(): Muestra la ruta desde la raíz hasta la dirección deseada
*buscarDireccion(): Verifica si una dirección esta en el recorrido del camión
*impresionRuta(): Muestra el árbol completo con o sin detalles como distancia o dirección exacta

### Funcionalidad nueva (Mejora con árboles)
La funcionalidad especial calcularPadre() permite organizar automáticamente los destinos del camión en función de su distancia. Esta lógica no era posible en la versión con listas y representa una mejora importante al modelo de datos, ya que:
*Agrupa por cercanía
*Permite una mejor planificación de ruta
*Facilita búsquedas jerárquicas y visualizaciones

### Tecnologías utilizadas
*Python 3.10+
*bigtree -- Para la gestión de estructuras de árbol