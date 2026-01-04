# import yfinance as yf

# ticker_symbol = 'AAPL' # Example: Apple Inc. stock symbol
# ticker_data = yf.Ticker(ticker_symbol)

# # Get the most recent market price (can be slightly delayed)
# current_price = ticker_data.info.get('regularMarketPrice')

# if current_price:
#     print(f"The current price of {ticker_symbol} is: ${current_price}")
# else:
#     # For real-time data, use history with a 1-minute interval and get the last close price
#     hist = ticker_data.history(period="1d", interval="1m")
#     if not hist.empty:
#         current_price = hist['Close'].iloc[-1]
#         print(f"The current price of {ticker_symbol} is: ${current_price:.2f}")
#     else:
#         print(f"Could not retrieve the current price for {ticker_symbol}.")

# import streamlit as st
# import pandas as pd
# from sqlalchemy import create_engine

# engine = create_engine(
#     "mysql+pymysql://root:Mysql%401234@localhost:3306/stockprofitmonitor"
# )

# query = "SELECT * FROM transactions"

# df = pd.read_sql(query, engine)
# print(df)
# # st.dataframe(df, use_container_width=True)