import pandas as pd

def filter_stocks() -> pd.DataFrame:

    df = pd.read_csv('MW-Pre-Open-Market-12-May-2026.csv')
    df.rename(columns={c: c.strip() for c in df.columns}, inplace=True)
    df = df.drop(columns=['IEP', 'VALUE \n (₹ Crores)', 'FFM CAP \n (₹ Crores)', 'NM 52W H', 'NM 52W L'])

    numeric_cols = ["PREV. CLOSE", "CHNG", "%CHNG", "FINAL", "FINAL QUANTITY"]
    for col in numeric_cols:
        df[col] = df[col].astype(str).str.replace(",", "").str.strip()
        df[col] = pd.to_numeric(df[col], errors="coerce")

    condition_prev_close = df["PREV. CLOSE"] > 10
    bullish_pct_change = abs(df["%CHNG"]) > 3
    condition_final_qty = df["FINAL QUANTITY"] > 50000
    mask = condition_prev_close & bullish_pct_change & condition_final_qty

    filtered = df.loc[mask].reset_index(drop=True)
    return filtered


filtered_df = filter_stocks()

print(f"\n{len(filtered_df)} stocks passed the filter:\n")
filtered_stocks = filtered_df.to_string(index=False)
print(filtered_stocks)



