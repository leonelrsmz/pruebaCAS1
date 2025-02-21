import streamlit as st

from pylti.flask import LTI

from flask import Flask, request



st.image("Resources/Banner CAS.jpg")

st.title("Ejercicio 1 - Busqueda Lineal")

st.header("Código")

st.code("""
def busqueda_lineal(A, X):
    for i in range(len(A)):
        if A[i] == X:
            return i  # Retorna el índice donde se encuentra el objetivo
    return -1  # Retorna -1 si el objetivo no está en la lista


# Ejemplo de uso
if __name__ == "__main__":
    lista = [1,10, 23, 45, 70,58, 11, 15]
    X = 70

    resultado = busqueda_lineal(lista, X)

    if resultado != -1:
        print(f"El elemento {X} se encuentra en el índice {resultado}.")
    else:
        print(f"El elemento {X} no se encuentra en la lista.")
""", language="python")

st.header("Resultado")

def busqueda_lineal(A, X):
    """
    Implementación del algoritmo de búsqueda lineal.
    :param arr: Lista de elementos en la que buscar.
    :param objetivo: Elemento que se desea encontrar.
    :return: Índice del elemento si se encuentra, de lo contrario, -1.
    """
    for i in range(len(A)):
        if A[i] == X:
            return i  # Retorna el índice donde se encuentra el objetivo
    return -1  # Retorna -1 si el objetivo no está en la lista


# Ejemplo de uso
if __name__ == "__main__":
    lista = [1,10, 23, 45, 70,58, 11, 15]
    X = 70

    resultado = busqueda_lineal(lista, X)

    if resultado != -1:
        print(f"El elemento {X} se encuentra en el índice {resultado}.")
        st.write(f"El elemento {X} se encuentra en el índice {resultado}.")
    else:
        print(f"El elemento {X} no se encuentra en la lista.")
        st.write(f"El elemento {X} no se encuentra en la lista.")

