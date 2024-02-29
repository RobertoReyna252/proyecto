import pandas as pd
import plotly.express as px
import streamlit as st
        
car_data = pd.read_csv('vehicles_us.csv') # leer los datos

# Mostrar un encabezado con texto
st.title('Análisis de Datos de Vehículos Nuevos y Usados')
st.header('Descripción general de los datos')
st.write('Este análisis proporciona una descripción general de los datos de vehículos')

# Mostrar un histograma
st.header('Histogramas')
feature_options = {
    "Año del Modelo": "model_year",
    "Cuenta Kilométrica": "odometer",
    "Precio": "price"
}
selected_feature = st.selectbox("Selecciona una característica para el histograma:", list(feature_options.keys()), index=0)
selected_feature_key = feature_options[selected_feature]
hist_fig = px.histogram(car_data, x=selected_feature_key, title=f"Histograma de {selected_feature}")
st.plotly_chart(hist_fig, use_container_width=True)

# Mostrar un gráfico de dispersión
st.header('Gráfico de dispersión del precio vs. año del modelo')
scatter_fig = px.scatter(car_data, x="model_year", y="price", title="Precio vs. Año del modelo")
st.plotly_chart(scatter_fig, use_container_width=True)

# Agregar un botón para mostrar información adicional
if st.checkbox('Mostrar información adicional sobre la base de datos'):
    st.write('La base de datos de vehículos contiene información sobre anuncios de venta de coches, con las siguientes columnas:')
    st.write('- Price: Precio del vehículo en dólares estadounidenses.')
    st.write('- Model Year: Año del modelo del vehículo.')
    st.write('- Model: Modelo del vehículo.')
    st.write('- Condition: Condición del vehículo (por ejemplo, "Nuevo", "Usado").')
    st.write('- Cylinders: Número de cilindros del motor del vehículo.')
    st.write('- Fuel: Tipo de combustible utilizado por el vehículo.')
    st.write('- Odometer: Kilometraje del vehículo.')
    st.write('- Transmission: Tipo de transmisión del vehículo.')
    st.write('- Type: Tipo de vehículo (por ejemplo, "Sedan", "SUV").')
    st.write('- Paint Color: Color de la pintura del vehículo.')
    st.write('- Is 4WD: Indica si el vehículo tiene tracción en las cuatro ruedas (1: Sí, 0: No).')
    st.write('- Date Posted: Fecha en que se publicó el anuncio de venta del vehículo.')
    st.write('- Days Listed: Número de días que el anuncio de venta del vehículo estuvo activo.')