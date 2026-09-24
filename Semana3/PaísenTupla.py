# Objetivo: Usar funciones, condicionales y tuplas.

def validar_pais(tupla, pais):
    if pais in tupla:
        print("Pais encontrado")
    else:
        print("Pais no encontrado")

paises = ("Costa Rica", "Panama", "Mexico", "España", "Argentina")
buscado = input("Pais a buscar: ")

validar_pais(paises, buscado)