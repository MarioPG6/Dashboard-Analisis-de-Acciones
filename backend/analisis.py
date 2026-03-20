import yfinance as yf
import pandas as pd

tickers = ["SPY", "NVDA", "NU"]

for t in tickers:
    df = yf.Ticker(t).history(period="2y")
    df['retorno'] = df['Close'].pct_change()
    df['media_20'] = df['Close'].rolling(20).mean()
    df['media_50'] = df['Close'].rolling(50).mean()
    df['volatilidad'] = df['retorno'].rolling(20).std()
    df['max_52s'] = df['Close'].rolling(252).max()
    df['min_52s'] = df['Close'].rolling(252).min()

    print(f"\n{'='*40}")
    print(f"  {t}")
    print(f"{'='*40}")
    print(df[['Close','retorno','media_20','media_50','volatilidad','max_52s','min_52s']].tail(3))