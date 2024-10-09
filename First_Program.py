import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("AL ML\OnlineRetail.csv")
print(data.head())
print(data.shape)
print(data.columns)
print(data.describe())
data.isnull().sum()
data.nunique()
data["Country"].unique()


data.plot(kind="scatter", x="Quantity", y="UnitPrice")
# plt.show()

data.plot(
    kind="scatter",
    x="Quantity",
    y="UnitPrice",
)
plt.show()

data.plot(kind="scatter", x="Quantity", y="UnitPrice", s=100)
plt.show()

data.plot(kind="scatter", x="Quantity", y="UnitPrice", s=100, alpha=0.5)
plt.show()

sns.scatterplot(x="Quantity", y="UnitPrice", hue="Country", data=data)
plt.show()

sns.scatterplot(x="Quantity", y="UnitPrice",
                hue="Country", data=data, alpha=0.5)
plt.show()

sns.scatterplot(x="Quantity", y="UnitPrice",
                hue="Country", data=data, alpha=0.5, s=100)
plt.show()