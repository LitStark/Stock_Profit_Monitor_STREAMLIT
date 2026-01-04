# pages/1_Dashboard.py
import streamlit as st
from datetime import date
from decimal import Decimal
from logic import add_trade, wallet_action, get_wallet_balance
from services.data_loader import total_invested, unrealized_pl, total_deposit
# from services import add_trade, wallet_action

st.set_page_config(page_title="DASHBOARD | Stock Profit Monitor",page_icon="📊", layout="wide")

st.title("Trading System")

st.header("Dashboard")

col1, col2, col3, col4, col5, col6 = st.columns(6)

col1.metric("Wallet Balance", f"${get_wallet_balance()}")
col2.metric("Total Deposit",f"${total_deposit()}")
col3.metric("Total Invested", f"${total_invested()}")
col4.metric("Currently Holding",f"${(total_invested()+unrealized_pl())}")
col5.metric("UnRealized P&l", f"${unrealized_pl()}")
col6.metric("Realized P&L", f"${(total_invested()+get_wallet_balance()-total_deposit())}")

st.header("Add New Transaction")

tab_trade, tab_wallet = st.tabs(["📈 Trade", "💰 Wallet"])

# ---------------- TRADE TAB ----------------
with tab_trade:
    st.header("Add Trade")

    with st.form("trade_form"):
        stock = st.text_input("Company Name")
        trade_type = st.selectbox("Trade Type", ["BUY", "SELL"])
        quantity = st.number_input("QTY ", min_value=0.000001, step=0.000001,format="%.5f")
        unit_stock_price = st.number_input("Unit Stock Price ($)", min_value=0.001, step=0.001,format="%.5f")
        trade_date = st.datetime_input("Trade Date", value=date.today())
        trade_amount = quantity * unit_stock_price

        submitted = st.form_submit_button("Submit Trade")

        if submitted:
            success, message = add_trade(
                stock=stock.upper(),
                trade_type=trade_type,
                trade_amount=Decimal(trade_amount),
                unit_stock_price=Decimal(unit_stock_price),
                trade_date=trade_date,
                quantity=Decimal(quantity)
            )

            if success:
                st.success(message)
            else:
                st.error(message)

# ---------------- WALLET TAB ----------------
with tab_wallet:
    st.header("Wallet Action")

    with st.form("wallet_form"):
        action_type = st.selectbox("Action", ["DEPOSIT", "WITHDRAW"])
        amount = st.number_input("Amount", min_value=0.01, step=0.01)
        create_at = st.datetime_input("Date", value=date.today())

        submitted = st.form_submit_button("SUBMIT")

        if submitted:
            success, message = wallet_action(
                trans_type=action_type,
                amount=Decimal(amount),
                created_at=create_at
            )

            if success:
                st.success(message)
            else:
                st.error(message)
