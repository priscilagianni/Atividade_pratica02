import pandas as pd

def processar_logs_treinamentos(nome_arquivo='logs_treinamento.csv'):
    try:
        # Ler o arquivo CSV
        df = pd.read_csv(nome_arquivo)
        
        # Calcular média e desvio padrão
        media_tempo = df['tempo_execucao'].mean()
        desvio_padrao_tempo = df['tempo_execucao'].std()

        # Exibir resultados
        print(f'Média do tempo de execução: {media_tempo:.2f}')
        print(f'Desvio padrão do tempo de execução: {desvio_padrao_tempo:.2f}')
    
    except FileNotFoundError:
        print('Arquivo não encontrado')
    except Exception as e:
        print(f'Erro ao processar o arquivo: {e}')

# Chamada da função
processar_logs_treinamentos()

# Para instalar o pandas, execute no terminal:
# pip install pandas


   
        
