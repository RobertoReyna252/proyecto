import pandas as pd
import plotly.express as px
import streamlit as st
        
car_data = pd.read_csv('vehicles_us.csv') # leer los datos

# Crear casillas de verificación para seleccionar tipos de gráficos
show_histogram = st.checkbox('Mostrar histograma')
show_scatterplot = st.checkbox('Mostrar gráfico de dispersión')

# Generar gráficos basados en las casillas de verificación seleccionadas
if show_histogram:
    # Escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    # Crear un histograma
    hist_fig = px.histogram(car_data, x="odometer")
    # Mostrar un gráfico Plotly interactivo
    st.plotly_chart(hist_fig, use_container_width=True)

if show_scatterplot:
    # Escribir un mensaje
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
    # Crear un gráfico de dispersión
    scatter_fig = px.scatter(car_data, x="odometer", y="price")
    # Mostrar un gráfico Plotly interactivo
    st.plotly_chart(scatter_fig, use_container_width=True)
