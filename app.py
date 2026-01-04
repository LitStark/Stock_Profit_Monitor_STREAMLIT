import streamlit as st

st.set_page_config(
    page_title="HOME |  Stock Profit Monitor",
    page_icon="📊",
    layout="centered"
)

st.markdown(
    """
    <style>
    .welcome-box {
        text-align: center;
        padding: 40px;
        border-radius: 12px;
        background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
        color: white;
    }
    .welcome-title {
        font-size: 40px;
        font-weight: 700;
        margin-bottom: 10px;
    }
    .welcome-subtitle {
        font-size: 18px;
        opacity: 0.9;
        margin-bottom: 30px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="welcome-box">
        <div class="welcome-title">📊 Profit Monitor</div>
        <div class="welcome-subtitle">
            Track trades • Monitor holdings • Analyze profit
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

st.write("")
st.write("")

col1, col2, col3 = st.columns(3)

with col1:
    st.info("📈 **Trades**\n\nBuy & sell stocks with full history")

with col2:
    st.info("📦 **Holdings**\n\nView your current stock positions")

with col3:
    st.info("💰 **Wallet**\n\nTrack cash balance & transactions")

st.write("")
st.success("Use the sidebar to get started.")

