import streamlit as st # type: ignore
from streamlit_option_menu import option_menu # type: ignore
from streamlit_gsheets import GSheetsConnection # type: ignore
import utils as ut # type: ignore

st.set_page_config(
    page_title="Research and Innovation",
    page_icon=":microscope:",
    layout="wide",
)
ut.sidebar_account()
st.title("Research and Innovation")

# Set the URL of the Google Sheets and the connection
url = "https://docs.google.com/spreadsheets/d/1DDpIEI0RtUhYujHk6FqTcG7a2bLWD1cllR_IFfpR1bE/edit?usp=sharing"
conn = st.connection("gsheets", type=GSheetsConnection)
perolehan_hibah_penelitian = conn.read(spreadsheet=url, usecols=list(range(13)), worksheet='1554272562')
pengusulan_hibah_penelitian = conn.read(spreadsheet=url, usecols=list(range(13)), worksheet='881437974')
perolehan_publikasi_ilmiah = conn.read(spreadsheet=url, usecols=list(range(10)), worksheet='1820188121')
pengusulan_publikasi_ilmiah = conn.read(spreadsheet=url, usecols=list(range(9)), worksheet='632236922')
perolehan_hki = conn.read(spreadsheet=url, usecols=list(range(6)), worksheet='310623266')
pengusulan_hki = conn.read(spreadsheet=url, usecols=list(range(5)), worksheet='1524255545')
perolehan_hibah_pengmas = conn.read(spreadsheet=url, usecols=list(range(13)), worksheet='369813888')
pengusulan_hibah_pengmas = conn.read(spreadsheet=url, usecols=list(range(13)), worksheet='592923655')
perolehan_hibah_industri = conn.read(spreadsheet=url, usecols=list(range(13)), worksheet='1329453071')
pengusulan_hibah_industri = conn.read(spreadsheet=url, usecols=list(range(13)), worksheet='1115369260')

# Calculate count for each category
hibah_penelitian_count = ut.count_non_nan_entries(perolehan_hibah_penelitian) + ut.count_non_nan_entries(pengusulan_hibah_penelitian)
publikasi_ilmiah_count = ut.count_non_nan_entries(perolehan_publikasi_ilmiah) + ut.count_non_nan_entries(pengusulan_publikasi_ilmiah)
hki_count = ut.count_non_nan_entries(perolehan_hki) + ut.count_non_nan_entries(pengusulan_hki)
hibah_pengmas_count = ut.count_non_nan_entries(perolehan_hibah_pengmas) + ut.count_non_nan_entries(pengusulan_hibah_pengmas)
hibah_industri_count = ut.count_non_nan_entries(perolehan_hibah_industri) + ut.count_non_nan_entries(pengusulan_hibah_industri)

# Add some space above the rounded corner boxes
st.write("")
st.write("")

# Colors and texts for the boxes
box_color = "#D32B28"
box_data = [
    (hibah_penelitian_count, "Hibah Penelitian"),
    (publikasi_ilmiah_count, "Publikasi Ilmiah"),
    (hki_count, "HKI"),
    (hibah_pengmas_count, "Hibah Pengmas"),
    (hibah_industri_count, "Hibah Industri"),
]

# Function to create a box with specific text
def create_box(number, text):
    return f"""
    <div style='
        background-color: {box_color};
        border-radius: 15px;
        padding: 20px;
        margin: 5px;
        text-align: center;
        color: white;
    '>
        <p>{number}</p>
        <p>{text}</p>
    </div>
    """

# Create columns for the boxes
box1, box2, box3, box4, box5 = st.columns(5)
boxes = [box1, box2, box3, box4, box5]

# Add boxes with specific texts
for box, (number, text) in zip(boxes, box_data):
    with box:
        st.markdown(create_box(number, text), unsafe_allow_html=True)

# Add some space below the rounded corner boxes
st.write("")
st.write("")

# Create columns for the option_menu and button
col1, col2, col3, col4, col5, col6, col7, col8 = st.columns([12, 1, 1, 1, 1, 1, 1, 2])

