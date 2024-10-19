import streamlit as st

st.set_page_config(page_title="Notas interactivas de probabilidad", page_icon="P.png")

fundamentos = st.Page("fundamentos.py", title="Fundamentos de probabilidad")
vas = st.Page("vas.py", title="Variables aleatorias")
distribuciones = st.Page("distribuciones.py", title="Distribuciones de probabilidad")
multivariadas = st.Page("multivariadas.py", title = "Distribuciones multivariadas")
general = st.Page("general.py", title = "General", default= True)
pg = st.navigation(
    {
        "General": [general],
        "Primer parcial": [fundamentos],
        "Segundo parcial": [vas, distribuciones],
        "Tercer parcial": [multivariadas],
    }
)
pg.run()
