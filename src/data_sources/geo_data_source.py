import geopandas as gpd

import streamlit as st


# @st.cache
def load_data():
  return gpd.read_file('countries.json')
