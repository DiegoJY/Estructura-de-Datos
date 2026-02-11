palabra = "Parangaricutirimicuaro"
conteo = {}
for i in palabra:
    if i in conteo:
        conteo[i] += 1
    else:
        conteo[i] = 1
for i, cantidad in conteo.items():
    print(f"{i}={cantidad}")
    

