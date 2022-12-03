import pickle
from pathlib import Path

import streamlit as st
names = ["Asilla", "User"]
usernames = ["Asll", "Usr"]
passwords = ["XXX", "XXX"]

hashed_passwords = st.Hasher(passwords).generate()

file_path = Path(__file__).parent / "hashed_pw.pkl"
with file_path.open("wb") as file:
    pickle.dump(hashed_passwords, file)