import streamlit as st
from streamlit_gsheets import GSheetsConnection

def show_publikasi_ilmiah():
    url = "https://docs.google.com/spreadsheets/d/1DDpIEI0RtUhYujHk6FqTcG7a2bLWD1cllR_IFfpR1bE/edit?usp=sharing"
    conn = st.connection("gsheets", type=GSheetsConnection)

    df_perolehan = conn.read(spreadsheet=url, usecols=list(range(10)), worksheet='1820188121')
    df_pengusulan = conn.read(spreadsheet=url, usecols=list(range(9)), worksheet='632236922')

    # Display the DataFrame for Perolehan
    st.header("(PEROLEHAN) Publikasi Ilmiah")
    st.dataframe(df_perolehan)

    # Display the DataFrame for Pengusulan
    st.header("(PENGUSULAN) Publikasi Ilmiah")
    st.dataframe(df_pengusulan)