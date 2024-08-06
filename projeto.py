import yfinance as yf
import pandas as pd

# Definindo o ticker da ação desejada
ticker = input("Digite o código da ação desejada: ")

# Criando o objeto da ação com yfinance
ticker_data = yf.Ticker(ticker)

# Obtendo os dados do histórico da ação
data = ticker_data.history(period="max")

# Obtendo outras informações da ação
long_name = ticker_data.info.get('longName', 'Não disponível')
country = ticker_data.info.get('country', 'Não disponível')
industry = ticker_data.info.get('industry', 'Não disponível')
dividend_rate = ticker_data.info.get('dividendRate', 'Não disponível')
dividend_yield = ticker_data.info.get('dividendYield', 'Não disponível')
beta = ticker_data.info.get('beta', 'Não disponível')
last_dividend_value = ticker_data.info.get('lastDividendValue', 'Não disponível')

# Mostrando as informações
print("Nome completo da ação:", long_name)
print("País:", country)
print("Indústria:", industry)
print("Taxa de dividendo (Dividend Rate):", dividend_rate)
print("Rendimento de dividendo (Dividend Yeld):", dividend_yield)
print("Beta (Volatilidade da ação sobre o mercado):", beta)
print("Último valor de dividendo:", last_dividend_value)

# Exibindo os primeiros registros do histórico de preços
print("\nHistórico de preços:")
print(data.head())

print(ticker_data.info)