import pandas as pd

# Load scrap data
df = pd.read_csv('../data/scrap_log.csv')

# Set a high-risk threshold
high_risk_threshold = 10  # KG

# Filter materials with scrap above threshold
high_risk = df[df['Scrap Qty (KG)'] > high_risk_threshold]

print("⚠️ High Scrap Risk Materials:")
print(high_risk[['Material', 'Supplier', 'Scrap Qty (KG)', 'Cause']])
