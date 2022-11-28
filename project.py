import streamlit as st
import pandas as pd

# membaca data berlabel hasil lexicon dan naive bayes
data = pd.read_csv('tweets_all_data_clean.csv')

# menampilkan jumlah nilai data label
neg = data['label'].value_counts()[-1]
net = data['label'].value_counts()[0]
pos = data['label'].value_counts()[1]
data_show= pd.DataFrame(data={'negatif' : [neg], 'positif': [pos], 'netral':[net]})

# menampilkan judul utama pada web
st.title('Selamat datang di aplikasi Senasi')
# menampilkan teks sub judul dan bar chart
st.subheader('Hasil Sentimen Inflasi dari komentar twitter')
st.bar_chart(data_show.T) 
