import streamlit as st
import pandas as pd
from streamlit_navigation_bar import st_navbar

# Create the navigation bar
page = st_navbar(["Home", "(PEROLEHAN)Hibah Penelitian", "(PENGUSULAN)Hibah Penelitian", "(PEROLEHAN)Publikasi Ilmiah", "(PENGUSULAN)Publikasi Ilmiah", "(PEROLEHAN)HKI", "(PENGUSULAN)HKI", "(PEROLEHAN)Hibah Pengmas", "(PENGUSULAN)Hibah Pengmas", "(PEROLEHAN)Hibah Industri", "(PENGUSULAN)Hibah Industri"])
st.write(page)

# Read the Excel file
df = pd.read_excel('Data HUMIC 2024.xlsx')

# Display the DataFrame
st.dataframe(df)