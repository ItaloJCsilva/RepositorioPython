'''Crie um script em Python que leia e escreva dados em um arquivo JSON. O arquivo JSON deve conter informações de uma pessoa, 
com campos nome, idade e cidade.'''

import json
dados = {
    'Nome': ['Ana', 'Carlos', 'Maria', 'Daniel', 'José'],
    'Idade': [21, 34, 29, 45, 30],
    'Cidade': ['Recife', 'Rio de Janeiro', 'São Paulo', 'Curitiba', 'Xique-Xique']
}

arquivo_json = "dados.json"
try:
    with open(arquivo_json, 'w', encoding='utf-8') as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)
    print(f"Dados escritos com sucesso em '{arquivo_json}'")
except Exception as e:
    print(f"Erro ao escrever o arquivo: {e}")
    exit()


with open(arquivo_json, 'r', encoding='utf-8') as arquivo:
    dados_carregados = json.load(arquivo)

print("\nDados lidos do arquivo:")
print(f"   Nome:   {dados_carregados['Nome']}")
print(f"   Idade:  {dados_carregados['Idade']} anos")
print(f"   Cidade: {dados_carregados['Cidade']}")


