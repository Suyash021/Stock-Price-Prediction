import yfinance as yf

nvda_data = yf.download('NVDA', start='1999-01-04', end='2024-03-03')
print(nvda_data.head())
appl_data = yf.download('AAPL', start='1999-01-04', end='2024-03-03')

nvda_data.to_csv('dataset/nvidia_stock_prices_final.csv', index=True)

# nvda_data.to_csv('dataset/Apple_stock_prices.csv', index=True)
