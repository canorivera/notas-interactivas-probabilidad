import streamlit as st

st.header("Temario")

fundamentos = st.Page("fundamentos.py", title="Fundamentos de probabilidad")
vas = st.Page("vas.py", title="Variables aleatorias")
distribuciones = st.Page("distribuciones.py", title="Distribuciones de probabilidad")
multivariadas = st.Page("multivariadas.py", title = "Distribuciones multivariadas")

st.navigation(
    {
        "Primer parcial": [fundamentos],
        "Segundo parcial": [vas, distribuciones],
        "Tercer parcial": [multivariadas],
    }
)
