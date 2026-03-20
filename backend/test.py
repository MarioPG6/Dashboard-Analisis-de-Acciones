import yfinance as yf
import pandas as pd

tickers = ["SPY", "NVDA", "NU"]  # tus acciones actuales

for t in tickers:
    df = yf.Ticker(t).history(period="1y")
    df['retorno'] = df['Close'].pct_change()
    df['media_20'] = df['Close'].rolling(20).mean()
    print(df[['Close', 'retorno', 'media_20']].tail(5))