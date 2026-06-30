import yfinance as yf
import pandas as pd

tickers = ["AAPL", "MSFT", "TSLA", "NVDA"]

all_data =  []

for ticker in tickers:

    df = yf.download(
        ticker,
        period="2y"
    )

    # flatten multiindex columns
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.get_level_values(0)

    df.reset_index(inplace=True)

    df["Ticker"] = ticker

    all_data.append(df)

final = pd.concat(all_data, ignore_index=True)

final.to_csv("market_data.csv", index=False)