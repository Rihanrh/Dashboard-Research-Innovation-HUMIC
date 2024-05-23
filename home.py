import streamlit as st
from streamlit_navigation_bar import st_navbar
import pandas as pd

page = st_navbar(["Home", "(PEROLEHAN)Hibah Penelitian", "(PENGUSULAN)Hibah Penelitian", "(PEROLEHAN)Publikasi Ilmiah", "(PENGUSULAN)Publikasi Ilmiah", "(PEROLEHAN)HKI", "(PENGUSULAN)HKI", "(PEROLEHAN)Hibah Pengmas", "(PENGUSULAN)Hibah Pengmas", "(PEROLEHAN)Hibah Industri", "(PENGUSULAN)Hibah Industri"])
st.write(page)