#Crie um programa que converte um valor em reais para dólares e euros. Use os seguintes dados:
#Valor em reais: R$ 100.00

#Taxa do dólar: R$ 5.60

#Taxa do euro: R$ 6.60 
#O programa deve calcular e exibir os valores convertidos, arredondando para duas casas decimais.

valor_reais = float(input("Qual o valor em reais que deseja converter? R$"))
taxa_dolar = 5.60
taxa_euro = 6.60
moeda = input("Converter para 'Dolar' ou 'Euro'? ")
if moeda == "Dolar":
    valor_convertido = valor_reais / taxa_dolar
    print(f"O valor em dólares é: U$ {valor_convertido:.2f}")
elif moeda == "Euro":
    valor_convertido = valor_reais / taxa_euro
    print(f"O valor em euros é: € {valor_convertido:.2f}")
else:
    print("Moeda inválida. Use 'Dolar' ou 'Euro'.")
