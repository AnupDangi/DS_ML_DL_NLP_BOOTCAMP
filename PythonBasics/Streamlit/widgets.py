import streamlit as st
import pandas as pd
import numpy as np 


st.title("Streamlit Text Input")

name=st.text_input("Enter your name:")

age=st.slider("Select your age:",0,100,25)

st.write(f"Your age is :{age}")

if name and  str.isalpha(name) :
    st.write(f"Hello,{name}")
    

st.write("Choose your favotite programming language")

options=["Python","Java"]
choice=st.selectbox("Choose your favorite language",options)
st.write(f"You selected {choice}.")

uploaded_file=st.file_uploader("choose a CSV file",type='csv')

if uploaded_file is not None:
    df=pd.read_csv(uploaded_file)
    st.write(df)
    
