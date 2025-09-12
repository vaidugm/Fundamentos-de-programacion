calificaciones = []

for i in range(5):
    calificaciones.append(float(input(f"Ingresa la calificación {i+1}: ")))

promedio = sum(calificaciones) / 5

print("Promedio:", promedio)
if promedio >= 70:
    print("¡APROBADO!")
else:
    print("¡REPROBADO!")