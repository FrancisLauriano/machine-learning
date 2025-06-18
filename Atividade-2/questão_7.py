# 7. Como concatenar vários DataFrames (empilhando linhas ou colunas), 
# mesmo que tenham colunas diferentes?
# Dica: Utiliza-se pd.concat() especificando axis=0 (linhas) ou axis=1 (colunas). 
# Quando há colunas diferentes, os valores ausentes são preenchidos com NaN.

'''
Para concatenar vários DataFrames, mesmo que possuam colunas diferentes, 
utilizamos a função pd.concat(). Ao especificar o parâmetro axis=0, 
empilhamos os DataFrames na vertical, ou seja, unimos pelas linhas. 
Já com axis=1, empilhamos na horizontal, unindo pelas colunas. 
Quando os DataFrames possuem colunas diferentes, os valores ausentes nas colunas 
que não existem em algum dos DataFrames são preenchidos automaticamente com NaN. 
'''

# Exemplo:
import pandas as pd

# DataFrame 1
df1 = pd.DataFrame({
    'Name': ['Ana', 'Bruno'],
    'Age': [25, 30]
})

# DataFrame 2 com coluna diferente
df2 = pd.DataFrame({
    'Name': ['Carlos', 'Diana'],
    'City': ['SP', 'RJ']
})

# Concatenar pelas linhas (axis=0)
result_lines = pd.concat([df1, df2], axis=0)

# Concatenar pelas colunas (axis=1)
result_columns = pd.concat([df1, df2], axis=1)

# TEST: 
print("="*50)
print("Result of Concatenation by Lines (axis=0):")
print("="*50)
print(result_lines)
print("="*50)
print("\n")
print("="*50)
print("Concatenation Result by Columns (axis=1):")
print("="*50)
print(result_columns)
print("="*50)

