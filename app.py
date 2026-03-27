
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

    st.subheader("Análise Dinâmica")

    # Selectbox para escolher a dimensão
    dimensao = st.selectbox(
        "Selecione a dimensão para agrupar:",
        ["Estado", "Cidade", "Nome do Vendedor", "Nome do Fornecedor"]
    )

    # Selectbox para escolher a métrica
    metrica = st.selectbox(
        "Selecione a métrica:",
        ["Total de vendas", "Quantidade vencida"]
    )

    # Agrupar dinamicamente
    df_group = df.groupby(dimensao)[metrica].sum().reset_index()

    # Criar gráfico
    fig = px.bar(
        df_group,
        x=dimensao,
        y=metrica,
        text=metrica,
        title=f"{metrica} por {dimensao}",
        color=metrica,
        color_continuous_scale="Blues"
    )
    fig.update_traces(texttemplate='%{text:.2s}', textposition='outside')
    st.plotly_chart(fig, use_container_width=True)
