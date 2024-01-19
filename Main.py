import streamlit as st
from src.st_simple_gui import Inputs

st.warning('hi')


a = Inputs({'str': {'label': 'uno', 'value': 'default_value', 'kwargs': {'key': 'value'}}})

st.write((a._type,a._label,a._value,a._kwargs))


