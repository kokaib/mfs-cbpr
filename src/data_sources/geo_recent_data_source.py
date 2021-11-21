from sklearn.preprocessing import MinMaxScaler
import streamlit as st

from . import (
  geo_data_source,
  recent_data_source
)


def load_data():
  geo_data = geo_data_source.load_data()
  interest_rate_data = recent_data_source.load_data()

  scaler = MinMaxScaler()
  interest_rate_data['interest_rate_scaled'] = scaler.fit_transform(
      interest_rate_data['interest_rate'].values.reshape(
        (interest_rate_data['interest_rate'].values.shape[0], 1)
      )
    )

  interest_rate_data['change_label'] = interest_rate_data['change'].apply(
      lambda x: f'{"+" if x > 0 else ""}{x:0.2f}'
    )

  data = geo_data.join(
      interest_rate_data.set_index('country'),
      on='country'
    ).drop(columns=['date', 'date_previous'])

  return data
