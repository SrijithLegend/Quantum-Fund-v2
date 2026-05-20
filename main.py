import pandas as pd
from bulk import bulk_deals
from premarket import filter_stocks

bulk_filtered_df = bulk_deals()
premarket_filtered_df = filter_stocks()

bulk_symbols = set(bulk_filtered_df["SYMBOL"].str.strip().str.upper())
premarket_symbols = set(premarket_filtered_df["SYMBOL"].str.strip().str.upper())
common_symbols = bulk_symbols & premarket_symbols

print(f"\n{len(common_symbols)} stocks appear in BOTH bulk deals and premarket filter:\n")

for symbol in sorted(common_symbols):
    print(f"\n{'='*60}")
    print(f"  {symbol}")
    print(f"{'='*60}")

    print("\n  [PREMARKET DATA]")
    pre = premarket_filtered_df[premarket_filtered_df["SYMBOL"].str.upper() == symbol]
    print(pre.to_string(index=False))

    print("\n  [BULK DEALS]")
    bulk = bulk_filtered_df[bulk_filtered_df["SYMBOL"].str.upper() == symbol]
    print(bulk.to_string(index=False))