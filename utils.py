from regex import sub
from dataset import df

from dataset import df
def format_number(value, prefix=''):
    # Se for bilhão
    if value >= 1_000_000_000:
        valor = value / 1_000_000_000
        return f'{prefix} {valor:,.2f} bilhões'.replace(',', 'X').replace('.', ',').replace('X', '.')
    # Se for milhão
    elif value >= 1_000_000:
        valor = value / 1_000_000
        return f'{prefix} {valor:,.2f} milhões'.replace(',', 'X').replace('.', ',').replace('X', '.')
    # Se for mil
    elif value >= 1_000:
        valor = value / 1_000
        return f'{prefix} {valor:,.2f} mil'.replace(',', 'X').replace('.', ',').replace('X', '.')
    # Valores menores
    else:
        return f'{prefix} {value:,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.')


# Total por estado
df_rec_estado = df.groupby('Estado')[['Total de vendas']].sum()
df_rec_estado = (
    df.drop_duplicates(subset='Estado')[['Estado']]
      .merge(
          df_rec_estado,
          left_on='Estado',
          right_index=True
      )
      .sort_values('Total de vendas', ascending=False)
)
#print(df_rec_estado)
print(df_rec_estado.columns)