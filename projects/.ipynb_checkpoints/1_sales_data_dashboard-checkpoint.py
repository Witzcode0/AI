import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

st.set_option('deprecation.showPyplotGlobalUse', False)

df = pd.read_csv('sales_data.csv')
df['Date'] = pd.to_datetime(df['Date'])
df['Total_Sales'] = df['Units_Sold'] * df['Price']

st.title("📊 Sales Dashboard")

# Show data
if st.checkbox("Show Raw Data"):
    st.write(df)

# Date filter
date_range = st.date_input("Select Date Range", [df['Date'].min(), df['Date'].max()])
filtered = df[(df['Date'] >= pd.to_datetime(date_range[0])) & (df['Date'] <= pd.to_datetime(date_range[1]))]

# Plot
st.subheader("Total Sales Per Day")
daily_sales = filtered.groupby('Date')['Total_Sales'].sum()
daily_sales.plot(kind='bar', color='lightgreen')
plt.xticks(rotation=45)
plt.ylabel("Sales ₹")
plt.tight_layout()
st.pyplot()

# Product Summary
st.subheader("Product-wise Sales Summary")
summary = filtered.groupby('Product').agg({
    'Units_Sold': 'sum',
    'Total_Sales': 'sum'
})
st.write(summary)
