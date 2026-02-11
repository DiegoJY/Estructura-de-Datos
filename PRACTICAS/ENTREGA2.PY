Calificaciones = [8, 8, 7, 5, 10, 9, 9, 5, 6, 10]

suma = 0
for i in range (len(Calificaciones)):
    suma += Calificaciones[i]

PromedioGen = suma / len(Calificaciones)
print("Promedio General del grupo:", PromedioGen)

AlumnosAprob = 0
for i in range (len(Calificaciones)):
    if Calificaciones[i] >= 6:
        AlumnosAprob += 1
print("Alumnos Aprobados:",AlumnosAprob)

AlumnosRep = 0
for i in range (len(Calificaciones)):
    if Calificaciones[i] < 6:
        AlumnosRep += 1
print("Alumnos reprobados:", AlumnosRep)

Aprobados = AlumnosAprob / len(Calificaciones) * 100
print(Aprobados, "% Son los alumnos Aprobados")

Reprobados = AlumnosRep / len(Calificaciones) * 100
print(Reprobados, "% Son los alumnos Reprobados")

CalificacionMayor8 = 0
for i in range(len(Calificaciones)):
    if Calificaciones[i] >= 8:
        CalificacionMayor8 += 1
print("Alumnos con calificacion mayor o igual a ocho:", CalificacionMayor8)