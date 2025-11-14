'''Leia um arquivo que contenha dados de log de treinamento de modelos de Machine Learning. Calcule a média e o 
desvio padrão do tempo de exercução constantes.'''

'''pedi para o chatgpt gerar os arquivos de log para teste.'''

import pandas as pd

nome_arquivo = 'logs_treinamento.csv'  
coluna_tempo = 'tempo_execucao_segundos'  
df = pd.read_csv(nome_arquivo)
tempos = pd.to_numeric(df[coluna_tempo], errors='coerce')  
tempos = tempos.dropna()
media = tempos.mean()
desvio_padrao = tempos.std()

print(f"\nResultados do tempo de execução ({coluna_tempo}):")
print(f"   Média:          {media:.4f} segundos")
print(f"   Desvio Padrão:  {desvio_padrao:.4f} segundos")
print(f"   Total de logs:  {len(tempos)} entradas válidas\n")

    
   