from db import engine
from decimal import Decimal
import pandas as pd
from pages.Holdings import get_market_price

def total_deposit():
    # Placeholder for total deposit calculation
    query = "SELECT SUM(amount) AS total_deposit FROM wallet_transactions WHERE trans_type = 'DEPOSIT'"
    df=pd.read_sql(query, engine)
    if not df.empty and df.iloc[0]['total_deposit'] is not None:
        return Decimal(df.iloc[0]['total_deposit'])
    else:
        return Decimal(0)
    
def total_invested():
    # Placeholder for unrealized P&L calculation
    query = "SELECT SUM(CASE WHEN trade_type = 'BUY' THEN (unit_stock_price * quantity) ELSE -(unit_stock_price * quantity) END) AS total_invested FROM trade_transactions group BY stock_name HAVING total_invested > 0"
    df=pd.read_sql(query, engine)
    if not df.empty and df.iloc[0]['total_invested'] is not None:
        ti = df["total_invested"].sum()
        return Decimal(ti)
    else:
        return Decimal(0)
    
def unrealized_pl():
    # Placeholder for unrealized P&L calculation
    query = "SELECT stock_name, SUM(CASE WHEN trade_type = 'BUY' THEN (unit_stock_price * quantity) ELSE -(unit_stock_price * quantity) END) AS total_invested,SUM(CASE WHEN trade_type = 'BUY' THEN quantity ELSE -quantity END) AS QUANTITY FROM trade_transactions group BY stock_name HAVING total_invested > 0"
    df=pd.read_sql(query, engine)
    df['MARKET PRICE'] = df['stock_name'].apply(get_market_price)
    if not df.empty and df.iloc[0]['total_invested'] is not None:
        upl = (df['MARKET PRICE'] * df['QUANTITY'] - df['total_invested']).sum()
        return Decimal(upl)
    else:
        return Decimal(0)
