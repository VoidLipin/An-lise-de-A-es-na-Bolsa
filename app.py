from flask import Flask, render_template, request
import yfinance as yf

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/acao', methods=['POST'])
def obter_acao():
    ticker = request.form['ticker']
    try:
        # Criando o objeto da ação com yfinance
        ticker_data = yf.Ticker(ticker)

        # Obtendo outras informações da ação
        long_name = ticker_data.info.get('longName', 'Não disponível')
        country = ticker_data.info.get('country', 'Não disponível')
        industry = ticker_data.info.get('industry', 'Não disponível')
        dividend_rate = ticker_data.info.get('dividendRate', 'Não disponível')
        dividend_yield = ticker_data.info.get('dividendYield', 'Não disponível')
        beta = ticker_data.info.get('beta', 'Não disponível')
        last_dividend_value = ticker_data.info.get('lastDividendValue', 'Não disponível')

        # Exibindo as informações na página
        return render_template('acao.html', 
                               ticker=ticker,
                               long_name=long_name,
                               country=country,
                               industry=industry,
                               dividend_rate=dividend_rate,
                               dividend_yield=dividend_yield,
                               beta=beta,
                               last_dividend_value=last_dividend_value)

    except Exception as e:
        return render_template('error.html', error=str(e))

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
