import pandas as pd

import streamlit as st


@st.cache
def load_data():
  return pd.read_feather('historical_interest_rates.feather')
