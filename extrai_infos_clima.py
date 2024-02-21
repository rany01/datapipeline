import os
import pandas as pd
from os.path import join
from datetime import datetime, timedelta

# intervalo de datas
data_inicio = datetime.today()
data_fim = data_inicio + timedelta(days=7)

# formantando as datas
data_inicio = data_inicio.strftime('%Y-%m-%d')
data_fim = data_fim.strftime('%Y-%m-%d')

city = 'Boston'
key = 'NV9453M2H7RK5ZGY6VT7F6DWZ'

# Passar as informações para a URL
URL = join('https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/',
           f'{city}/{data_inicio}/{data_fim}?unitGroup=metric&include=days&key={key}&contentType=csv')

# Extrair os dados em csv e printar as primeiras linhas no terminal
dados = pd.read_csv(URL)
print(dados.head())

# Definir o diretório para salvar os arquivos e criar uma pasta
file_path = f'/Users/rany/datapipeline/semana={data_inicio}/'
os.mkdir(file_path)

# Salvar os arquivos em csv
dados.to_csv(file_path + 'dados_brutos.csv')
dados[['datetime', 'tempmin', 'temp', 'tempmax']].to_csv(file_path + 'temperaturas.csv')
dados[['datetime', 'description', 'icon']].to_csv(file_path + 'condicoes.csv')