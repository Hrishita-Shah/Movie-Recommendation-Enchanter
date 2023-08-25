import base64
import streamlit as st

def header(url):
    st.markdown(f'<p style="color:#DC143C;font-style:bold;font-size:45px;">{url}</p>',
                unsafe_allow_html=True)
def header2(url):
    st.markdown(f'<p style="color:#DC143C;font-style:bold;font-size:30px;">{url}</p>',
                unsafe_allow_html=True)

def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()
def set_background(jpg_file):
    bin_str = get_base64(jpg_file)
    page_bg_img = '''
    <style>
    .stApp {
    background-image: url("data:image/jpg;base64,%s");
    background-size: cover;
    }
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)