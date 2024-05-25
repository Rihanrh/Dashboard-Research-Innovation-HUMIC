import streamlit as st
from streamlit_gsheets import GSheetsConnection

def show_hibah_pengmas():
    url = "https://docs.google.com/spreadsheets/d/1DDpIEI0RtUhYujHk6FqTcG7a2bLWD1cllR_IFfpR1bE/edit?usp=sharing"
    conn = st.connection("gsheets", type=GSheetsConnection)

    df_perolehan = conn.read(spreadsheet=url, usecols=list(range(13)), worksheet='369813888')
    df_pengusulan = conn.read(spreadsheet=url, usecols=list(range(13)), worksheet='592923655')

    # Display the DataFrame for Perolehan
    st.header("(PEROLEHAN) Hibah Pengmas")
    st.dataframe(df_perolehan)

    # Display the DataFrame for Pengusulan
    st.header("(PENGUSULAN) Hibah Pengmas")
    st.dataframe(df_pengusulan)