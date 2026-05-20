import pandas as pd

def bulk_deals() -> pd.DataFrame:

    df = pd.read_csv('Large-deals-BULK-08-May-2026.csv')
    df.rename(columns={c: c.strip() for c in df.columns}, inplace=True)
    df = df.drop(columns=['DATE', 'SECURITY NAME', 'REMARKS'])

    df["QUANTITY TRADED"] = df["QUANTITY TRADED"].astype(str).str.replace(",", "").str.strip()
    df["QUANTITY TRADED"] = pd.to_numeric(df["QUANTITY TRADED"], errors="coerce")

    bulk_filtered = df[df["QUANTITY TRADED"] > 100000].reset_index(drop=True)
    bulk_filtered = bulk_filtered.sort_values(by="SYMBOL").reset_index(drop=True)

    return bulk_filtered


bulk_filtered_df = bulk_deals()

print(f"\n{len(bulk_filtered_df)} bulk deals across {bulk_filtered_df['SYMBOL'].nunique()} unique stocks:\n")
bulk_filtered = bulk_filtered_df.to_string(index=False)
print(bulk_filtered)