# Option menu in the first column
with col1:
    option_menu_styles = {
        "nav-link": {
            "background-color": "transparent",
            "color": "black",
            "text-decoration": "none",
            "font-weight": "normal",
            "border": "none",
            "transition": "none",
        },
        "nav-link:hover": {  # Hover style
            "color": "#F97066",
            "text-decoration": "none",
        },
        "nav-link-selected": {
            "background-color": "transparent",
            "color": "#F97066",  # Selected option color
            "text-decoration": "none",
            "font-weight": "normal",
            "border": "none",
            "transition": "none",
        },
        "icon": {
            "display": "none",
        },
        "container": {
            "background-color": "transparent",
        },
    }

    # Create the option menu with a unique key and the callback function for option change
    selected_option = option_menu(
        menu_title=None,
        options=["Hibah Penelitian", "Publikasi Ilmiah", "HKI", "Hibah Pengmas", "Hibah Industri"],
        orientation="horizontal",
        styles=option_menu_styles,
        default_index=0,
    )

category_perolehan = True
category_pengusulan = True
year_2024 = True
year_2023 = True

# Create a dialog function. Every element in it will show inside the dialog.
session_state = st.session_state.setdefault("filter", {})
@st.experimental_dialog("Filter")
def show_filter_dialog():
    st.subheader("Category")
    session_state["category_perolehan"] = st.checkbox("Perolehan", value=session_state.get("category_perolehan", True))
    session_state["category_pengusulan"] = st.checkbox("Pengusulan", value=session_state.get("category_pengusulan", True))

    st.subheader("Year")
    session_state["year_2024"] = st.checkbox("2024", value=session_state.get("year_2024", True))
    session_state["year_2023"] = st.checkbox("2023", value=session_state.get("year_2023", True))

    if st.button("Close"):
        st.rerun()

# Button in the second column
with col8:
    if st.button("Filter"):
        show_filter_dialog()

if selected_option == "Hibah Penelitian":
    perolehan_id = '1554272562'
    pengusulan_id = '881437974'

    if session_state.get("category_perolehan", True):
        ut.show_perolehan_hibah_penelitian(url, perolehan_id)
    if session_state.get("category_pengusulan", True):
        ut.show_pengusulan_hibah_penelitian(url, pengusulan_id)

elif selected_option == "Publikasi Ilmiah":
    perolehan_id = '1820188121'
    pengusulan_id = '632236922'
    year = None
    if session_state.get("year_2024", True):
        year = 2024
        if session_state.get("category_perolehan", True):
            ut.show_perolehan_publikasi_ilmiah(url, perolehan_id, year)
        if session_state.get("category_pengusulan", True):
            ut.show_pengusulan_publikasi_ilmiah(url, pengusulan_id, year)
    elif session_state.get("year_2023", True):
        year = 2023
        if session_state.get("category_perolehan", True):
            ut.show_perolehan_publikasi_ilmiah(url, perolehan_id, year)
        if session_state.get("category_pengusulan", True):
            ut.show_pengusulan_publikasi_ilmiah(url, pengusulan_id, year)

elif selected_option == "HKI":
    perolehan_id = '310623266'
    pengusulan_id = '1524255545'

    if session_state.get("category_perolehan", True):
        ut.show_perolehan_hki(url, perolehan_id)
    if session_state.get("category_pengusulan", True):
        ut.show_pengusulan_hki(url, pengusulan_id)

elif selected_option == "Hibah Pengmas":
    perolehan_id = '369813888'
    pengusulan_id = '592923655'

    if session_state.get("category_perolehan", True):
        ut.show_perolehan_hibah_pengmas(url, perolehan_id)
    if session_state.get("category_pengusulan", True):
        ut.show_pengusulan_hibah_pengmas(url, pengusulan_id)

elif selected_option == "Hibah Industri":
    perolehan_id = '1329453071'
    pengusulan_id = '1115369260'

    if session_state.get("category_perolehan", True):
        ut.show_perolehan_hibah_industri(url, perolehan_id)
    if session_state.get("category_pengusulan", True):
        ut.show_pengusulan_hibah_industri(url, pengusulan_id)