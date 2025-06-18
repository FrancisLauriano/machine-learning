# 8. Utilizando pandas, como realizar a leitura de um arquivo CSV em um 
# DataFrame e exibir as primeiras linhas?

'''
Para realizar a leitura de um arquivo CSV em um DataFrame utilizando pandas, 
é utilizado a função pd.read_csv(), informando o caminho do arquivo. 
Para exibir as primeiras linhas do DataFrame, é usuado o método .head(), 
que por padrão retorna as 5 primeiras linhas. Pode passar um número 
dentro de head() para definir quantas linhas deseja visualizar
'''

# Exemplo:
import pandas as pd

# Ler o arquivo CSV
df = pd.read_csv('./Atividade-2/test_file.csv')

# TEST:
# Exibir as primeiras 6 linhas
print("Display First Lines:")
print(df.head(6))
print("\n")

# Configurar pandas para exibir todas as linhas
pd.set_option('display.max_rows', None)

# Exibir todas as linhas
print("Show All Rows:")
print(df)