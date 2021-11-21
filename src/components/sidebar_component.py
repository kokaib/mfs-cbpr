import streamlit as st


def render():
  st.sidebar.write('''
    # Central Bank Interest Rates By Country

    Sources: 
      * [IMF](https://data.imf.org/regular.aspx?key=63087881)
      * [Trading Economics](https://tradingeconomics.com/country-list/interest-rate?continent=world)
  ''')
