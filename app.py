import streamlit as st 
st.title('New app in streamlit')
st.header('This is header in the page')
st.subheader('This is subheader')
st.write()
st.text_input('Enter your name')

import pandas as pd  
data=pd.DataFrame({'city':['kochi','chennai','bangalore'],'temperature':[30,40,35]})
st.dataframe(data)
st.slider('select your age',10,60)
st.selectbox('how would you like to contact?',('email','phone'))
