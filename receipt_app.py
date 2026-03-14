import streamlit as st
from PIL import Image
import base64
from io import BytesIO

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="MJK File Uploader",
    page_icon=None,
    layout="centered",
)

# --- BRAND COLORS ---
BACKGROUND = "#F5E9D3"   # beige
BURGUNDY = "#7A1F1F"
BLACK = "#000000"

# --- PAGE STYLE ---
st.markdown(
    f"""
    <style>
        .main {{
            background-color: {BACKGROUND};
        }}
        .upload-box {{
            border: 2px solid {BURGUNDY};
            padding: 20px;
            border-radius: 10px;
            background-color: white;
        }}
    </style>
    """,
    unsafe_allow_html=True
)

# --- LOGO (CENTERED) ---
logo = Image.open("mjk_logo.png")

# Convert logo to base64
buffer = BytesIO()
logo.save(buffer, format="PNG")
img_str = base64.b64encode(buffer.getvalue()).decode()

# Center using flexbox
st.markdown(
    f"""
    <div style='display:flex; justify-content:center; margin-top:10px;'>
        <img src='data:image/png;base64,{img_str}' width='220'>
    </div>
    """,
    unsafe_allow_html=True
)

# --- TITLE ---
st.markdown(
    f"<h1 style='text-align:center; color:{BLACK}; margin-top:-10px;'>MJK File Uploader</h1>",
    unsafe_allow_html=True
)

# --- UPLOAD AREA ---
st.markdown("<div class='upload-box'>", unsafe_allow_html=True)

uploaded_file = st.file_uploader(
    "Upload a file",
    type=["jpg", "jpeg", "png"]
)

st.markdown("</div>", unsafe_allow_html=True)

# --- DISPLAY UPLOADED IMAGE ---
if uploaded_file is not None:
    st.success("Receipt uploaded successfully!")
    st.image(uploaded_file, caption="Uploaded Receipt", width=600)
    st.write("This is where your automation will process the receipt.")