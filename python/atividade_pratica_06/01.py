'''
Crie um programa que gera uma senha aleatória com o módulo random, 
utilizando caracteres especiais, possibilitando o usuário a informar 
a quantidade de caracteres dessa senha aleatória.'''
import random
import string

def gerar_senha(comprimento):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    
    # Lista temporária para armazenar os caracteres
    lista_de_caracteres = []
    
    # Loop 'for' explícito para adicionar caracteres à lista
    for _ in range(comprimento):
        caractere_aleatorio = random.choice(caracteres)
        lista_de_caracteres.append(caractere_aleatorio)
        
    # Junta todos os caracteres da lista em uma única string
    senha = ''.join(lista_de_caracteres)
    
    return senha

# Exemplo de uso: gerar senha com comprimento 12
senha_gerada = gerar_senha(12)
print("Senha gerada:", senha_gerada)