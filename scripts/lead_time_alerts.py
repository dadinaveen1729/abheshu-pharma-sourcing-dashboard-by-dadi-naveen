import pandas as pd

# Load lead time data
df = pd.read_csv('../data/lead_times.csv')

# Define acceptable threshold
lead_time_limit = 20  # days

# Flag suppliers exceeding threshold
delayed = df[df['Average Lead Time (Days)'] > lead_time_limit]

print("⏱️ Suppliers with High Lead Times:")
print(delayed[['Supplier', 'Average Lead Time (Days)', 'On-Time %']])
