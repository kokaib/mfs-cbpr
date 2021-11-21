import streamlit as st

import plotly.express as px


def render(data):
  with st.container():
    selected_country = st.selectbox(
      'Country', sorted(set(data['country'].values))
    )
    country_data = data[data['country'] == selected_country].sort_values('date')
    fig = px.line(country_data[['date', 'interest_rate']].set_index('date'))
    st.plotly_chart(fig)
