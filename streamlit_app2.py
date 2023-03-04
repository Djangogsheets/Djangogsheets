# streamlit_app.py
import streamlit as st
from PIL import Image
#from streamlit_faker import get_streamlit_faker

st.title("Hi Daar Sirah Jamien")

st.subheader("Bestel Vandag glimlag môre nog 'n Slag")

st.title("Gee vir die Dokter se vrou ook Blomme !!!")

st.markdown("Kontak Sirah direk op WHATS APP nr: 000 0000 0000")


#image = Image.open(htp7)
#htp7 = "https://drive.google.com/file/d/1-3YgXi2RF2PqCpRu7YypDyfVwUal2Nab/view?usp=share_link" 
#st.image(htp7, caption= "The streamlit image from GOOGLE DRIVE", width=800)
image = st.file_uploader('"https://drive.google.com/file/d/1LvS9cqkz6ApCkgygoVK2EEmMwvxGvLLg/view?usp=share_link"', type='jpg', key=6)
if image is not None:
    image = Image.open(image)
    1new_image = image.resize((600, 400))
    st.image(1new_image)

bottom_image = st.file_uploader('"https://drive.google.com/file/d/1-3YgXi2RF2PqCpRu7YypDyfVwUal2Nab/view?usp=share_link"', type='jpg', key=6)
if bottom_image is not None:
    image = Image.open(bottom_image)
    new_image = image.resize((600, 400))
    st.image(new_image)


