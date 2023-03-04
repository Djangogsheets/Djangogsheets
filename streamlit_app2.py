# streamlit_app.py
from streamlit_faker import get_streamlit_faker

st_faker = get_streamlit_faker()
st_faker.subheader()
st_faker.markdown()
st_faker.selectbox()
st_faker.slider()
st_faker.map()
