import streamlit as st

st.title("Decode Investing Clone")
st.write("Welcome to the AI-assisted Stock Market Analysis Platform")

# Example input and output
stock_ticker = st.text_input("Enter Stock Ticker", "AAPL")
st.write(f"Stock Ticker: {stock_ticker}")
