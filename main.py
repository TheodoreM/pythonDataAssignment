import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("liquorSales.csv")
print(df.info())
ItemProfit = df.groupby("item_description").agg({"bottles_sold": "sum", "sale_dollars": "sum"})
print(ItemProfit)
print(df["store_name"])
Place = df.groupby("zip_code").agg({"bottles_sold": "sum"})
print(Place)
plt.scatter(df["zip_code"],df["bottles_sold"])
plt.xlabel("Zip code")
plt.ylabel("Bottles sold")
plt.title("Bottles Sold")
plt.show()