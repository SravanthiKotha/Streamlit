import streamlit as st
import pandas as pd
from matplotlib import image
import pandas as pd
import numpy as np
import plotly.express as px

df = pd.read_csv("Data/emoji_data.csv")

img = image.imread("img\emoji.png")
st.set_page_config(layout="wide")
st.header("Emoji's data")
st.image(img)
col1, col2 = st.columns([1,2],gap="medium")
with col1:
    st.subheader("Here I have list of emoji's :sunglasses: \n Please select a emoji type, this app will give all emoji's for your desired type!!!")
    selected_group = st.selectbox("Select the type of emoji's:",df['group'].unique())
    plot_data = df.loc[df['group'].str.contains(selected_group, case=False)]
    sub_group = st.selectbox("select the type of subgroup : ",np.append((["All"]),plot_data['sub_group'].unique()))
    button_click = st.button("Get Emoji's")
with col2:
    st.subheader("Your desired emoji's : \n", )
    if(button_click):
        if(sub_group == "All"):
            st.subheader(" ".join(plot_data["emoji"]))
        else:
            st.subheader(" ".join(plot_data[plot_data["sub_group"]==sub_group]['emoji']))
