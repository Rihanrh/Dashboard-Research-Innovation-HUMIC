import streamlit as st
import pandas as pd

# Read the Excel file
df = pd.read_excel('Data HUMIC 2024.xlsx')

# Display the DataFrame
st.dataframe(df)