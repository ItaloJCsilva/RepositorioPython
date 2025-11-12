'''Leia um arquivo que contenha dados de log de treinamento de modelos de Machine Learning. Calcule a média e o 
desvio padrão do tempo de exercução constantes.'''

import statistics
def calcular_estatisticas_tempo_execucao(caminho_arquivo):
    tempos_execucao = []
    
    with open(caminho_arquivo, 'r') as arquivo:
        for linha in arquivo:
            if "Tempo de execução:" in linha:
                partes = linha.split("Tempo de execução:")
                if len(partes) > 1:
                    tempo_str = partes[1].strip().split()[0]
                    try:
                        tempo = float(tempo_str)
                        tempos_execucao.append(tempo)
                    except ValueError:
                        continue
    
    if tempos_execucao:
        media = statistics.mean(tempos_execucao)
        desvio_padrao = statistics.stdev(tempos_execucao)
        return media, desvio_padrao
    else:
        return None, None
caminho_arquivo = 'log_treinamento.txt'
media, desvio_padrao = calcular_estatisticas_tempo_execucao(caminho_arquivo)