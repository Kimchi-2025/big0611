import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import yfinance as yf

# raw = yf.download("AAPL", start="2026-01-01", end="2026-06-30")
raw = yf.download("NVDA", period="1y", interval="1d", multi_level_index=False)

# df = raw.copy()
# print(df['Close'].agg(['max', 'min', 'mean']).map('{:.0f}'.format))

# print(df['Volume'].agg(['mean', 'median', 'std']).map('{:,.0f}'.format))

# new = df[['Close', 'Volume']]

# print("tail", df.tail(10))

# print("iloc", df.iloc[-10:])

# print(len(df[df['Close'] > df['Close'].quantile(0.9)].index))
# print(df[df['Close'] > df['Close'].quantile(0.9)].index)

plt.figure(figsize=(10,5))
plt.subplot(1,2,1)
sns.histplot(raw, x='Close')
plt.subplot(1,2,2)
sns.histplot(raw, x='Close')
plt.show()