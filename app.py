import streamlit as st
import pandas as pd
import plotly.express as px

# Page title
st.title("Hello TripleTen 👋")

# Header
st.header("🚗 Vehicle Listings Dashboard")

# Load the dataset from the root directory
df = pd.read_csv('vehicles_us.csv')

# Histogram: Distribution of Vehicle Prices
st.subheader("Distribution of Vehicle Prices")
fig_price_hist = px.histogram(
    df,
    x='price',
    nbins=50,
    title='Distribution of Vehicle Prices'
)
st.plotly_chart(fig_price_hist)

# Scatter Plot: Price vs. Odometer
st.subheader("Price vs. Odometer by Vehicle Type")
fig_price_vs_odometer = px.scatter(
    df,
    x='odometer',
    y='price',
    color='type',
    hover_data=['model', 'model_year'],
    title='Price vs. Odometer by Vehicle Type'
)
st.plotly_chart(fig_price_vs_odometer)

# Optional: Bar chart based on checkbox
if st.checkbox("Show Average Price by Vehicle Type"):
    avg_price = df.groupby('type')['price'].mean().reset_index()
    fig_avg_price = px.bar(
        avg_price,
        x='type',
        y='price',
        title='Average Price by Vehicle Type'
    )
    st.plotly_chart(fig_avg_price)
