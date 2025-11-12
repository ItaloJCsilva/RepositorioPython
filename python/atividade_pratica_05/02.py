'''rie uma função que verifique se uma palavra ou frase é um palíndromo 
(lê-se igual de trás para frente, ignorando espaços e pontuação). Se o resultado é True, 
responda “Sim”, se o resultado for False, responda “Não”.'''


def palindromo(palavraFrase):
    palavraFraseTratada= palavraFrase.replace(" ","").lower()
    palavraFraseIvertida = palavraFraseTratada[::-1]
    if (palavraFraseTratada == palavraFraseIvertida):
        return "Sim"
    else:
        return "Não"

palavraFrase = input("Digite uma palavra ou frase: ")
print(palindromo(palavraFrase))
