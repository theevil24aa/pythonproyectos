nota = 0
for x in range(3):
    estu = int(input("pedir las tres notas:"))
    nota += 3
nota /= 3
nota = float(int((nota * 55) / 100))
print(nota)
examen = float(input("pon la nota del examen"))
print("la nota es", float((examen * 30) / 100))
trabajo = float(input("trabajo final"))
print("trabajo final es", float((trabajo * 15) / 100))
print("____________")
print("la nota final es :  ",(float((trabajo * 15) / 100)+float((examen * 30) / 100)+float(int((nota * 55) / 100)))/3)

# Un estudiante desea saber cuál será su calificación final en la materia de
# Algoritmos. Dicha calificación se compone de los siguientes porcentajes:
#   55% del promedio de sus tres calificaciones parciales.
#   30% de la calificación del examen final.
#   15% de la calificación de un trabajo final.