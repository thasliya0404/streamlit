import streamlit as st 
import pickle


st.write()
model=pickle.load(open('model_final.pkl','rb'))
st.title('Iris species prediction')
with st.form('iris_app_form'):
    sl=st.number_input('Sepal_Length')
    sw=st.number_input('Sepal_Width')
    pl=st.number_input('Petal_Length')
    pw=st.number_input('Petal_Width')
    submit=st.form_submit_button('predict species')

if st.button('predict'):
    prediction=model.predict([[sl,sw,pl,pw]])
    st.success(f'predicted Species:{prediction[0]}')