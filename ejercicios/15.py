# matematicas
examenm = (input("#-- Examen de Matematica = ") * 0.90)
promediodetareasm = (input("#-- Promedio de Tareas Matematica=") * 0.10)
total = float(examenm + promediodetareasm)
# fisica
examenf = (input("#-- Examen Fisica=") * 0.80)
promediodetareasf = (input("#-- Promedio de Tareas Fisica = ") * 0.20)
totalf = float(examenf + promediodetareasf)
# quimica
examenq = (input("#-- Examen Quiminca =") * 0.85)
promediodetareasq = (input("#-- Promedio de Tareas de Quiminca = ") * 0.10)
totalq = float(examenf + promediodetareasq)

print("el resultado de Matematicas es %d " % (total))
print("el resultado de Fisica es %d " % (totalf))
print("el resultado de quimica es %d" % (totalq))


#  Un estudiante desea saber cuál será su promedio general en las tres
# materias más difíciles que cursa y cuál será el promedio que obtendrá en
# cada una de ellas. Estasmaterias se evalúancomo se muestra a
# continuación
# La calificación de Matemáticas se obtiene de la sig. manera:
# Examen 90% * 0.90
# Promedio de tareas 10% * 0.1
# En esta materia se pidió un total de tres tareas.
# La calificación de Física se obtiene de la sig. manera:
# Examen 80%
# Promedio de tareas 20%
# En esta materia se pidió un total de dos tareas.
# La calificación de Química se obtiene de la sig. manera:
# Examen 85%
# Promedio de tareas 15%
# En esta materia se pidió un promedio de tres tareas.
