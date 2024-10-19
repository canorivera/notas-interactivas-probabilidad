import streamlit as st
st.markdown("# Variables aleatorias")

st.markdown('# Definición')
st.markdown('Se dice que $X$ es una variable aleatoria si $:\Omega \mapsto \Reals$. Es decir, las variables aleatorias son funciones reales definidas sobre un espacio muestral. La v.a. es discreta si solo puede tomar un número finito o contablemente infinito de valores. Por otro lado, la v.a. es continua si puede tomar infinitos valores en determinado intervalo.')

st.markdown(r''' 
    ## Función de masa de probabilidad
    Definición: Si $X$ es una v.a.d. con soporte $S_x = \{x_1, x_2, ... \}$ se dice que $f_x(x) = \Reals \to [0,1]$ es la función de masa de probabilidad (f.m.p.) si: 
    1. $f_x(x) = \begin{cases} P(X = x) > 0 & x = x_i \forall i \\ 0 & e.o.c. \end{cases}$
    2. $\sum_x f_x(x) = 1 $
    ''')
st.markdown(r''' 
    ## Funci[on de densidad de probabilidad
    Definición: Si $X$ es una v.a.c. se dice que $f_x(x): \Reals \to [0, \infin] $ es la función de densidad de probabilidad de $X$ si:
    1. $f_x(x) \geq 0 \forall x \in \Reals$
    2. $\int_{-\infin}^{\infin} f_x(x) dx = 1$
    Además, cumple con las propiedades:
    1. $P[a \leq x \leq b] = \int_{a}^b f_x(x) dx$
    2. $P[x = a] = \int_{a}^a f_x(x) dx = 0$
    3. $P[x \leq a] = P[x < a]$
''')


st.markdown("## Función de densidad de probabilidad")
st.markdown("## Función de distribución acumulada")
st.markdown("## Características numéricas de las variables aleatorias")
