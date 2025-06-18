# 10. Utilizando pandas, como lidar com valores ausentes (NaN) em um DataFrame?

'''
Para lidar com valores ausentes (NaN) em um DataFrame utilizando pandas, 
é usado as seguintes funções:
1. df.isnull() ou df.isna() → Verifica onde estão os valores ausentes (retorna True para NaN).
2. df.dropna() → Remove as linhas (ou colunas) que possuem valores ausentes.
3. df.fillna(valor) → Preenche os valores ausentes com um valor específico (ex.: média, zero, texto, etc.).
'''

# Exemplo:
import pandas as pd

# Criar um DataFrame com valores ausentes
data_test = {
    'Name': ['Ana', 'Bruno', 'Carlos', 'Diana'],
    'Age': [25, None, 35, 40],
    'City': ['SP', 'RJ', None, 'PE']
}

df = pd.DataFrame(data_test)

# Verificar onde há valores ausentes
print("Missing values in DataFrame:")
print(df.isnull())

# Remover linhas com valores ausentes
df_sem_nan = df.dropna()
print("\nDataFrame without missing values:")
print(df_sem_nan)

# Preencher valores ausentes
df_preenchido = df.fillna({'Age': df['Age'].mean(), 'City': 'Not informed'})

# Converter a coluna 'Age' para inteiro
df_preenchido['Age'] = df_preenchido['Age'].round(0).astype(int)

print("\nDataFrame with filled values:")
print(df_preenchido)
