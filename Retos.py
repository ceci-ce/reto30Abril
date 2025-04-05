# 📌 1. RETO 30 DÍAS ABRIL: DIA 1 | Redondeo
# ------------------------------------------
# En Grado Superior las notas se tienen que poner como un número entero, así que un día podrás ser el profe de entornos
# y podrás disfrutar del placer de poner un 7 a un estudiante con un 7,49 en el examen.
# Desarrolla un algoritmo que, dado un número decimal, devuelve su resultado entero redondeado siguiendo estas normas:
# Todos los números decimales por debajo de ,5 se redondean a la baja.
# Los que tengan decimales desde ,5 a superior, se redondean al alza.
#
# Ejemplo:
# Si el usuario introduce 4,49, el programa debe devolver un 4
# Si el usuario introduce 9,5 el programa debe devolver un 10

import math
nota = float(input("¿Qué nota has sacado?")) # Convierte lo que escribe el usuario en decimales
if (nota - int(nota) >= 0.5): #int(nota) quita los decimales y nota - int(nota) da solo la parte decimal
    print(int(nota) + 1)
else:
    print(int(nota))

   # Entonces:
#-Si esa parte es mayor o igual a 0.5, redondea hacia arriba
#-Si es menor a 0.5, redondea hacia abajo
#Si la parte decimal es mayor o igual a 0.5, le suma 1. Si la parte es menor o igual a 0.5, solo muestra la parte entera