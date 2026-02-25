import streamlit as st
import pandas as pd

##*** author stramlit.io


st.title("Stream Tex input")

name = st.text_input("Enter your Name:")


age = st.slider("Select your age :" ,0 ,100,25)

st.write(f"Your age is {age}.")


options = ["Python","Java","c++"]
choice = st.selectbox("Chooose yor favorite langeuge:",options)
st.write(f"You select {choice}.")

if name :
    st.write(f"Helo , {name}")


data = {
    "Name ":["john","jane","jake","jill"],
    "Age": [28,24,35,40],
    "City":["New York", "Bankok" , "Pattani","Nonthaburi"]

    
}

df = pd.DataFrame(data)
df.to_csv("Sampledata.Csv")
st.write(df)



uploaded_file = st.file_uploader("Choose a CSV file",type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)