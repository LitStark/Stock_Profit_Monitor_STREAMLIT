from db import wallet_transactions, trade_transactions, SessionLocal, engine
from decimal import Decimal
import pandas as pd
from sqlalchemy.sql import func

def add_trade(stock:str, trade_type:str, trade_amount:Decimal, unit_stock_price:Decimal, trade_date, quantity:Decimal):
    session = SessionLocal()
    try:
        trade = trade_transactions(
            stock_name=stock,
            trade_type=trade_type,
            trade_amount=trade_amount,
            unit_stock_price=unit_stock_price,
            quantity=quantity,
            created_at=trade_date
        )
        session.add(trade)
        session.flush()
        if trade_type == "BUY":
            amount=-(trade_amount)
        else:
            amount=trade_amount

        wallet= wallet_transactions(
            trans_type=trade_type,
            amount=amount,
            ref_trade_id=trade.trade_id,
            created_at=trade_date,
        )

        session.add(wallet)
        session.commit()
        return True, "Trade added successfully."
    except Exception as e:
        session.rollback()
        return False, f"Error adding trade: {str(e)}"
    finally:
        session.close()

def wallet_action(trans_type:str, amount:Decimal,created_at):
    session = SessionLocal()
    try:
        if trans_type == "WITHDRAWAL":
            amount=-abs(Decimal(amount))
        else:
            amount=abs(Decimal(amount))

        wallet= wallet_transactions(
            trans_type=trans_type,
            amount=amount,
            created_at=created_at
        )
        session.add(wallet)
        session.commit()
        return True, "Wallet action recorded successfully."
    except Exception as e:
        session.rollback()
        return False, f"Error recording wallet action: {str(e)}"
    finally:
        session.close()

def get_wallet_balance():
    session = SessionLocal()
    try:
        result = session.query(
            func.COALESCE(func.SUM(wallet_transactions.amount), 0)
        ).scalar()
        return Decimal(result)
    except Exception as e:
        return Decimal(0)
    finally:
        session.close()


    return ti


    
