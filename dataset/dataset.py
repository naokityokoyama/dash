import pandas as pd

class Dataset:
    
    def __init__(self):
       self.df = pd.read_csv('https://raw.githubusercontent.com/naokityokoyama/dash/master/dataset/dados_mercado_livre.csv', sep=',').dropna()
       self.numero = (13,4,52,23,67,82)
       
