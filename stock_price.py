import streamlit as st
import yfinance as yf    
import pandas as pd 

st.title("Simple stock price app")
st.subheader("Shown below are the closing price and Volume of Tesla")

ticker_symbol = 'TSLA'
ticker_data = yf.Ticker(ticker_symbol)
ticker_df = ticker_data.history(period="1d", start="2020-5-31", end="2022-5-31")

st.write("""
## Closing Price
""")
st.line_chart(ticker_df.Close)
st.write("""
## Volume
""")
st.line_chart(ticker_df.Volume)
st.write(ticker_df)