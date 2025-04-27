import streamlit as st
import pandas as pd
import plotly.express as px

# Leer los datos
car_data = pd.read_csv(
    "vehicles_us.csv"
)  # Asegúrate de tener el archivo en la misma carpeta

# Encabezado
st.header("Análisis de Datos de Vehículos en Venta (vehicles_us.csv) 🚗")

# Botón para construir histograma
hist_button = st.button("Construir Histograma de Odómetro")

if hist_button:
    st.write(
        'Creación de un histograma para la columna "odometer" del conjunto de datos de anuncios de venta de coches.'
    )
    fig_hist = px.histogram(
        car_data, x="odometer", title="Distribución del Kilometraje de Vehículos"
    )
    st.plotly_chart(fig_hist, use_container_width=True)

# Botón para construir gráfico de dispersión
scatter_button = st.button("Construir Gráfico de Dispersión Año vs Precio")

if scatter_button:
    st.write('Creación de un gráfico de dispersión entre "model_year" y "price".')
    fig_scatter = px.scatter(
        car_data,
        x="model_year",
        y="price",
        title="Relación entre Año del Modelo y Precio",
        hover_data=["model"],
    )
    st.plotly_chart(fig_scatter, use_container_width=True)

# -----------------------------------------
# (DESAFÍO EXTRA): Versión con casillas de verificación (checkbox)

st.subheader("Opciones adicionales usando Casillas de Verificación ✅")

# Casilla para construir histograma
build_histogram = st.checkbox("Mostrar Histograma de Odómetro")

if build_histogram:
    st.write('Construyendo histograma para la columna "odometer".')
    fig_hist_checkbox = px.histogram(
        car_data, x="odometer", title="Distribución del Kilometraje de Vehículos"
    )
    st.plotly_chart(fig_hist_checkbox, use_container_width=True)

# Casilla para construir gráfico de dispersión
build_scatter = st.checkbox("Mostrar Gráfico de Dispersión Año vs Precio")

if build_scatter:
    st.write('Construyendo gráfico de dispersión de "model_year" vs "price".')
    fig_scatter_checkbox = px.scatter(
        car_data,
        x="model_year",
        y="price",
        title="Relación entre Año del Modelo y Precio",
        hover_data=["model"],
    )
    st.plotly_chart(fig_scatter_checkbox, use_container_width=True)
