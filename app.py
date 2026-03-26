
import streamlit as st
import pandas as pd
import plotly.express as px
from dataset import df
from utils import format_number

st.set_page_config(layout="wide")


# Carregar Font Awesome via CDN
st.markdown(
    """
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">
    """,
    unsafe_allow_html=True
)

# Usar ícone no título
st.markdown(
    "<h1>Dashboard de Vendas <i class='fa fa-shopping-cart'></i></h1>",
    unsafe_allow_html=True
)

# Converter a coluna para numérica (ignora erros se houver texto)
#df['Total de vendas'] = pd.to_numeric(df['Total de vendas'], errors='coerce')


aba1, aba2, aba3 = st.tabs(['Dataset', 'Receitas', 'Vendedores'])
with aba1:
     st.dataframe(df.head(10))
with aba2:
    coluna1, coluna2 = st.columns(2)
    with coluna1:
       st.metric('Receitas Total', format_number(df['Total de vendas'].sum(),'R$'))
    with coluna2:
        st.metric('Quantidade de vendas', format_number(df.shape[0]))