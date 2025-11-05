'''
Desenvolva uma calculadora em Python que realize as quatro operações básicas 
(adição, subtração, multiplicação e divisão) entre dois números. 
A calculadora deve ser capaz de lidar com diversos tipos de erros 
de entrada e operação. Siga as especificações abaixo:
A calculadora deve solicitar ao usuário que insira dois números e uma operação.
As operações válidas são: + (adição), - (subtração), * (multiplicação) e / (divisão).
O programa deve continuar solicitando entradas até que uma operação válida seja concluída.
Trate os seguintes erros:
Entrada inválida (não numérica) para os números
Divisão por zero
Operação inválida
Use try/except para capturar e tratar os erros apropriadamente.
Após cada erro, o programa deve informar o usuário sobre o erro e solicitar nova entrada.
uando uma operação é concluída com sucesso, exiba o resultado e encerre o programa.
'''

while True:
    try:
        num1 = float(input("Digite o primeiro número: "))
        operacao = input("Digite a operação (+, -, *, /): ")
        num2 = float(input("Digite o segundo número: "))
        

        if operacao == '+':
            resultado = num1 + num2
        elif operacao == '-':
            resultado = num1 - num2
        elif operacao == '*':
            resultado = num1 * num2
        elif operacao == '/':
            if num2 == 0:
                raise ZeroDivisionError("Divisão por zero não é permitida.")
            resultado = num1 / num2
        else:
            raise ValueError("Erro: Operação inválida. Use +, -, *, ou /.")

        print(f"O resultado de {num1} {operacao} {num2} é: {resultado}")
        break

    except ValueError as ve:
        print(ve)
    except ZeroDivisionError as zde:
        print(zde)
    except Exception as e:
        print(f"Erro inesperado: {e}")
