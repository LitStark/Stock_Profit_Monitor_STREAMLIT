# Stock_Profit_Monitor_STREAMLIT
Stock Profit Monitor with yfinance API
## Overview
A Streamlit-based application that tracks stock holdings and evaluates profit/loss
using real-time market data.

## Features
- Portfolio tracking
- Profit and loss calculation
- Interactive dashboard

## Requirements
- Python 3.10+
- pip

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/LitStark/Stock_Profit_Monitor_STREAMLIT.git
   cd REPO_NAME
2. Create and Activate a Virutal Environment:
   ```bash
   python -m venv venv
   venv\Scripts\activate   # Windows
3. Install Dependencies:
   ```bash
   pip install -r requirement.txt

## Setup Database 
1. Install MySQL
2. Create database:
   ```bash
   CREATE DATABASE stockprofitmonitor;

3. Create .env file: (in root Directory)
   ```bash
   DB_USER=your_user
   DB_PASSWORD=your_password
   DB_HOST=localhost
   DB_PORT=port_number
   DB_NAME=stockprofitmonitor


## Run the App Using
```bash
streamlit run app.py
