import streamlit as st
import yfinance as yf
import matplotlib.pyplot as plt
import time

st.title('MiCo BioMed Co., Ltd.')
text_input = st.text_input("Enter a stock symbol 👇")

# Create a Ticker object when a valid stock symbol is provided
mico = None
if text_input:
    mico = yf.Ticker(text_input)

fig, ax = plt.subplots()
plot = st.pyplot(fig)

current_price_text = st.empty()
while True:
    try:
        if mico:
            historical_prices = mico.history(period='1d', interval='1m')
            if not historical_prices.empty:
                latest_price = historical_prices['Close'].iloc[-1]
                latest_time = historical_prices.index[-1].strftime('%H:%M:%S')
                ax.clear()
                ax.plot(historical_prices.index, historical_prices['Close'], label='Stock Value')
                ax.set_xlabel('Time')
                ax.set_ylabel('Stock Value')
                ax.set_title(text_input)
                ax.legend(loc='upper left')
                ax.tick_params(axis='x', rotation=45)
                plot.pyplot(fig)
                new_data = mico.history(period='1d', interval='1m')
                current_price = new_data['Close'].iloc[-1]
                current_price_text.text(f'Real-time price: ({latest_time}) {current_price}')
        time.sleep(1)
    except IndexError:
        # Handle the "IndexError" when it occurs, e.g., when there's no data available
        current_price_text.text("No data available for the specified stock symbol.")
        time.sleep(60)  # Sleep for a longer time to avoid frequent retries

