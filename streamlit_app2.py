# streamlit_app.py
import streamlit as st
from PIL import Image
#from streamlit_faker import get_streamlit_faker

st.title("Hi Daar Sirah Jamien")

st.subheader("Bestel Vandag glimlag môre nog 'n Slag")

st.title("Gee vir die Dokter se vrou ook Blomme !!!")

st.markdown("Kontak Sirah direk op WHATS APP nr: 000 0000 0000")




bottom_image = st.file_uploader('"https://drive.google.com/file/d/1LvS9cqkz6ApCkgygoVK2EEmMwvxGvLLg/view?usp=share_link"', type='jpg', key=6)"', type='jpg', key=6)
if bottom_image is not None:
    image = Image.open(bottom_image)
    new_image = image.resize((600, 400))
    st.image(new_image)


