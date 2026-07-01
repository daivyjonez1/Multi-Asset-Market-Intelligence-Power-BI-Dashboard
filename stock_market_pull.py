import yfinance as yf
import pandas as pd

# Asset metadata
assets = {

    "AAPL": {
        "asset_class": "Equity",
        "asset_name": "Apple Inc",
        "sector": "Technology",
        "region": "USA"
    },

    "MSFT": {
        "asset_class": "Equity",
        "asset_name": "Microsoft Corporation",
        "sector": "Technology",
        "region": "USA"
    },

    "NVDA": {
        "asset_class": "Equity",
        "asset_name": "NVIDIA Corporation",
        "sector": "Semiconductors",
        "region": "USA"
    },

    "BTC-USD": {
        "asset_class": "Crypto",
        "asset_name": "Bitcoin",
        "sector": "Digital Asset",
        "region": "Global"
    },

    "GC=F": {
        "asset_class": "Commodity",
        "asset_name": "Gold Futures",
        "sector": "Precious Metals",
        "region": "Global"
    }

}

# Store all datasets here
all_data = []

# Loop through assets
for ticker, metadata in assets.items():

    df = yf.download(
        ticker,
        start="2000-01-01"
    )

    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.get_level_values(0)

    df.reset_index(inplace=True)

    df["Ticker"] = ticker
    df["Asset_Class"] = metadata["asset_class"]
    df["Asset_Name"] = metadata["asset_name"]
    df["Sector"] = metadata["sector"]
    df["Region"] = metadata["region"]

    all_data.append(df)

# Combine everything
final = pd.concat(all_data, ignore_index=True)

# Save CSV
final.to_csv("market_data.csv", index=False)

print("CSV created successfully.")