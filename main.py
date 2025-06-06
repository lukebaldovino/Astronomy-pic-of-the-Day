import streamlit as st
import requests
from datetime import datetime
import creds

URL = f"https://api.nasa.gov/planetary/apod?api_key={creds.API_KEY}"
params = {"api_key": creds.API_KEY}

st.title("🌌Astronomy Pic of the Day!🌌")

response = requests.get("https://api.nasa.gov/planetary/apod", params=params)
data = response.json()

st.header(f"✨{data.get('title')}✨")
get_date = datetime.strptime(data.get("date"), "%Y-%m-%d")
format_date = get_date.strftime("%B %d, %Y")
st.subheader(format_date)
st.image(data.get("url"))

st.write(data.get("explanation"))


st.markdown(
    '<p>Powered by <a href="https://api.nasa.gov/">NASA API</a></p>', unsafe_allow_html=True
)

st.markdown('<p><small>made by <a href="https://github.com/lukebaldovino"> me💗 </a></small)</p>', unsafe_allow_html=True)

