import streamlit as st
st.markdown("# Variables aleatorias")

st.markdown('# Definición')
st.markdown('Se dice que $X$ es una variable aleatoria si $:\Omega \mapsto \Reals$. Es decir, las variables aleatorias son funciones reales definidas sobre un espacio muestral. La v.a. es discreta si solo puede tomar un número finito o contablemente infinito de valores. Por otro lado, la v.a. es continua si puede tomar infinitos valores en determinado intervalo.')

st.markdown(r'''
    ## Función de masa de probabilidad
    Definición: Si $X$ es una v.a.d. con soporte $S_x = \{x_1, x_2, ... \}$ se dice que $f_x(x) = \Reals \to [0,1]$ es la función de masa de probabilidad (f.m.p.) si:
        1. $ \[ f_x(x) = \begin{cases} P(X = x) > 0 & , x = x_i \forall i \\ 0 & e.o.c. \end{cases} \] $
''')

st.markdown("## Función de densidad de probabilidad")
st.markdown("## Función de distribución acumulada")
st.markdown("## Características numéricas de las variables aleatorias")
