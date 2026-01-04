# pages/2_Holdings.py
import streamlit as st
import pandas as pd
from db import SessionLocal, engine
import yfinance as yf
# --------------------------
#     Page Configuration
# --------------------------
st.set_page_config(page_title="HOLDINGS | Stock Profit Monitor", page_icon="📦", layout="wide")
st.header("Current Holdings")
session = SessionLocal()
# ----------------------------
#     SQL Query to fetch holdings
# ----------------------------
query = """
SELECT 
    stock_name as 'STOCK NAME',
    SUM(CASE WHEN trade_type = 'BUY' THEN quantity ELSE -quantity END) AS QUANTITY,
    AVG(CASE WHEN trade_type = 'BUY' THEN unit_stock_price END) AS 'AVG. PRICE',
    SUM(CASE 
            WHEN trade_type = 'BUY' THEN (unit_stock_price * quantity) 
            ELSE -(unit_stock_price * quantity) 
            END) AS 'TOTAL INVESTMENT' 
FROM trade_transactions 
GROUP BY stock_name 
HAVING QUANTITY > 0
"""
# ----------------------------
#   Fetch data and calculate market values
# ----------------------------
st.cache_data(ttl=300)
def get_market_price(ticker_symbol):
    try:
        ticker = yf.Ticker(ticker_symbol)

        # Fast path
        price = ticker.fast_info.get("lastPrice")
        if price:
            return price

        # Fallback
        hist = ticker.history(period="1d")
        if not hist.empty:
            return hist["Close"].iloc[-1]

    except Exception:
        pass

    return 0.0
# ─────────────────────────────────────────────
# Load data
# ─────────────────────────────────────────────
df = pd.read_sql(query, engine)

df['MARKET PRICE'] = df['STOCK NAME'].apply(get_market_price)
df['MARKET VALUE'] = df['QUANTITY'] * df['MARKET PRICE']
df['UNREALIZED P/L'] = df['MARKET VALUE'] - df['TOTAL INVESTMENT']
df=df.round(2)
st.dataframe(df, use_container_width=True, height=500, hide_index=True)

st.info("Holdings are derived from trade transactions and cannot be edited.")
session.close()