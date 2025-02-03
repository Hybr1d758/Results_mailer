import pandas as pd
from faker import Faker

def generate_excel(filename="bio_data.xlsx", num_entries=100):
    fake = Faker()
    
    data = {
        "Name": [fake.name() for _ in range(num_entries)],
        "Email": [fake.email() for _ in range(num_entries)]
    }
    
    df = pd.DataFrame(data)
    df.to_excel(filename, index=False)
    print(f"Excel file '{filename}' generated successfully with {num_entries} entries.")

if __name__ == "__main__":
    generate_excel()

