import os
from pathlib import Path

import streamlit as st # type: ignore
from streamlit_navigation_bar import st_navbar # type: ignore

import pages as pg

st.set_page_config(initial_sidebar_state="collapsed")

pages = ["Hibah Penelitian", "Publikasi Ilmiah", "HKI", "Hibah Pengmas", "Hibah Industri"]
parent_dir = os.path.dirname(os.path.abspath(__file__))
styles = {
    "nav": {
        "background-color": "white",
        "justify-content": "middle",
    },
    "img": {
        "padding-right": "14px",
    },
    "span": {
        "color": "black",
        "padding": "14px",
    },
    "active": {
        "background-color": "white",
        "color": "var(--text-color)",
        "font-weight": "normal",
        "padding": "14px",
    }
}
options = {
    "show_menu": True,
    "show_sidebar": False,
}

page = st_navbar(
    pages,
    styles=styles,
    options=options,
)

functions = {
    "Hibah Penelitian": pg.show_hibah_penelitian,
    "Publikasi Ilmiah": pg.show_publikasi_ilmiah,
    "HKI": pg.show_hki,
    "Hibah Pengmas": pg.show_hibah_pengmas,
    "Hibah Industri": pg.show_hibah_industri,
}
go_to = functions.get(page)
if go_to:
    go_to()
