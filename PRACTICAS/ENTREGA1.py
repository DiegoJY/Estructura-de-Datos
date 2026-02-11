arreglo = [12, 24, 16, 15, 20, 18, 6, 10, 12, 11, 15, 12]

# Sacar el promedio del arreglo
suma = 0
for i in range(len(arreglo)):
    suma += arreglo[i]

print("Suma total de todos los elementos en el array:", suma)

promedio = suma / len(arreglo)          # En Python 3 la división ya es float
print("Promedio Total del arreglo:", promedio)

# Contar valores mayores
valores_mayores = 0
for i in range(len(arreglo)):
    if arreglo[i] > promedio:
        valores_mayores += 1

print("Valores Mayores al promedio:", valores_mayores)

# Crear lista con valores superiores
val_sup = [0] * valores_mayores   # lista del tamaño necesario
count1 = 0
for i in range(len(arreglo)):
    if arreglo[i] > promedio:
        val_sup[count1] = arreglo[i]
        count1 += 1

print("Lista con valores superiores al promedio:", val_sup)

# Contar valores menores
valores_menores = 0
for i in range(len(arreglo)):
    if arreglo[i] < promedio:
        valores_menores += 1

# Crear lista con valores inferiores
val_inf = [0] * valores_menores
count2 = 0
for i in range(len(arreglo)):
    if arreglo[i] < promedio:
        val_inf[count2] = arreglo[i]
        count2 += 1

print("Lista con valores inferiores al promedio:", val_inf)