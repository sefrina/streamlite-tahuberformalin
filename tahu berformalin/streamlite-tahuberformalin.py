import pickle
import streamlit as st

#membaca model
rf_model = pickle.load(open('rf_model.sav', 'rb'))

#judul web
st.title('Data Mining prediksi tahu berformalin')

h2_MQ2 = st.text_input ('input nilai h2_MQ2')

lpg_MQ2 = st.tex_input ('input nilai lpg_MQ2')

co_MQ2 = st.tex_input ('input nilai C0_MQ2')

alcohol_MQ2 = st.text_input ('input nilai alcohol_MQ2')

propane_MQ2 = st.text_input ('input nilai propane_MQ2')

ch4_MQ4 = st.text_input ('input nilai ch4_MQ4')

smoke_MQ4 = st.text_input ('input nilai smoke_MQ4')

temperature = st.text_input ('input nilai temperature')

label = st.text_input ('input nilai label')

# code untuk prediksi
tahu_tahunosis = ''

#membuat tombol untuk prediksi
if st.button('test prediksi tahu berformalin'):
    tahu_prediction = rf_model.predict([[h2_MQ2, lpg_MQ2, co_MQ2, alcohol_MQ2, propane_MQ2, ch4_MQ4, smoke_MQ4, temperature, label]])

if(tahu_prediction[0] == 1):
    tahu_tahunosis = 'tahu berformalin'
else :
     tahu_tahunosis = 'tahu non formalin'

     st.success(tahu_tahunosis)
