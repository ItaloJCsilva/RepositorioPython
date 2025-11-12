'''Crie um programa que receba o preço original de um produto e um percentual de desconto, 
realizando o cálculo do preço final após a aplicação do desconto. Requisitos:
Permitir que o usuário informe o preço do produto e o percentual de desconto.
Utilizar operações matemáticas para calcular o valor do desconto e o preço final.
Exibir o preço final com duas casas decimais para garantir precisão. Entrada esperada: 
preço do produto (exemplo: 250.75) e o percentual de desconto (exemplo: 10).'''

def calcularPrecoFinal(precoOriginal, percentualDesconto):
    valorDesconto = (percentualDesconto / 100) * precoOriginal
    precoFinal = precoOriginal - valorDesconto
    return round(precoFinal, 2)
precoOriginal = float(input("Digite o preço original do produto: "))
percentualDesconto = float(input("Digite o percentual de desconto: "))
precofinal = calcularPrecoFinal(precoOriginal, percentualDesconto)
print(f"O preço final após o desconto é: R$ {precofinal:.2f}")