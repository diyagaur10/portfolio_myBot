import streamlit as st
import google.generativeai as genai

api_key= st.secrets["GOOGLE_API_KEY"]

genai.configure(api_key=api_key)

model = genai.GenerativeModel('gemini-1.5-flash')

col1, col2 = st.columns(2)
with col1:
    st.subheader("Hi :wave: ")
    st.title("I am Diya Gaur")


with col2:
    st.image("images/Diya photo.jpg")
st.title(" ")

persona= """ You are Diya AI bot you help people answer questions about yourself (that is Diya). answer as if you are responding. don't answer in second or third person. if you don't know the answer you simple say "that a secret". here is more information about Diya. Diya is a third year student at MBM University Jodhpur currently pursuing bachelors of engineering in artificial intelligence and data science branch. she is familier with coding languages like python, c++, c, html,css, javascript. her hobbies are dancing, singing, painting and doing theater.her best friends are Lakshika and Meghna """

st.title("Diya's AI bot")

user_question = st.text_input("Ask anything about me.")
if st.button("ASK", use_container_width=400):
    prompt = persona + "Here is the question that the user asked: " +user_question
    response = model.generate_content(prompt)
    st.write(response.text)

st.title("")

col1, col2 =st.columns(2)
with col1:
    st.subheader("Youtube Channel")
    st.write("My first theater performance")

with col2:
    st.video("https://youtu.be/98E3c4fcRGQ?feature=shared")

st.write(" ")
st.title("My setup")
st.image("images/setup.jpg")
st.slider("Programming", 0,100,70)
st.slider("Teaching", 0,100,80)
st.slider("Dancing", 0,100,85)

st.write(" ")
st.title("Gallery")

col1, col2, col3= st.columns(3)

with col1:
    st.image("images/d1.jpg")
    st.image("images/d2.jpg")
    st.image("images/d3.jpg")

with col2:
    st.image("images/d4.jpg")
    st.image("images/d5.jpg")
    st.image("images/d6.jpg")

with col3:
    st.image("images/d7.jpg")
    st.image("images/d8.jpg")
    st.image("images/d9.jpg")

st.subheader(" ")
st.write("CONTACT")
st.title("FOR any enquiry, email at:")
st.subheader("diyagaur59@gmail.com")




