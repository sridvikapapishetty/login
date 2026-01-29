import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="Student_db"
    )
    cur = con.cursor()
    
import streamlit as st
st.header("REGISRTATION")
name = st.text_input("enter your name:")
if name == "":
    st.warning("name cannot be empty!")
elif not name.isalpha():
    st.error("invalid input please enter only alphabets")
collegename = st.text_input("enter your college name:")
if collegename == "":
    st.warning("collegename cannot be empty!")
elif not name.isalpha():
    st.error("invalid input please enter only alphabets")
gender = st.radio("Select you gender:",("Male","female","other"))
st.write(f"you selected, {gender}")
    