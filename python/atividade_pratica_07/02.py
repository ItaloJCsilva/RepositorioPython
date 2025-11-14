''' 
Crie um script em Python que escreva dados em um arquivo CSV. O arquivo 
CSV deve conter informações pessoais, como colunas Nome, Idade e Cidade.
'''

import pandas as pd

dados = {
    'Nome': ['Ana', 'Carlos', 'Maria', 'Daniel', 'José'],
    'Idade': [21, 34, 29, 45, 30],
    'Cidade': ['Recife', 'Rio de Janeiro', 'São Paulo', 'Curitiba', 'Xique-Xique']
}
df = pd.DataFrame(dados)
nome_arquivo = 'dados_pessoais.csv'
df.to_csv(nome_arquivo, index=False)
print(f"Arquivo '{nome_arquivo}' criado com sucesso com os dados pessoais.")