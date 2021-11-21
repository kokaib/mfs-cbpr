import streamlit as st
import numpy as np


def render(data):
  with st.container():
    col1, col2 = st.columns(2)

    with col1:
      sort_by = st.radio('Sort By', options=['Interest Rate', 'Change'])
    with col2:
      direction = st.radio('Sort Direction', options=['Descending', 'Ascending'])

  df = data[[
      'country', 'date', 'interest_rate', 'change',
      'date_previous', 'interest_rate_previous'
    ]].rename(
      columns={
          'country': 'Country',
          'date': 'Date',
          'interest_rate': 'Interest Rate',
          'change': 'Change',
          'date_previous': 'Previous Date',
          'interest_rate_previous': 'Previous Interest Rate'
        }
    ).sort_values(sort_by, ascending=(direction == 'Ascending'))
  df.index = np.arange(1, len(df) + 1)

  with st.container():
    st.dataframe(df)
