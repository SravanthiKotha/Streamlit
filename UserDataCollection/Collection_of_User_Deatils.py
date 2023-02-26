import streamlit as st
import pandas as pd

from matplotlib import image
import os

# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)

df1 = pd.read_csv(os.path.join(PARENT_DIR),"Data/UserDetails.csv")
st.image(image.imread(os.path.join(PARENT_DIR),"img/images.jpeg"))
st.header("This page will save your details!! \n Please provide your details as requested!!")
name = st.text_input("please enter your name:")
if(len(name)>0):
    st.write("Welcome ",name)
    if(name.lower()=="admin"):
        st.dataframe(df1)
    else:
        lnkdn_url = st.text_input("Please provide your LinkedIn Profile URL")
        options = ["Student","IT Proffessional","Others"]
        profes = st.selectbox(label="professionality",options=options)
        address = st.text_input("your contact Address:")

        df = {"Name":name,"LinkedIn":lnkdn_url,"Proffession":profes,"Address":address}
        df1 = df1.append(df,ignore_index=True)
        if(len(address)>0):
            st.header("Your Details:")
            st.dataframe(df)
            df1.to_csv("Data/UserDetails.csv",index=False)
