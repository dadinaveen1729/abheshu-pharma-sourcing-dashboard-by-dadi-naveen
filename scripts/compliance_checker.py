import pandas as pd

# Load compliance matrix
df = pd.read_csv('../data/compliance_matrix.csv')

# Flag any supplier with compliance issues
non_compliant = df[(df['Has GMP?'] != 'Yes') | (df['CoA Submitted?'] != 'Yes') | (df['Regulatory Flag'] == 'Yes')]

print("🚫 Non-Compliant Suppliers:")
print(non_compliant[['Supplier', 'Has GMP?', 'CoA Submitted?', 'Regulatory Flag']])
