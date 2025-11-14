'''Crie um script en Python que leia um arquivo CSV e exiba os dados na tela. 
O arquivo CSV deve conter 
informações de pessoas, com colunas Nome, Idade e Cidade.'''

import pandas as pd

nome_arquivo = 'dados_pessoais.csv'
df = pd.read_csv(nome_arquivo)
print("\nDados Pessoais lidos do arquivo CSV:")
print(df)

