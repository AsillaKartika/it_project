import streamlit as st
import pandas as pd
import pickle  

# load the model from disk
loaded_model = pickle.load(open('tweets_all_data_clean_model.sav', 'rb'))
loaded_vec= pickle.load(open('vec_model.sav', 'rb'))


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
# Preformatted text
st.text("This is fixed-width text")
st.bar_chart(data_show.T) 


# Membuat prediksi
st.subheader('Prediksi hasil sentimen inflasi')

user_input = st.text_input("tweets")

res = loaded_model.predict(loaded_vec.transform(['coba ngobrolin geopolitik eropa timur dan inflasi turki yg meroket']))

if st.button('Prediksi'):
    st.write('Hasil Sentimen : ')
    st.write(res[0])