
import streamlit as st

from web_functions import load_data

st.set_page_config(
    page_title = 'Diabetes Prediction',
    page_icon ='🥯',
    layout = 'wide',
    initial_sidebar_state = 'auto'
)


from Tabs import home, data, predict, visualise

Tabs = {
    "Home": home,
    "Data Info": data,
    "Prediction": predict,
    "Visualisation": visualise
}

st.sidebar.title("Navigation")

page = st.sidebar.radio("Pages", list(Tabs.keys()))

df, X, y = load_data()

if page in ["Prediction", "Visualisation"]:
    Tabs[page].app(df, X, y)
elif (page == "Data Info"):
    Tabs[page].app(df)
else:
    Tabs[page].app()
