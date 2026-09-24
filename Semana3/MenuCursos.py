# Objetivo: Aplicar funciones, ciclos y tuplas.

def mostrar_menu(tupla):
    for curso in tupla:
        print(curso)

cursos = ("Python Basico", "Programacion Intermedia", "Bases de Datos")

mostrar_menu(cursos)