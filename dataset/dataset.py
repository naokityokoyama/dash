import pandas as pd

class Dataset:
    
    def __init__(self):
       self.df = pd.read_csv('dataset\dados_mercado_livre.csv').dropna()
       self.numero = (13,4,52,23,67,82)
       
