'''Crie uma função que calcule a gorjeta a ser deixada em um restaurante, baseada no valor total da conta e na 
porcentagem de gorjeta desejada. Calcula o valor da gorjeta baseado no total da conta e na porcentagem desejada.
Parâmetros: valor_conta (float): O valor total da conta porcentagem_gorjeta (float): A porcentagem da gorjeta 
(ex: 15 para 15%)
Retorna: float: O valor da gorjeta calculada'''

valorConta = float(input("Digite o valor total da conta: "))
porcentagemGorjeta = float(input("Digite a porcentagem da gorjeta desejada: "))
calcular_gorjeta(valorConta, porcentagemGorjeta)
def calcular_gorjeta(valor_conta, porcentagem_gorjeta):
    gorjeta = (porcentagem_gorjeta / 100) * valor_conta
    return print(f"O valor da gorjeta é: R$ {gorjeta:.2f}")
    
