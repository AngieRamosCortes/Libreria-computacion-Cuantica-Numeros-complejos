#Autor: Angie Julieth Ramos Cortes
#CNYT-2. Tarea1. Librería computación Cuántica: Números complejos
#Operaciones básicas Complejos
#21/08/24

import math

def suma(a, b):
    return (a[0] + b[0], a[1] + b[1])  #sumo reales con reales e img con img

def resta(a, b):
    return (a[0] - b[0], a[1] - b[1])

def producto(a, b):
    real = a[0] * b[0] - a[1] * b[1]
    imag = a[0] * b[1] + a[1] * b[0]
    return (real, imag)

def division(a, b):
    divisor = b[0]**2 + b[1]**2
    real = (a[0] * b[0] + a[1] * b[1]) / divisor
    imag = (a[1] * b[0] - a[0] * b[1]) / divisor
    return (real, imag)

def modulo(a):
    return math.sqrt(a[0]**2 + a[1]**2)

def conjugado(a):
    return (a[0], -a[1])

def cartesianoAPolar(a):
    modulo = math.sqrt(a[0]**2 + a[1]**2)
    fase = math.atan2(a[1], a[0])
    return (modulo, fase)

def polarACartesiano(p):
    real = p[0] * math.cos(p[1])
    imag = p[0] * math.sin(p[1])
    return (real, imag)

def fase(a):
    return math.atan2(a[1], a[0])
