import numpy as np 
import pandas as pd
import tensorflow as tf
from tensorflow.keras.models import Sequential 
from tensorflow.keras.layers import Embedding,SimpleRNN,Dense
from tensorflow.keras.preprocessing import sequence
from tensorflow.keras.models import load_model
from tensorflow.keras.datasets import imdb

## load the imdb dataset word inndex 
word_index=imdb.get_word_index()
reverse_word_index={value:key for key,value in word_index.items()}

## load the pretrained model 
model=load_model('simple_rnn_imbd.keras')

## Step 2; helper function 
def decode_review(encoded_review):
    return ' '.join([reverse_word_index.get(i-3,'?') for i in encoded_review])


## function to preprocess the user input 
def preprocess_text(text):
    words=text.lower().split()
    encoded_review=[word_index.get(word,2)+3 for word in words]
    padded_review=sequence.pad_sequences([encoded_review],maxlen=500)
    return padded_review


## Step 3: Prediction function 
def predict_sentiment(review):
    preprocessed_input=preprocess_text(review)
    prediction=model.predict(preprocessed_input)[0][0]
    sentiment='positive' if prediction>=0.5 else 'negative'
    return sentiment,prediction[0][0]



import streamlit as st 

## streamlit app 
st.title('Movie Review Sentiment Analysis')
st.write("Enter a movie review to predict its sentiment (positive or negative).")

## user input 

user_input=st.text_area("Movie Review")

if st.button("Classify"):
    preprocessed_input=preprocess_text(user_input)

    ## make prediction 
    prediction=model.predict(preprocessed_input)
    sentiment='positive' if prediction>=0.5 else 'negative'

    ## display the result 
    st.write(f"Predicted :{sentiment}")
    st.write(f"Prediction Score: {prediction[0][0]:.4f}")

else: 
    st.write("Please enter a movie review and click 'Classify' to see the prediction.")
