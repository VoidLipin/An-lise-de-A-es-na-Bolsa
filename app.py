import streamlit as st
import yfinance as yf
import matplotlib.pyplot as plt

# Configurando o título da aplicação
st.title("Informações de Ações")

# Entrada para o código da ação
ticker = st.text_input("Digite o código da ação desejada:")

if ticker:
    ticker_data = yf.Ticker(ticker)
    data = ticker_data.history(period="max")

    long_name = ticker_data.info.get('longName', 'Não disponível')
    country = ticker_data.info.get('country', 'Não disponível')
    industry = ticker_data.info.get('industry', 'Não disponível')
    dividend_rate = ticker_data.info.get('dividendRate', 'Não disponível')
    dividend_yield = ticker_data.info.get('dividendYield', 'Não disponível')
    beta = ticker_data.info.get('beta', 'Não disponível')
    last_dividend_value = ticker_data.info.get('lastDividendValue', 'Não disponível')
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
    st.subheader(f"Informações para {long_name}")
    st.write(f"**País:** {country}")
    st.write(f"**Indústria:** {industry}")
    st.write(f"**Taxa de dividendo:** {dividend_rate}")
    st.write(f"**Rendimento de dividendo:** {dividend_yield}")
    st.write(f"**Beta:** {beta}")
    st.write(f"**Último valor de dividendo:** {last_dividend_value}")
    st.write(f"**Preço-alvo médio dos analistas:** {target_mean_price}")
    st.write(f"**Proporção P/L (Forward P/E):** {forward_pe}")
    st.write(f"**Proporção P/L (Trailing P/E):** {trailing_pe}")
    st.write(f"**Receita Total:** {total_revenue}")
    st.write(f"**Lucro Líquido:** {net_income}")
    st.write(f"**Margem Bruta:** {gross_margins}")
    st.write(f"**Margem de Lucro:** {profit_margins}")
    st.write(f"**Dívida/Patrimônio (Debt to Equity):** {debt_to_equity}")
    st.write(f"**Dívida Total:** {total_debt}")
    st.write(f"**ROE:** {roe}")
    st.write(f"**Fluxo de Caixa Livre:** {free_cash_flow}")

    # Gráfico de Preço de Fechamento
    st.subheader("Histórico de Preços de Fechamento")
    st.line_chart(data['Close'])

    # Gráfico de Volume Negociado
    st.subheader("Histórico de Volume Negociado")
    st.line_chart(data['Volume'])
