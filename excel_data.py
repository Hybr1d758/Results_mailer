import pandas as pd

# Load the Excel file
file_path = "customers.xlsx"
data = pd.read_excel(file_path)

# Example structure: ['Name', 'Email', 'Result_ID']
print(data.head())
