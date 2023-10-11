import streamlit as st
import yfinance as yf
import pandas as pd
import time


st.title('MiCo BioMed Co., Ltd.')

samsung = yf.Ticker('214610.KQ') 

historical_data = samsung.history(period="14d") 

update_interval = 1  

chart = st.line_chart(historical_data['Close'])

current_price_text = st.empty()

while True:

    new_data = samsung.history(period="1d")

    historical_data = pd.concat([historical_data, new_data])

    chart.line_chart(historical_data['Close'])

    current_price = new_data['Close'].iloc[-1]
    
    current_price_text.text(f'Real time price: {current_price}')
   
    time.sleep(update_interval)
