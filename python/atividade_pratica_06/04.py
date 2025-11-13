'''
Crie um programa que consulte a cotação atual de uma moeda estrangeira em relação ao Real Brasileiro 
(BRL). O usuário deve informar o código da moeda desejada (ex: USD, EUR, GBP), e o programa deve exibir 
o valor atual, máximo e mínimo da cotação, além da data e hora da última atualização. Utilize a API da 
AwesomeAPI para obter os dados de cotação.

'''
import requests
from datetime import datetime

def consultar_cotacao():
    moeda = input("Informe o código da moeda USD, EUR, GBP : ").upper()

    url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"

    try:
        resposta = requests.get(url)
        dados = resposta.json()
        chave = f"{moeda}BRL"
        cotacao = dados[chave]
        print(f"Moeda: {cotacao['code']} -> {cotacao['codein']}")
        print(f"Valor Atual: R$ {float(cotacao['bid']):.2f}")
        print(f"Valor Máximo: R$ {float(cotacao['high']):.2f}")
        print(f"Valor Mínimo: R$ {float(cotacao['low']):.2f}")
        data = datetime.fromtimestamp(int(cotacao['timestamp']))
        print(f"Última Atualização: {data.strftime('%d/%m/%Y %H:%M:%S')}")

    except requests.exceptions.RequestException as e:
        print(f"Erro ao consultar a API: {e}")
    except ValueError:
        print("Erro ao processar os dados da API")

consultar_cotacao()
