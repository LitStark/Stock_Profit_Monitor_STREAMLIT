# pages/3_Evaluation.py
import streamlit as st

st.set_page_config(page_title="EVALUATION | Stock Profit Monitor", page_icon="📈", layout="wide")

st.header("Stock Evaluation")

stock = st.selectbox("Select Stock", ["AAPL", "TSLA"])

st.subheader(f"Evaluation for {stock}")

col1, col2, col3 = st.columns(3)

col1.metric("Avg Buy", "$...")
col2.metric("Current Price", "$...")
col3.metric("Highest Price", "$...")

st.line_chart({
    "Price": [145, 150, 160, 170, 180]
})
