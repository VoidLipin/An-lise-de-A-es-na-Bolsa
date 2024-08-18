import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

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

# Informações adicionais
target_mean_price = ticker_data.info.get('targetMeanPrice', 'Não disponível')
forward_pe = ticker_data.info.get('forwardPE', 'Não disponível')
trailing_pe = ticker_data.info.get('trailingPE', 'Não disponível')
total_revenue = ticker_data.info.get('totalRevenue', 'Não disponível')
net_income = ticker_data.info.get('netIncomeToCommon', 'Não disponível')
gross_margins = ticker_data.info.get('grossMargins', 'Não disponível')
profit_margins = ticker_data.info.get('profitMargins', 'Não disponível')
debt_to_equity = ticker_data.info.get('debtToEquity', 'Não disponível')
total_debt = ticker_data.info.get('totalDebt', 'Não disponível')
roe = ticker_data.info.get('returnOnEquity', 'Não disponível')
free_cash_flow = ticker_data.info.get('freeCashflow', 'Não disponível')

# Mostrando as informações
print("Nome completo da ação:", long_name)
print("País:", country)
print("Indústria:", industry)
print("Taxa de dividendo (Dividend Rate):", dividend_rate)
print("Rendimento de dividendo (Dividend Yield):", dividend_yield)
print("Beta (Volatilidade da ação sobre o mercado):", beta)
print("Último valor de dividendo:", last_dividend_value)

print("\nInformações adicionais:")
print("Preço-alvo médio dos analistas:", target_mean_price)
print("Proporção P/L (Forward P/E):", forward_pe)
print("Proporção P/L (Trailing P/E):", trailing_pe)
print("Receita total (Total Revenue):", total_revenue)
print("Lucro líquido (Net Income):", net_income)
print("Margem bruta (Gross Margins):", gross_margins)
print("Margem de lucro (Profit Margins):", profit_margins)
print("Dívida/Patrimônio (Debt to Equity):", debt_to_equity)
print("Dívida total (Total Debt):", total_debt)
print("Retorno sobre patrimônio (ROE):", roe)
print("Fluxo de caixa livre (Free Cash Flow):", free_cash_flow)

# Exibindo os primeiros registros do histórico de preços
print("\nHistórico de preços:")
print(data.head())

# Exibindo o dicionário completo de informações
print("\nInformações completas da ação:")
print(ticker_data.info)

# Gráficos
# Gráfico de Preço de Fechamento ao longo do tempo
plt.figure(figsize=(14, 7))
plt.plot(data.index, data['Close'], label='Preço de Fechamento')
plt.title(f'Histórico de Preços de Fechamento - {long_name}')
plt.xlabel('Data')
plt.ylabel('Preço de Fechamento (USD)')
plt.legend()
plt.grid(True)
plt.show()

# Gráfico de Volume negociado ao longo do tempo
plt.figure(figsize=(14, 7))
plt.plot(data.index, data['Volume'], label='Volume Negociado', color='orange')
plt.title(f'Histórico de Volume Negociado - {long_name}')
plt.xlabel('Data')
plt.ylabel('Volume')
plt.legend()
plt.grid(True)
plt.show()
