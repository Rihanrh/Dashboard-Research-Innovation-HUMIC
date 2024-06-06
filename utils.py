import streamlit as st # type: ignore
import pandas as pd # type: ignore
from streamlit_gsheets import GSheetsConnection # type: ignore
import io # type: ignore

def sidebar_account():
    with st.sidebar:
        st.image("https://img.freepik.com/premium-vector/avatar-icon002_750950-52.jpg", width=100)  
        st.write("Jane Doe")

def count_non_nan_entries(df):
    first_column = df.iloc[0:, 0]  # Select the first column starting from the second row
    return first_column.dropna().count()

def show_perolehan_hibah_penelitian(url, worksheet_id, year, author=""):
    conn = st.connection("gsheets", type=GSheetsConnection)
    df = conn.read(spreadsheet=url, usecols=list(range(14)), worksheet=worksheet_id)

    # Filter the DataFrame based on the author's name
    if author:
        df = df[df['NAMA LENGKAP'].str.contains(author, case=False)]

    for index, row in df.iterrows():
        judul_penelitian = row[5]
        nama_hibah = row[6]
        nama_lengkap = row[1]
        tahun = row[13]

        if not pd.isna(judul_penelitian) and not pd.isna(nama_lengkap):
            if year is None or tahun == year:
                # Define the box content
                box_content = f"""<b>{judul_penelitian}</b>
{nama_hibah}
{nama_lengkap}
{tahun}
Perolehan
"""

                # Create the box using a container
                with st.container():
                    st.write("")  # Add space before the container
                    st.markdown(f"""
                    <div style="
                        background-color: white;
                        padding: 20px;
                        border: 1px solid black;
                        border-radius: 5px;
                    ">
                        <div style="
                            font-family: sans-serif;
                            white-space: pre-wrap;
                            word-wrap: break-word;
                        ">{box_content}</div>
                    </div>
                    """, unsafe_allow_html=True)
                    st.write("")  # Add space after the container

def show_pengusulan_hibah_penelitian(url, worksheet_id, year, author=""):
    conn = st.connection("gsheets", type=GSheetsConnection)
    df = conn.read(spreadsheet=url, usecols=list(range(14)), worksheet=worksheet_id)

    # Filter the DataFrame based on the author's name
    if author:
        df = df[df['NAMA LENGKAP'].str.contains(author, case=False)]

    for index, row in df.iterrows():
        judul_penelitian = row[5]  
        nama_hibah = row[6]
        nama_lengkap = row[1]  
        tahun_pengusulan = row[13]

        if not pd.isna(judul_penelitian) and not pd.isna(nama_lengkap):
            if year is None or tahun_pengusulan == year:
                # Define the box content
                box_content = f"""<b>{judul_penelitian}</b>
{nama_hibah}
{nama_lengkap}
{tahun_pengusulan}
Pengusulan
"""

                # Create the box using a container
                with st.container():
                    st.write("")  # Add space before the container
                    st.markdown(f"""
                    <div style="
                        background-color: white;
                        padding: 20px;
                        border: 1px solid black;
                        border-radius: 5px;
                    ">
                        <div style="
                            font-family: sans-serif;
                            white-space: pre-wrap;
                            word-wrap: break-word;
                        ">{box_content}</div>
                    </div>
                    """, unsafe_allow_html=True)
                    st.write("")  # Add space after the container

def show_perolehan_publikasi_ilmiah(url, worksheet_id, year, author=""):
    conn = st.connection("gsheets", type=GSheetsConnection)
    df = conn.read(spreadsheet=url, usecols=list(range(10)), worksheet=worksheet_id)

    if author:
        df = df[df['AUTHOR'].str.contains(author, case=False)]

    for index, row in df.iterrows():
        judul_artikel = row[6] 
        author = row[7]
        tahun_publish = row[8] 

        if not pd.isna(judul_artikel) and not pd.isna(author) and not pd.isna(tahun_publish):
            # Convert tahun_publish to integer to remove decimal point
            tahun_publish = int(tahun_publish)

            # Check if the year matches the specified year
            if year is None or tahun_publish == year:
                # Define the box content
                box_content = f"""<b>{judul_artikel}</b>
{author}
{tahun_publish}
Perolehan
"""

                # Create the box using a container
                with st.container():
                    st.write("")  # Add space before the container
                    st.markdown(f"""
                    <div style="
                        background-color: white;
                        padding: 20px;
                        border: 1px solid black;
                        border-radius: 5px;
                    ">
                        <div style="
                            font-family: sans-serif;
                            white-space: pre-wrap;
                            word-wrap: break-word;
                        ">{box_content}</div>
                    </div>
                    """, unsafe_allow_html=True)
                    st.write("")  # Add space after the container

