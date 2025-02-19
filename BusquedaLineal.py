import streamlit as st

from pylti.flask import LTI

from flask import Flask, request



app = Flask(__name__)

# Configuración LTI
CONSUMER_KEY = "caspruebaclave"
SHARED_SECRET = "caspruebasecret"

# Inicializar LTI
lti = LTI(
    consumer_key=CONSUMER_KEY,
    shared_secret=SHARED_SECRET
)

@app.route("/launch", methods=["POST"])
def launch():
    if lti.verify_request(request):
        # Obtener información del usuario
        user_id = lti.user_id
        user_name = lti.user_full_name

        # Mostrar la aplicación
        return f"<h1>Aplicación Python integrada con Moodle</h1><p>Bienvenido, {user_name} (ID: {user_id})</p>"
    else:
        return "Error: Solicitud LTI inválida."

if __name__ == "__main__":
    app.run(debug=True)



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

