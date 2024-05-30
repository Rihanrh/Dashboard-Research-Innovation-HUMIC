import streamlit as st # type: ignore
import utils as ut

st.set_page_config(
    page_title="Dashboard",
    page_icon=":bar_chart:",
)

ut.sidebar_account()
st.title("Dashboard")