import streamlit as st

from data_sources import (
  geo_recent_data_source,
  historical_data_source,
  recent_data_source
)
from components import (
  country_details_component,
  map_component,
  sidebar_component,
  top_value_component
)


recent_data = recent_data_source.load_data()
historical_data = historical_data_source.load_data()
geo_recent_data = geo_recent_data_source.load_data()

sidebar_component.render()

with st.container():
  map_component.render(geo_recent_data)
  country_details_component.render(historical_data)
  top_value_component.render(recent_data)
