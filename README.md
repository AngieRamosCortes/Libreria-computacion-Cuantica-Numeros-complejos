# Libreria-computacion-Cuantica-Numeros-complejos
2024-2 CNYT-2 LAB1 Librería computación Cuántica: Números complejos 

# Librería de Operaciones con Números Complejos

## Descripción
Esta librería proporciona una serie de funciones para realizar operaciones con números complejos, incluyendo suma, resta, producto, división, módulo, conjugado, conversión entre formas cartesiana y polar, y cálculo de la fase.

## Funciones
- `suma(a, b)`: Retorna la suma de dos números complejos `a` y `b`.
- `resta(a, b)`: Retorna la resta de dos números complejos `a` y `b`.
- `producto(a, b)`: Retorna el producto de dos números complejos `a` y `b`.
- `division(a, b)`: Retorna la división de dos números complejos `a` y `b`.
- `modulo(a)`: Retorna el módulo de un número complejo `a`.
- `conjugado(a)`: Retorna el conjugado de un número complejo `a`.
- `cartesiano_a_polar(a)`: Convierte un número complejo `a` de forma cartesiana a polar.
- `polar_a_cartesiano(p)`: Convierte un número complejo `p` de forma polar a cartesiana.
- `fase(a)`: Retorna la fase de un número complejo `a`.

## Pruebas Automáticas
Las pruebas automáticas para esta librería se han implementado utilizando el framework `unittest` de Python. Las pruebas cubren todas las funciones mencionadas anteriormente.

## Ejemplo de Uso
En el archivo .py llamado "libreriaComplejos" se encuentran los diferentes métodos correspondientes en donde se puede evidenciar la lógica que se utilizó para desarrollar la operación.

    import math
    def suma(a, b):
        return (a[0] + b[0], a[1] + b[1])  #sumo reales con reales e img con img
y su respectiva prueba en el archivo de pruebas automáticas de la librería "pruebasUnitextComplejos" usando el framework de pruebas unittest de Python (https://docs.python.org/3/library/unittest.html) 

    def test_suma(self):
        self.assertEqual(lc.suma((1, 2), (3, 4)), (4, 6))        #assertEqual: compara la primera parte con la segunda que sean iguales
        self.assertEqual(lc.suma((-1, -2), (1, 2)), (0, 0))


## Requisitos
- Python 3.x
- Módulo math (incluido en la biblioteca estándar de Python)
- framework de pruebas unittest de Python (https://docs.python.org/3/library/unittest.html) 

## Instalación
Si aún no se tiene instalada una versión mayor o igual a 3.5 del programa Python, se deberá realizar la respectiva instalación. En este espacio se puede encontrar la versión y el programa antes mencionado https://www.python.org/downloads/ .

## Construido con
- Visual Studio Code

## Autor
Angie Julieth Ramos Cortes

## Licencia
Este proyecto está bajo la Licencia MIT.
