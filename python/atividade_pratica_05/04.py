'''Crie uma função que calcule a idade de uma pessoa em dias, baseada no ano de nascimento.'''

def calcularIdadeEmDias(anoNascimento, anoAtual):
    idadeAnos = anoAtual - anoNascimento
    idadeDias = idadeAnos * 365
    return idadeDias
anoNascimento = int(input("Digite o ano de nascimento: "))
anoAtual = int(input("Digite o ano atual: "))
idadeDias = calcularIdadeEmDias(anoNascimento, anoAtual)
print(f"A idade em dias é: {idadeDias} dias")
