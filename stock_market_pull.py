import yfinance as yf
import pandas as pd

# Asset metadata
assets = {

    "AAPL": "Equity",
    "MSFT": "Equity",
    "NVDA": "Equity",
    "GOOGL": "Equity",
    "AMZN": "Equity",

    "BTC-USD": "Crypto",
    "ETH-USD": "Crypto",

    "SPY": "ETF",

    "GC=F": "Commodity",

    "USDNGN=X": "Forex"
}

# Store all datasets here
all_data = []

# Loop through assets
for ticker, asset_class in assets.items():

    print(f"Downloading {ticker}...")

    df = yf.download(
        ticker,
        start="2000-01-01"
    )

    # Fix MultiIndex issue
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.get_level_values(0)

    # Convert index to normal column
    df.reset_index(inplace=True)

    # Add metadata columns
    df["Ticker"] = ticker
    df["Asset_Class"] = asset_class

    # Append to master list
    all_data.append(df)

# Combine everything
final = pd.concat(all_data, ignore_index=True)

# Save CSV
final.to_csv("market_data.csv", index=False)

print("CSV created successfully.")