def show_pengusulan_publikasi_ilmiah(url, worksheet_id, year, author=""):
    conn = st.connection("gsheets", type=GSheetsConnection)
    df = conn.read(spreadsheet=url, usecols=list(range(9)), worksheet=worksheet_id)

    if author:
        df = df[df['AUTHOR'].str.contains(author, case=False)]

    for index, row in df.iterrows():
        judul_artikel = row[6] 
        author = row[7]
        tahun_publish = row[8] 

        if not pd.isna(judul_artikel) and not pd.isna(author) and not pd.isna(tahun_publish):
            # Convert tahun_publish to integer to remove decimal point
            tahun_publish = int(tahun_publish)

            # Check if the year matches the specified year
            if year is None or tahun_publish == year:
                # Define the box content
                box_content = f"""<b>{judul_artikel}</b>
{author}
{tahun_publish}
Pengusulan
"""

                # Create the box using a container
                with st.container():
                    st.write("")  # Add space before the container
                    st.markdown(f"""
                    <div style="
                        background-color: white;
                        padding: 20px;
                        border: 1px solid black;
                        border-radius: 5px;
                    ">
                        <div style="
                            font-family: sans-serif;
                            white-space: pre-wrap;
                            word-wrap: break-word;
                        ">{box_content}</div>
                    </div>
                    """, unsafe_allow_html=True)
                    st.write("")  # Add space after the container

def show_perolehan_hki(url, worksheet_id, year, author=""):
    conn = st.connection("gsheets", type=GSheetsConnection)
    df = conn.read(spreadsheet=url, usecols=list(range(7)), worksheet=worksheet_id)

    if author:
        df = df[df['NAMA LENGKAP'].str.contains(author, case=False)]

    for index, row in df.iterrows():
        nama_produk = row[3] 
        asal_institusi = row[2]
        nama_lengkap = row[1]
        tahun = row[6]

        if not pd.isna(nama_produk) and not pd.isna(nama_lengkap):
            # Define the box content
            if year is None or tahun == year:
                box_content = f"""<b>{nama_produk}</b>
{asal_institusi}
{nama_lengkap}
{tahun}
Perolehan
"""

                # Create the box using a container
                with st.container():
                    st.write("")  # Add space before the container
                    st.markdown(f"""
                    <div style="
                        background-color: white;
                        padding: 20px;
                        border: 1px solid black;
                        border-radius: 5px;
                    ">
                        <div style="
                            font-family: sans-serif;
                            white-space: pre-wrap;
                            word-wrap: break-word;
                        ">{box_content}</div>
                    </div>
                    """, unsafe_allow_html=True)
                    st.write("")  # Add space after the container

def show_pengusulan_hki(url, worksheet_id, year, author=""):
    conn = st.connection("gsheets", type=GSheetsConnection)
    df = conn.read(spreadsheet=url, usecols=list(range(6)), worksheet=worksheet_id)

    if author:
        df = df[df['NAMA LENGKAP'].str.contains(author, case=False)]

    for index, row in df.iterrows():
        nama_produk = row[3]  
        asal_institusi = row[2]
        nama_lengkap = row[1]  
        tahun = row[5]

        if not pd.isna(nama_produk) and not pd.isna(nama_lengkap):
            if year is None or tahun == year:
                # Define the box content
                box_content = f"""<b>{nama_produk}</b>
{asal_institusi}
{nama_lengkap}
{tahun}
Pengusulan
"""

                # Create the box using a container
                with st.container():
                    st.write("")  # Add space before the container
                    st.markdown(f"""
                    <div style="
                        background-color: white;
                        padding: 20px;
                        border: 1px solid black;
                        border-radius: 5px;
                    ">
                        <div style="
                            font-family: sans-serif;
                            white-space: pre-wrap;
                            word-wrap: break-word;
                        ">{box_content}</div>
                    </div>
                    """, unsafe_allow_html=True)
                    st.write("")  # Add space after the container

def show_perolehan_hibah_pengmas(url, worksheet_id, year, author=""):
    conn = st.connection("gsheets", type=GSheetsConnection)
    df = conn.read(spreadsheet=url, usecols=list(range(14)), worksheet=worksheet_id)

    if author:
        df = df[df['NAMA LENGKAP'].str.contains(author, case=False)]

    for index, row in df.iterrows():
        judul_penelitian = row[5] 
        nama_hibah = row[6]
        asal_institusi = row[2]
        nama_lengkap = row[1]
        tahun = row[13] 

        if not pd.isna(judul_penelitian) and not pd.isna(nama_lengkap):
            if year is None or tahun == year:
                # Define the box content
                box_content = f"""<b>{judul_penelitian}</b>
{nama_hibah}
{asal_institusi}
{nama_lengkap}
{tahun}
Perolehan
"""

                # Create the box using a container
                with st.container():
                    st.write("")  # Add space before the container
                    st.markdown(f"""
                    <div style="
                        background-color: white;
                        padding: 20px;
                        border: 1px solid black;
                        border-radius: 5px;
                    ">
                        <div style="
                            font-family: sans-serif;
                            white-space: pre-wrap;
                            word-wrap: break-word;
                        ">{box_content}</div>
                    </div>
                    """, unsafe_allow_html=True)
                    st.write("")  # Add space after the container

