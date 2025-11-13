'''
Desenvolva um programa que consulte informações de endereço a partir de um CEP fornecido pelo usuário, 
utilizando a API ViaCEP. O programa deve exibir o logradouro, bairro, cidade e 
estado correspondentes ao CEP consultado'''

import requests

def consultaCep(cep):
    url = f'https://viacep.com.br/ws/{cep}/json/'
    resposta = requests.get(url)
    dados = resposta.json()
    if resposta.status_code == 200:
        logradouro = dados.get('logradouro')
        bairro = dados.get('bairro')
        cidade = dados.get('localidade')
        estado = dados.get('uf')
        return logradouro, bairro, cidade, estado
    else:
        return "Erro CEP não encontrado"
cep_usuario = input("Digite o CEP (somente números) ")
resultado = consultaCep(cep_usuario)
print("Resultado da consulta:", resultado)
    