import streamlit as st # type: ignore
from streamlit_gsheets import GSheetsConnection # type: ignore

def show_hki():
    url = "https://docs.google.com/spreadsheets/d/1DDpIEI0RtUhYujHk6FqTcG7a2bLWD1cllR_IFfpR1bE/edit?usp=sharing"
    conn = st.connection("gsheets", type=GSheetsConnection)

    df_perolehan = conn.read(spreadsheet=url, usecols=list(range(6)), worksheet='310623266')
    df_pengusulan = conn.read(spreadsheet=url, usecols=list(range(5)), worksheet='1524255545')

    # Display the DataFrame for Perolehan
    st.header("(PEROLEHAN) HKI")
    st.dataframe(df_perolehan)

    # Display the DataFrame for Pengusulan
    st.header("(PENGUSULAN) HKI")
    st.dataframe(df_pengusulan)