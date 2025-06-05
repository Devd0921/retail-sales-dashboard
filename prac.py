import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read and fix data
df = pd.read_csv("product_sales_fresh.csv")
df.rename(columns={"Transactions":"Units_Sold", "Units_Sold": "Transactions"}, inplace=True)

# Group and compute ratio
grouped = df.groupby("Product")[["Units_Sold","Transactions"]].sum().reset_index()
grouped["Units_Sold_Per_Transaction"] = grouped["Units_Sold"]/grouped["Transactions"]

# Clean start
plt.close("all")
sns.set(style="whitegrid")

# Start fresh plot
fig, ax = plt.subplots(figsize=(10, 6))

# Draw bar chart
sns.barplot(data=grouped, x="Product", y="Units_Sold_Per_Transaction", ax=ax)

# Add data labels only once
for i, row in grouped.iterrows():
    ax.text(i, row["Units_Sold_Per_Transaction"] * 1.01,
            f"{row['Units_Sold_Per_Transaction']:.2f}",
            ha="center", va="bottom", fontsize=9)

# Titles and labels
ax.set_title("Units Sold per Transaction vs Product")
ax.set_xlabel("Products")
ax.set_ylabel("Units Sold per Transaction")

plt.tight_layout()
plt.show()