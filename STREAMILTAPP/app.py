import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title("Gráfica de datos aleatorios con Streamlit")

# Slider para elegir el número de datos
num_datos = st.slider("Selecciona la cantidad de datos a generar",min_value=5,max_value=50,value=10)

# Generar datos aleatorios
tiempo = np.linspace(0, 10, num_datos)
voltaje = np.random.uniform(low=0.5, high=5.0, size=num_datos)

# Crear DataFrame
df = pd.DataFrame({
    "Tiempo (s)": tiempo,
    "Voltaje (V)": voltaje
})

# Mostrar datos
st.write("Datos generados aleatoriamente:")
st.dataframe(df)

# Graficar
fig, ax = plt.subplots()
ax.plot(df["Tiempo (s)"], df["Voltaje (V)"], marker="o", linestyle="-", color="green")
ax.set_xlabel("Tiempo (s)")
ax.set_ylabel("Voltaje (V)")
ax.set_title("Voltaje vs. Tiempo")
st.pyplot(fig)
