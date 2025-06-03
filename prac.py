import pandas as pd

def ingresar_datos():
    estudiantes = {}
    while True:
        nombre = input("Nombre del estudiante: ")
        if nombre.lower() == 'salir':
            break
        try:
            calificaciones = list(map(float, input(f"Ingresa las calificaciones: ").split(',')))
            estudiantes[nombre] = calificaciones
        except ValueError:
            print(" separados por comas.")
    return estudiantes

def calcular_promedios(estudiantes):
    promedios = {nombre: sum(cals)/len(cals) for nombre, cals in estudiantes.items()}
    return promedios

def encontrar_mejor_estudiante(promedios):
    mejor = max(promedios, key=promedios.get)
    return mejor, promedios[mejor]

def guardar_resultados(estudiantes, promedios, mejor_estudiante):
    with open('resultados.txt', 'w') as f:
        f.write("Resultados de estudiantes:\n")
        for nombre in estudiantes:
            f.write(f"{nombre}: Calificaciones: {estudiantes[nombre]}, Promedio: {promedios[nombre]:.2f}\n")
        f.write(f"\nMejor estudiante: {mejor_estudiante[0]} con promedio de {mejor_estudiante[1]:.2f}\n")

def main():
    estudiantes = ingresar_datos()
    promedios = calcular_promedios(estudiantes)
    mejor_estudiante = encontrar_mejor_estudiante(promedios)
    guardar_resultados(estudiantes, promedios, mejor_estudiante)
    print("Resultados guardados")

if __name__ == "__main__":
    main()
