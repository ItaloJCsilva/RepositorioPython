'''
Crie um programa que gera uma senha aleatória com o módulo random, 
utilizando caracteres especiais, possibilitando o usuário a informar 
a quantidade de caracteres dessa senha aleatória.'''
import random
import string

def gerar_senha(comprimento):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    lista_de_caracteres = []
    for _ in range(comprimento):
        caractere_aleatorio = random.choice(caracteres)
        lista_de_caracteres.append(caractere_aleatorio)
    senha = ''.join(lista_de_caracteres)
    
    return senha

senha_gerada = gerar_senha(int(input("Digite o comprimento desejado para a senha: ")))
print("Senha gerada:", senha_gerada)