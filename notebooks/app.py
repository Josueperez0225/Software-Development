import streamlit as st
st.title("Hello Streamlit 👋")

import pandas as pd
import plotly.express as px

# Load the dataset
df = pd.read_csv('notebooks/vehicles_us.csv')

# Title/Header
st.header("🚗 Vehicle Listings Dashboard")

# Histogram Example
st.subheader("Distribution of Vehicle Prices")
fig_price_hist = px.histogram(df, x='price')
st.plotly_chart(fig_price_hist)

# Scatter Plot Example
st.subheader("Price vs. Odometer")
fig_price_vs_odometer = px.scatter(df, x='odometer', y='price', color='type')
st.plotly_chart(fig_price_vs_odometer)

# Checkbox Interaction
if st.checkbox("Show Average Price by Type"):
    avg_price = df.groupby('type')['price'].mean().reset_index()
    fig_avg_price = px.bar(avg_price, x='type', y='price', title="Average Price by Vehicle Type")
    st.plotly_chart(fig_avg_price)
