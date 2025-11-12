'''Crie um programa que gera um perfil de usuário aleatório usando a API 
'Random User Generator'. O programa deve exibir o nome, email e país do usuário gerado.'''

import requests
import json
def gerar_perfil_usuario():
    url = 'https://randomuser.me/api/'
    resposta = requests.get(url)
    dados = resposta.json()
    
    usuario = dados['results'][0]
    nome = f"{usuario['name']['first']} {usuario['name']['last']}"
    email = usuario['email']
    pais = usuario['location']['country']
    
    return nome, email, pais
nome, email, pais = gerar_perfil_usuario()
print(f"Nome: {nome}")
print(f"Email: {email}")
print(f"País: {pais}")
