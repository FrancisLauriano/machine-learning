# 9. Utilizando pandas, como selecionar uma coluna específica e 
# filtrar linhas em um “DataFrame” com base em uma condição?

'''
Para selecionar uma coluna específica em um DataFrame com pandas, 
é utilizado a sintaxe df['nome_coluna'].
Para filtrar linhas com base em uma condição, é usado operações booleanas, como por exemplo:
df[df['nome_coluna'] > valor],
onde a condição pode ser de igualdade, maior, menor, diferente, entre outras.
'''

# Exemplo:
import pandas as pd

# Criar um DataFrame de exemplo
data_test = {
    'Name': ['Ana', 'Bruno', 'Carlos', 'Diana'],
    'Age': [25, 30, 35, 40],
    'City': ['SP', 'RJ', 'BH', 'PA']
}

df = pd.DataFrame(data_test)

# Selecionar a coluna 'Idade'
column_age = df['Age']
print("="*50)
print("column 'Age':")
print("="*50)
print(column_age)
print("\n")

# Filtrar linhas onde a idade é maior que 30
filter_age_over_30 = df[df['Age'] > 30]
print("="*50)
print("People over 30 years of age:")
print("="*50)
print(filter_age_over_30)

