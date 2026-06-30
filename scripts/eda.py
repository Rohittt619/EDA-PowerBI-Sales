import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("data/superstore_cleaned.csv")

print(df.head())

region_summary = df.groupby('Region').agg(
    Total_Sales=('Sales','sum'),
    Total_Profit=('Profit','sum'),
    Order_Count=('Order ID','nunique')
).reset_index()

fig, axes = plt.subplots(1,2,figsize=(12,5))

axes[0].bar(region_summary['Region'],region_summary['Total_Sales'])
axes[0].set_title("Sales by Region")

axes[1].bar(region_summary['Region'],region_summary['Total_Profit'])
axes[1].set_title("Profit by Region")

plt.tight_layout()

plt.savefig("outputs/figures/sales_profit_by_region.png")

plt.show()


# -----------------------------
# Monthly Sales Trend
# -----------------------------

monthly = df.groupby(['Order Year', 'Order Month'])['Sales'].sum().reset_index()

plt.figure(figsize=(12,5))

for year in monthly['Order Year'].unique():
    subset = monthly[monthly['Order Year'] == year]
    plt.plot(subset['Order Month'],
             subset['Sales'],
             marker='o',
             linewidth=2,
             label=str(year))

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.xticks(range(1,13),
['Jan','Feb','Mar','Apr','May','Jun',
 'Jul','Aug','Sep','Oct','Nov','Dec'])

plt.legend(title="Year")

plt.tight_layout()

plt.savefig("outputs/figures/monthly_sales_trend.png")

plt.show()

# -----------------------------
# Sales & Profit by Sub-Category
# -----------------------------

subcat = df.groupby('Sub-Category').agg(
    Sales=('Sales','sum'),
    Profit=('Profit','sum')
).reset_index()

subcat = subcat.sort_values('Profit')

colors = ['red' if x < 0 else 'steelblue' for x in subcat['Profit']]

plt.figure(figsize=(12,7))

plt.barh(subcat['Sub-Category'],
         subcat['Profit'],
         color=colors)

plt.axvline(0,color='black')

plt.title("Profit by Sub-Category")

plt.tight_layout()

plt.savefig("outputs/figures/subcategory_profit.png")

plt.show()


# -----------------------------
# Discount vs Profit
# -----------------------------

plt.figure(figsize=(8,5))

plt.scatter(df['Discount'],
            df['Profit'],
            alpha=0.4)

plt.axhline(0,color='red')

plt.title("Discount vs Profit")

plt.xlabel("Discount")

plt.ylabel("Profit")

plt.tight_layout()

plt.savefig("outputs/figures/discount_vs_profit.png")

plt.show()


# -----------------------------
# Shipping Analysis
# -----------------------------

ship = df.groupby('Ship Mode')['Ship Days'].mean()

plt.figure(figsize=(8,5))

plt.bar(ship.index,
        ship.values)

plt.title("Average Shipping Days")

plt.ylabel("Days")

plt.xticks(rotation=15)

plt.tight_layout()

plt.savefig("outputs/figures/shipping_days.png")

plt.show()


# -----------------------------
# Correlation Heatmap
# -----------------------------

corr = df[['Sales',
           'Profit',
           'Quantity',
           'Discount',
           'Ship Days']].corr()

plt.figure(figsize=(8,6))

sns.heatmap(corr,
            annot=True,
            cmap='Blues')

plt.title("Correlation Heatmap")

plt.tight_layout()

plt.savefig("outputs/figures/correlation_heatmap.png")

plt.show()


