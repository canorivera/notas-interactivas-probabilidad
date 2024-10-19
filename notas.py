import streamlit as st

st.markdown("# Temario")
st.markdown("1. Hola")

fundamentos = st.Page("fundamentos.py", title="Fundamentos de probabilidad")
vas = st.Page("vas.py", title="Variables aleatorias")
distribuciones = st.Page("distribuciones.py", title="Distribuciones de probabilidad")
multivariadas = st.Page("multivariadas.py", title = "Distribuciones multivariadas")
st.set_page_config(page_title="Notas interactivas de probabilidad", page_icon=":favicon:")
pg = st.navigation(
    {
        "Primer parcial": [fundamentos],
        "Segundo parcial": [vas, distribuciones],
        "Tercer parcial": [multivariadas],
    }
)
pg.run()