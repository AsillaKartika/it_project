import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('tweets_all_data_clean.csv')

neg = data['label'].value_counts()[-1]
net = data['label'].value_counts()[0]

pos = data['label'].value_counts()[1]
data_show= pd.DataFrame(data={'negatif' : [neg], 'positif': [pos], 'netral':[net]})
plt.bar(x_pos, height, color=['red', 'blue', 'lilac'])

st.title('Selamat datang di aplikasi Senasi')

st.subheader('Hasil Sentimen Inflasi dari komentar twitter')
st.bar_chart(data_show.T) 
