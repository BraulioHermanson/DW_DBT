#TODO import
import yfinance as yf
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

#TODO import das variaveis de ambiente

#TODO pegar a cotacao dos ativos
commodities = ['CL=F', 'GC=F', 'SI=F']

def buscar_dados_commodities(ticker, periodo='5d', intervalo='1d'):
    ticker = yf.Ticker('CL=F')
    dados = ticker.history(period=periodo, interval=intervalo)[['Close']]
    dados['Ticker'] = ticker
    return dados

def concat_dados(commodities):
    data = []
    for ticker in commodities:
        dados = buscar_dados_commodities(ticker)
        data.append(dados)
    return pd.concat(data)

if __name__ == "__main__":
    concat_dados = buscar_dados_commodities(commodities)
    print(concat_dados)

#TODO salvar no banco de dados