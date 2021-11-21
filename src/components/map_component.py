import streamlit as st
from streamlit_folium import folium_static
import branca.colormap as cm
import folium


_colormap = cm.linear.OrRd_09
_nan_color = '#000000'


def _style_function(feature):
  return {
    'fillColor': _colormap(
        feature['properties']['interest_rate_scaled'] ** (1/5)
      ) if feature['properties']['interest_rate'] is not None else _nan_color,
    'fillOpacity': 0.5
  }


def _highlight_function(feature):
  return {'fillOpacity': 0.8}


def render(data):
  with st.container():
    m = folium.Map()

    folium.GeoJson(
        data.to_json(),
        style_function=_style_function,
        highlight_function=_highlight_function,
        tooltip=folium.features.GeoJsonTooltip(
            fields=['country', 'interest_rate', 'change_label'],
            aliases=['Country', 'Interest Rate', 'Change']
          ),
        name='recent_interest_rates'
      ).add_to(m)

    folium_static(m)