def show_pengusulan_hibah_pengmas(url, worksheet_id, year, author=""):
    conn = st.connection("gsheets", type=GSheetsConnection)
    df = conn.read(spreadsheet=url, usecols=list(range(14)), worksheet=worksheet_id)

    if author:
        df = df[df['NAMA LENGKAP'].str.contains(author, case=False)]

    for index, row in df.iterrows():
        judul_penelitian = row[5] 
        nama_hibah = row[6]
        asal_institusi = row[2]
        nama_lengkap = row[1] 
        tahun = row[13]

        if not pd.isna(judul_penelitian) and not pd.isna(nama_lengkap):
            if year is None or tahun == year:
                # Define the box content
                box_content = f"""<b>{judul_penelitian}</b>
{nama_hibah}
{asal_institusi}
{nama_lengkap}
{tahun}
Pengusulan
"""

                # Create the box using a container
                with st.container():
                    st.write("")  # Add space before the container
                    st.markdown(f"""
                    <div style="
                        background-color: white;
                        padding: 20px;
                        border: 1px solid black;
                        border-radius: 5px;
                    ">
                        <div style="
                            font-family: sans-serif;
                            white-space: pre-wrap;
                            word-wrap: break-word;
                        ">{box_content}</div>
                    </div>
                    """, unsafe_allow_html=True)
                    st.write("")  # Add space after the container

def show_perolehan_hibah_industri(url, worksheet_id, year, author=""):
    conn = st.connection("gsheets", type=GSheetsConnection)
    df = conn.read(spreadsheet=url, usecols=list(range(14)), worksheet=worksheet_id)

    if author:
        df = df[df['NAMA LENGKAP'].str.contains(author, case=False)]

    for index, row in df.iterrows():
        judul_penelitian = row[5] 
        nama_hibah = row[6]
        asal_institusi = row[2]
        nama_lengkap = row[1] 
        tahun = row[13]

        if not pd.isna(judul_penelitian) and not pd.isna(nama_lengkap):
            if year is None or tahun == year:
                # Define the box content
                box_content = f"""<b>{judul_penelitian}</b>
{nama_hibah}
{asal_institusi}
{nama_lengkap}
{tahun}
Perolehan
"""

                # Create the box using a container
                with st.container():
                    st.write("")  # Add space before the container
                    st.markdown(f"""
                    <div style="
                        background-color: white;
                        padding: 20px;
                        border: 1px solid black;
                        border-radius: 5px;
                    ">
                        <div style="
                            font-family: sans-serif;
                            white-space: pre-wrap;
                            word-wrap: break-word;
                        ">{box_content}</div>
                    </div>
                    """, unsafe_allow_html=True)
                    st.write("")  # Add space after the container

def show_pengusulan_hibah_industri(url, worksheet_id, year, author=""):
    conn = st.connection("gsheets", type=GSheetsConnection)
    df = conn.read(spreadsheet=url, usecols=list(range(14)), worksheet=worksheet_id)

    if author:
        df = df[df['NAMA LENGKAP'].str.contains(author, case=False)]

    for index, row in df.iterrows():
        judul_penelitian = row[5] 
        nama_hibah = row[6]
        asal_institusi = row[2]
        nama_lengkap = row[1] 
        tahun = row[13]

        if not pd.isna(judul_penelitian) and not pd.isna(nama_lengkap):
            if year is None or tahun == year:
                # Define the box content
                box_content = f"""<b>{judul_penelitian}</b>
{nama_hibah}
{asal_institusi}
{nama_lengkap}
{tahun}
Pengusulan
"""

                # Create the box using a container
                with st.container():
                    st.write("")  # Add space before the container
                    st.markdown(f"""
                    <div style="
                        background-color: white;
                        padding: 20px;
                        border: 1px solid black;
                        border-radius: 5px;
                    ">
                        <div style="
                            font-family: sans-serif;
                            white-space: pre-wrap;
                            word-wrap: break-word;
                        ">{box_content}</div>
                    </div>
                    """, unsafe_allow_html=True)
                    st.write("")  # Add space after the container