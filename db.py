from sqlalchemy import create_engine, Column, Integer, String, Enum, DATETIME, DECIMAL, ForeignKey,TIMESTAMP, DATE
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.sql import func
import os
# without this show NONE values in os.getenv()
from dotenv import load_dotenv  

# Load environment variables from .env file for python readability (for linux and docker not needed)
load_dotenv()       

# Load Database configuration from environment variables
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

engine = create_engine(
    f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}",echo= False,future= True,
    pool_pre_ping=True
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
base = declarative_base()

class trade_transactions(base):
    __tablename__ = "trade_transactions"
    # Define your columns here
    trade_id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    stock_name = Column(String(12),nullable=False)
    quantity = Column(DECIMAL(12, 4), nullable=False)
    unit_stock_price = Column(DECIMAL(10, 2), nullable=False)
    trade_amount = Column(DECIMAL(12, 2), nullable=False)
    created_at = Column(DATETIME, server_default=func.now(), nullable=False)
    trade_type = Column(Enum("BUY", "SELL"), nullable=False)
    

class wallet_transactions(base):
    __tablename__ = "wallet_transactions"
    # Define your columns here
    trans_id = Column(Integer, primary_key=True, index=True)
    trans_type = Column(Enum("BUY", "SELL","WITHDRAWAL","DEPOSIT"), nullable=False)
    amount = Column(DECIMAL(12, 2), nullable=False)
    ref_trade_id = Column(Integer, ForeignKey("trade_transactions.trade_id"), nullable=True)
    created_at = Column(DATETIME, server_default=func.now(), nullable=False)

# Create tables if they don't exist
def init_db():
    base.metadata.create_all(bind=engine)       

