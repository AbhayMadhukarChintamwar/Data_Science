import pandas as pd
import random
from datetime import datetime, timedelta

# number of rows (change to 200000, 500000, 1000000 etc.)
num_rows = 100

# file name
file_name = "finance_small_data.csv"

# sample values
companies = ["TCS", "Infosys", "Reliance", "HDFC", "ICICI", "Wipro"]
sectors = ["IT", "Banking", "Energy", "Finance"]
types = ["Buy", "Sell"]

start_date = datetime(2020, 1, 1)

# write header first
columns = ["Date", "Company", "Sector", "Transaction_Type", "Price", "Quantity", "Total_Value"]
pd.DataFrame(columns=columns).to_csv(file_name, index=False)

# chunk size (important for large data)
chunk_size = 100

for i in range(0, num_rows, chunk_size):
    data = []

    for _ in range(chunk_size):
        date = start_date + timedelta(days=random.randint(0, 1500))
        price = round(random.uniform(100, 50), 2)
        quantity = random.randint(1, 10)

        data.append([
            date.strftime("%Y-%m-%d"),
            random.choice(companies),
            random.choice(sectors),
            random.choice(types),
            price,
            quantity,
            round(price * quantity, 2)
        ])

    df = pd.DataFrame(data, columns=columns)

    # append to CSV
    df.to_csv(file_name, mode='a', header=False, index=False)

    print(f"✅ Written {i + chunk_size} rows")

print("🎉 Finance CSV (100K+) created successfully!")