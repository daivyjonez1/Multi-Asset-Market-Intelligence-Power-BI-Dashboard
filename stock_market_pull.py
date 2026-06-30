import yfinance as yf
import pandas as pd

assets = {

"AAPL":"Equity",
"MSFT":"Equity",
"NVDA":"Equity",
"GOOGL":"Equity",
"AMZN":"Equity",

"BTC-USD":"Crypto",
"ETH-USD":"Crypto",

"SPY":"ETF",

"GC=F":"Commodity",

"USDNGN=X":"Forex"

}

for ticker, asset_class in assets.items():

    df = yf.download(
        ticker,
        start="2000-01-01"
    )

    df["Ticker"] = ticker

    df["Asset_Class"] = asset_class

all_data =  []

for ticker in tickers:

    df = yf.download(
        ticker,
        period="20y"
    )

    # flatten multiindex columns
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.get_level_values(0)

    df.reset_index(inplace=True)

    df["Ticker"] = ticker

    all_data.append(df)

final = pd.concat(all_data, ignore_index=True)

final.to_csv("market_data.csv", index=False)