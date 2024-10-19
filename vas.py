import streamlit as st
st.markdown("# Variables aleatorias")

st.markdown('# Definición')
st.markdown('Se dice que $X$ es una variable aleatoria si $:\Omega \mapsto \Reals$. Es decir, las variables aleatorias son funciones reales definidas sobre un espacio muestral. La v.a. es discreta si solo puede tomar un número finito o contablemente infinito de valores. Por otro lado, la v.a. es continua si puede tomar infinitos valores en determinado intervalo.')

st.markdown(r''' 
    ## Función de masa de probabilidad
    Definición: si $X$ es una v.a.d. con soporte $S_x = \{x_1, x_2, ... \}$ se dice que $f_x(x) = \Reals \to [0,1]$ es la función de masa de probabilidad (f.m.p.) si: 
    1. $f_x(x) = \begin{cases} P(X = x) > 0 & x = x_i \forall i \\ 0 & e.o.c. \end{cases}$
    
    2. $\sum_x f_x(x) = 1 $
    ''')
st.markdown(r''' 
    ## Función de densidad de probabilidad
    Definición: si $X$ es una v.a.c. se dice que $f_x(x): \Reals \to [0, \infin] $ es la función de densidad de probabilidad (f.d.p.) de $X$ si:
    1. $f_x(x) \geq 0, \forall x \in \Reals$
    
    2. $\intop_{-\infin}^{\infin} f_x(x) dx = 1$
            
    Además, cumple con las propiedades:
    1. $P[a \leq x \leq b] = \intop_{a}^b f_x(x) dx$
    
    2. $P[x = a] = \intop_{a}^a f_x(x) dx = 0$
    
    3. $P[x \leq a] = P[x < a]$
''')


st.markdown(r'''
    ## Función de distribución acumulada
    Definición: se dice que la función $F_x(x): \Reals \to [0,1]$ es la función de distribución acumulada (f.d.a.) de la v.a. si $F_x(X) = P(X \leq x)$
            
    Además, si X es una v.a.c., entonces:
    1. $P(a \leq x \leq b) = P(X \leq b) - P(X \leq a) = F_x(b) - F_x(a) $
    
    2. $F_x(X) = P(X \leq x) = \int_{-\infin}^x f_x(t)dt$
    
    3. $f_x(x) = \frac{d}{dx}F_x(x) $
    ''')

st.markdown("## Características numéricas de las variables aleatorias")
st.markdown('''
    ### Esperanza, media o valor esperado
    Esperanza de una v.a.d.: $E[X] = \sum_{x \in S_x} x \cdot P(X = x)$
            
    Esperanza de una v.a.c.: $E[X] = \int_{x \in S_x} x \cdot f_x(X) dx$
            
    La esperanza cumple con las siguientes propiedades para $X, Y$ variables aleatorias y $c$ una constante:
    1. $E[c] = c$
    2. $E[cX] = c \cdot E[X]$
    3. $E[X + Y] = E[X] + E[Y] $
    ''')
st.markdown('''
    ### Varianza
    $Var(X) = \sigma^2_x = E[(X - E[X])^2] = E[X^2] - E^2[X]$
            
    Si $X$ es una v.a., y $c$ una constante, se cumple:
    1. $Var(c) = 0$
    2. $Var(cX) = c^2 \cdot Var(X)$
''')
st.markdown('''
### Lotus o ley del estadístico inconsciente
La ley del estadístico inconsciente nos permite calcular el valor esperado de la transformación de una variable aleatoria $g(X)$, de forma que:
- Si $X$ es una v.a.d., $E[g(X)] = \sum_{x \in S_x} g(x) \cdot P(X = x)$
            
- Si $X$ es una v.a.d., $E[g(X)] = \int_{x \in S_x} g(x) \cdot f_x(X) dx$
''')

st.markdown(r''' 
### Momentos y momentos centrales
Si $X$ es una v.a. y $k \in \Z^+$:
- $\mu_k = E[X^k]$ es el k-ésimo momento de la variable
            
- $\alpha_k = E[ (X - E[X])^k ] $ es el k-ésimo momento central de la variable 
''')

st.markdown(r'''
### Medidas de tendencia central 
Media: esperanza o primer momento
            
Mediana: Si X es una v.a. con f.d.a. $F_x(X), entonces la mediana, $\tilde{x}$ es el valor del soporte de $X$ tal que:
- Si X es discreta: $F_x(\tilde{x}^-) \leq \frac{1}{2} \leq F_x(\tilde{x})$
- Si X es continua: $F_x(\tilde{x}) = \frac{1}{2}$
            ''')