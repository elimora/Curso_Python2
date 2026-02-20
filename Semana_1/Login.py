import streamlit as st

# *Credenciales internas del sistema, simulando un BD (PARA IM LOGIN)
CORREO_CORRECTO = "admin@mail.com"
PASSWORD_CORRECTO = "1234"

# *TITULO
st.title("Sistema de Login en Python 🐍")

# * Formulario Visial

correo = st.text_input("Correo electronico 📧")
password = st.text_input("Contraseña 🔑", type="password")

# * Boton
if st.button("Ingresar"):
    # *Operadores de Igualdad y Logicos
    if correo == CORREO_CORRECTO and password == PASSWORD_CORRECTO:
        st.success("Acceso Autorizado. Bievenido Usuario 👋")
    else:
        st.error("Acceso Negado 🔥")
