import yfinance as yf
import pandas as pd

tickers = ["AAPL", "MSFT", "TSLA", "NVDA"]

all_data = []

for ticker in tickers:
    
    df = yf.download(
        ticker,
        start="2024-01-01",
        interval="1d"
    )

    df["Ticker"] = ticker

    all_data.append(df)

final_df = pd.concat(all_data)

final_df.to_csv("market_data.csv")