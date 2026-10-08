import pandas as pd
import plotly.express as px
import streamlit as st

# Carregar os dados dos carros
car_data = pd.read_csv("vehicles_us.csv")

# Cabeçalho do aplicativo
st.header("Dashboard de Anúncios de Carros")

# Botão para criar um histograma
hist_button = st.button("Criar histograma")

if hist_button:
    st.write("Distribuição da quilometragem dos carros")
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

# Botão para criar um gráfico de dispersão
scatter_button = st.button("Criar gráfico de dispersão")

if scatter_button:
    st.write("Relação entre quilometragem e preço dos carros")
    fig = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)
