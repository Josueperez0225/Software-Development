import streamlit as st
import pandas as pd
import plotly.express as px

# Page title
st.title("Hello TripleTen 👋")

# Header
st.header("🚗 Vehicle Listings Dashboard")

# Load the dataset from the root directory
try:
    df = pd.read_csv('vehicles_us.csv')
    st.write("Data loaded successfully!")
    st.write(df.head())  # Display the first few rows of the DataFrame for verification
except Exception as e:
    st.error(f"Error loading data: {e}")

# Histogram: Distribution of Vehicle Prices
st.subheader("Distribution of Vehicle Prices")
try:
    fig_price_hist = px.histogram(
        df,
        x='price',
        nbins=50,
        title='Distribution of Vehicle Prices'
    )
    st.plotly_chart(fig_price_hist)
except Exception as e:
    st.error(f"Error creating histogram: {e}")

# Scatter Plot: Price vs. Odometer
st.subheader("Price vs. Odometer by Vehicle Type")
try:
    fig_price_vs_odometer = px.scatter(
        df,
        x='odometer',
        y='price',
        color='type',
        hover_data=['model', 'model_year'],
        title='Price vs. Odometer by Vehicle Type'
    )
    st.plotly_chart(fig_price_vs_odometer)
except Exception as e:
    st.error(f"Error creating scatter plot: {e}")

# Optional: Bar chart based on checkbox
if st.checkbox("Show Average Price by Vehicle Type"):
    try:
        avg_price = df.groupby('type')['price'].mean().reset_index()
        fig_avg_price = px.bar(
            avg_price,
            x='type',
            y='price',
            title='Average Price by Vehicle Type'
        )
        st.plotly_chart(fig_avg_price)
    except Exception as e:
        st.error(f"Error creating bar chart: {e}")