# Reporte del Analizador Léxico Simple

## 1. Introducción

Este proyecto consiste en un analizador léxico simple desarrollado en Python. Su objetivo es procesar una cadena de código fuente y descomponerla en una secuencia de componentes léxicos llamados **tokens**. Cada token representa una unidad indivisible del lenguaje, como una palabra clave, un identificador, un número o un operador.

El analizador se construyó utilizando expresiones regulares para definir los patrones de cada tipo de token y un bucle principal que recorre el código fuente para encontrar coincidencias.

## 2. Evolución y Cambios Realizados

El script inicial tenía la lógica básica para la tokenización, pero requería varias mejoras para ser más funcional, robusto y legible. A continuación, se detallan los cambios implementados.

### 2.1. Mejora en la Visualización de Tokens

**Problema:** Al imprimir los tokens generados, se mostraba la representación genérica de los objetos `Token` de Python (ej. `<__main__.Token object at 0x...`), lo cual no era informativo.

**Solución:**
1.  **Método `__str__`:** Se añadió un método `__str__` a la clase `Token`. Este método especial de Python permite definir una representación en formato de cadena para un objeto, facilitando su depuración.
2.  **Formato de Tabla:** Se modificó el bucle de impresión al final del script para presentar los tokens en un formato de tabla alineada. Esto se logró usando f-strings y especificando el ancho de las columnas (`f"{token.tipo:<15}"`), mejorando drásticamente la legibilidad de la salida.

### 2.2. Corrección de Secuencias de Escape en Expresiones Regulares

**Problema:** Las expresiones regulares que contenían barras invertidas (`\`) no usaban el formato de "cadena cruda" (raw string). Esto puede causar que Python interprete la barra invertida como un carácter de escape antes de que la cadena llegue al motor de expresiones regulares.

**Solución:**
Se antepuso una `r` a todas las cadenas de patrones de expresiones regulares (ej. `r'\d+'` en lugar de `'\d+'`). Esto le indica a Python que no procese las secuencias de escape, pasando la cadena "cruda" directamente al motor de regex. Esto hace que los patrones sean más seguros y predecibles.

### 2.3. Corrección de Patrones de Expresiones Regulares

**Problema:** Los patrones para `KEYWORD` e `IDENTIFIER` contenían errores que impedían que reconocieran correctamente las palabras clave y los nombres de variables.

**Solución:**
1.  **`KEYWORD`**: El patrón original `r'\b(if while for return|int|float)\b'` era incorrecto porque no separaba todas las palabras clave con el operador `|` (OR). Se corrigió a `r'\b(if|while|for|return|int|float)\b'`.
2.  **`IDENTIFIER`**: El patrón `r' [a-zA-Z_] [a-zA-Z0-9_]*'` contenía espacios que no permitían reconocer identificadores como `x` o `mi_variable`. Se corrigió a `r'[a-zA-Z_][a-zA-Z0-9_]*'`, eliminando los espacios.

## 3. Explicación del Código Final

El script final se compone de dos clases principales: `Token` y `AnalizadorLexico`.

### 3.1. Clase `Token`

Es una clase simple que actúa como un contenedor de datos para cada token.

```python
class Token:
    def __init__(self, tipo, valor, Linea):
        self.tipo = tipo      # Ej: 'KEYWORD', 'IDENTIFIER'
        self.valor = valor    # Ej: 'int', 'x'
        self.linea = Linea    # Número de línea donde se encontró
```

### 3.2. Clase `AnalizadorLexico`

Esta es la clase principal que realiza el análisis léxico.

-   **`__init__(self, codigo)`**: El constructor inicializa el analizador con el código fuente a procesar, un puntero de posición (`self.pos`) y un contador de línea (`self.linea`).

-   **`self.patrones`**: Es una lista de tuplas donde cada tupla contiene el `tipo` de token y su `patrón` de expresión regular. **El orden en esta lista es crucial**:
    -   `KEYWORD` va antes que `IDENTIFIER` para que palabras como `if` o `int` sean reconocidas como palabras clave y no como identificadores genéricos.
    -   `WHITESPACE` y `NEWLINE` se identifican para poder ignorarlos y para actualizar el contador de línea.
    -   `ERROR` va al final para capturar cualquier carácter que no coincida con los patrones anteriores.

-   **`tokenizar(self)`**: Este es el método central del analizador.
    1.  Inicia un bucle `while` que se ejecuta mientras no se haya recorrido todo el código (`self.pos < len(self.codigo)`).
    2.  Dentro del bucle, itera sobre la lista `self.patrones`.
    3.  Para cada patrón, intenta hacer una coincidencia (`regex.match()`) desde la posición actual (`self.pos`).
    4.  Si encuentra una coincidencia:
        -   Extrae el valor del token (`match.group(0)`).
        -   Si el token es `NEWLINE`, incrementa el contador de línea.
        -   Si el token no es un espacio en blanco o una nueva línea, crea un objeto `Token` y lo añade a la lista de `tokens`.
        -   Actualiza la posición (`self.pos`) al final del token encontrado.
        -   Rompe el bucle interno y comienza una nueva búsqueda desde la nueva posición.
    5.  Si no se encuentra ninguna coincidencia para ningún patrón (lo cual no debería ocurrir gracias al patrón `ERROR`), avanza la posición en uno para evitar un bucle infinito.
    6.  Finalmente, devuelve la lista completa de `tokens` encontrados.

## 4. Conclusión

A través de una serie de mejoras iterativas, el script ha evolucionado desde un prototipo básico a un analizador léxico funcional y robusto. Las correcciones en la visualización, el uso de cadenas crudas y la depuración de las expresiones regulares han sido pasos clave para lograr un resultado preciso y fácil de interpretar.