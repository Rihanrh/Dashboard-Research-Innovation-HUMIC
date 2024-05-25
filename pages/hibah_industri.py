import streamlit as st # type: ignore
from streamlit_gsheets import GSheetsConnection # type: ignore

def show_hibah_industri():
    url = "https://docs.google.com/spreadsheets/d/1DDpIEI0RtUhYujHk6FqTcG7a2bLWD1cllR_IFfpR1bE/edit?usp=sharing"
    conn = st.connection("gsheets", type=GSheetsConnection)

    df_perolehan = conn.read(spreadsheet=url, usecols=list(range(13)), worksheet='1329453071')
    df_pengusulan = conn.read(spreadsheet=url, usecols=list(range(13)), worksheet='1115369260')

    # Display the DataFrame for Perolehan
    st.header("(PEROLEHAN) Hibah Industri")
    st.dataframe(df_perolehan)

    # Display the DataFrame for Pengusulan
    st.header("(PENGUSULAN) Hibah Industri")
    st.dataframe(df_pengusulan)