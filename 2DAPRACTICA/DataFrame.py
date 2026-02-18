import pandas as pd

df = pd.read_csv('Housing.csv')

def calcular_media(lista_datos):
    suma = 0
    for valor in lista_datos:
        suma += valor
    return suma / len(lista_datos)

def calcular_varianza(lista_datos):
    media = calcular_media(lista_datos)
    suma_cuadrados = 0
    for valor in lista_datos:
        suma_cuadrados += (valor - media) ** 2
    return suma_cuadrados / len(lista_datos)

def calcular_moda(lista_datos):
    conteo = {}
    for valor in lista_datos:
        if valor in conteo:
            conteo[valor] += 1
        else:
            conteo[valor] = 1
    
    moda_final = None
    max_votos = 0
    for valor, frecuencia in conteo.items():
        if frecuencia > max_votos:
            max_votos = frecuencia
            moda_final = valor
    return moda_final



columnas_interes = [
    'price', 'bedrooms', 'bathrooms', 'sqft_living',
    'sqft_lot', 'floors', 'waterfront', 'view', 'condition',
    'grade', 'sqft_above', 'sqft_basement', 'yr_built', 'yr_renovated',
    'zipcode', 'lat', 'long', 'sqft_living15', 'sqft_lot15'
]

for col in columnas_interes:
    lista_datos = list(df[col])
    
    m = calcular_media(lista_datos)
    v = calcular_varianza(lista_datos)
    mo = calcular_moda(lista_datos)
    desviacion = v ** 0.5 
    
    print(f"--- Columna: {col} ---")
    print(f"Media: {m:.2f} | Moda: {mo} | Varianza: {v:.2f} | Desviación: {desviacion:.2f}")
    print("-" * 30)