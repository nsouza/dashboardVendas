import plotly.express as px
from utils import df_rec_estado, format_number

# Criar coluna com valores formatados
df_rec_estado["Total formatado"] = df_rec_estado["Total de vendas"].apply(
    lambda x: format_number(x, prefix="R$")
)

print(df_rec_estado.head())

grafico_barras_vendas = px.bar(df_rec_estado,
    x="Estado",
    y="Total de vendas",
    title="Grafico de Vendas",
    text="Total de vendas",   # adiciona os valores como rótulos    
    color_discrete_sequence=["#0A3D91"]  # azul escuro personalizado
)

# Forçar uso da coluna formatada como rótulo
grafico_barras_vendas.update_traces(
    text=df_rec_estado["Total formatado"],  # aqui garantimos que usa a coluna
    textposition="outside"
)

# Ajustar layout
grafico_barras_vendas.update_layout(
    uniformtext_minsize=8,
    uniformtext_mode="hide"
)

grafico_barras_vendas.update_layout(
    xaxis=dict(
        showgrid=False,   # remove linhas de fundo no eixo X
        zeroline=True,    # mantém a linha do eixo X
        showline=True     # mostra a linha do eixo X
    ),
    yaxis=dict(
        showgrid=False,   # remove linhas de fundo no eixo Y
        zeroline=True,    # mantém a linha do eixo Y
        showline=True     # mostra a linha do eixo Y
    ),
    #plot_bgcolor="white"  # fundo branco sem linhas
)

#print(df_rec_estado)