## streamlit 

import streamlit as st
import pandas as pd
import numpy as np

## Title of the application
st.title("Hello Streamlit")

## create a simple dataframe
df=pd.DataFrame({
    'first column':[1,2,3,4],
    'second column':[10,20,30,40]
})

## Dsiplay the dataframe 
st.write("Here is the dataframe")
st.write(df)

## Create a line chart

chart_data=pd.DataFrame(
    np.random.randn(20,4),columns=['a','b','c','d']
)

st.line_chart(chart_data)

