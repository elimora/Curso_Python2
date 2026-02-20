import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Gráfico desde listas usando DataFrame")

# * Inputs para las listas
nombres = st.text_input("Nombres separados por coma:", "Ana,Luis,Carlos,María")
notas = st.text_input("Notas separadas por coma:", "15,18,12,20")

if st.button("Generar gráfico"):  # ? 💡Lo siguiente ocurre SI, se hace click en el botón
    # **********CASTINGS
    # * Convertir strings en listas con el metodo split("separador")
    lista_nombres = nombres.split(",")
    lista_notas_str = notas.split(",")

    # * Convertir la lista de notas str a una lista de números
    # lista_notas = [int(n) for n in lista_notas] # forma de crear listas compactaS, es lo mismo que:
    lista_notas_num = []  # limp
    for n in lista_notas_str:
        lista_notas_num.append(int(n))

    # * Crear DataFrame: espera un diccionario de listas (con las listas credas arriba)
    df = pd.DataFrame({
        "Estudiante": lista_nombres,
        "Nota": lista_notas_num
    })

    st.write("📊 DataFrame generado:")
    st.dataframe(df)

    # * Crear gráfico
    fig, ax = plt.subplots()
    ax.bar(df["Estudiante"], df["Nota"])
    ax.set_title("Notas de Estudiantes")
    ax.set_xlabel("Estudiante")
    ax.set_ylabel("Nota")

    st.pyplot(fig)
