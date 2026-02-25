import streamlit as st 
import numpy as np 
import tensorflow as tf 
from sklearn.preprocessing import StandardScaler,LabelEncoder,OneHotEncoder

import pandas as pd 
import numpy as np 
import pickle


## load the trained models 
model=tf.keras.models.load_model('model.h5')

## load the encoders and scalers 
with open('label_encoder_gender.pkl','rb') as f: 
    label_encoder_gender=pickle.load(f)

with open('onehot_encoder_geo.pkl','rb') as f:
    onehot_encoder_geo=pickle.load(f)

with open('scaler.pkl','rb') as f: 
    scaler=pickle.load(f)


## streamlit app 
st.title('Customer Churn Prediction')

## user inputs 
geography=st.selectbox('Geography',onehot_encoder_geo.categories_[0])
gender=st.selectbox('Gender',label_encoder_gender.classes_)
age=st.slider('Age',18,100,30)
balance=st.slider('Balance',0.0,250000.0,50000.0)
credit_score=st.slider('Credit Score',300,850,600)
estimated_salary=st.slider('Estimated Salary',0.0,200000.0,50000.0)
tenure=st.slider('Tenure',0,10,3)
num_of_products=st.slider('Number of Products',1,4,2)
has_cr_card=st.selectbox('Has Credit Card', ['0', '1'])
is_active_member=st.selectbox('Is Active Member', ['0', '1'])



## preprocess the inputs
input_data = pd.DataFrame({
    'CreditScore': [credit_score],
    'Geography': [geography],
    'Gender': [gender],
    'Age': [age],
    'Tenure': [tenure],
    'Balance': [balance],
    'NumOfProducts': [num_of_products],
    'HasCrCard': [int(has_cr_card)],
    'IsActiveMember': [int(is_active_member)],
    'EstimatedSalary': [estimated_salary],
})

# one-hot encode 'Geography'
geo_encoded = onehot_encoder_geo.transform(input_data[['Geography']])
geo_cols = onehot_encoder_geo.get_feature_names_out(['Geography'])
geo_encoded_df = pd.DataFrame(geo_encoded, columns=geo_cols)

# label encode 'Gender'
input_data['Gender'] = label_encoder_gender.transform(input_data['Gender'])

# drop original geography and concat one-hot columns
input_df = pd.concat(
    [input_data.drop('Geography', axis=1).reset_index(drop=True),
     geo_encoded_df.reset_index(drop=True)],
    axis=1,
)

# wait for user to submit before running prediction
if st.button('Submit'):
    # scale and predict
    input_scaled = scaler.transform(input_df)
    prediction = model.predict(input_scaled)[0][0]

    # display results
    st.write('### Input features')
    st.write(input_df)

    st.write('### Churn probability')
    st.write(f"{prediction:.2f}")

    if prediction > 0.5:
        st.warning('Customer is likely to churn.')
    else:
        st.success('Customer is unlikely to churn.')
