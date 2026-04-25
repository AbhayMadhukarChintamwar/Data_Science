import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('fmcg_sales_marketing_profitability_2023_2025.csv')

print(df.head())

data = pd.DataFrame(df)

# Set column as index
df.set_index('Net_Revenue_USD', inplace=True)

# Line Graph
df.plot(kind='line', title='Sales Over Days')

# Labels
plt.xlabel('Marketing_Spend_USD')
plt.ylabel('Profit_USD')
df.plot(kind='bar')
# Show graph
plt.show()