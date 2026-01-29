import streamlit as st

st.header("Students Record Management")

st.title("Student CRUD Application")

st.subheader("Manage student records efficiently and effectively.")

st.markdown("------------------------------------------------------------")

st.text("This application allows you to perform CRUD operations using database")

st.write("hello")
st.write({"name": "sridvika", "Marks": 90})

st.markdown("**Bold Text**")
st.markdown("*Italic Text*")
st.markdown("- Item 1\n- Item 2\n")

st.markdown("<h3 style='color:red'>Red Text</h3>",
unsafe_allow_html=True)

st.caption("Caption for student management system.")

st.code("""
def add(a,b):
return a + b
""", language="python")

st.latex(r'''
a^2 + b^2 = c^2
''')

st.divider()
# button method to create a button
if st.button("click me"):
    st.write("button clicked!")
    st.success("operation successful!")
    st.snow()
else:
    st.write("button not clicked yet.")
    st.error("connection error!")
#text input method to get user input
name = st.text_input("enter your name:")
if name == "":
    st.warning("name cannot be empty!")
elif not name.isalpha():
    st.error("invalid input please enter only alphabets")
st.write(f"hello,{name}!")
#checkbox method to create a checkbox
if st.checkbox("i agree to terms and conditions"):
    st.write("thankyou for agreeing!")
    
#Radio button method to create radio buttons
gender = st.radio("Select you gender:",("Male","female","other"))
st.write(f"you selected, {gender}")


feedback = st.text_area("Enter feedback")
st.write(feedback)
#select method to create dropdown box
country = st.selectbox("select your country:",("india","dubai"))
st.write(f"you selected :(country)")
skills = st.multiselect(
    "select skills",
    ["python","sql","ml"]
)
st.write("skills:",skills)
#slider method to create slider
age = st.slider("select your age:",0, 100,25)
st.write(f"you are {age}years old.")
#file uploader method to upload files
uploaded_file = st.file_uploader("choose a file")
if uploaded_file is not None:
    st.success("file uploaded successfully!")
    st.write(f"filename:{uploaded_file.name}")
#form method to create a form
with st.form("my_form"):
    name = st.text_input("Name")
    age = st.number_input("Age", 0, 100)
    submit =st.form_submit_button("Submit")
if submit:
    st.write(name,age)

with st.form("login"):
    user = st.text_input("Username")
    pwd = st.text_input("Password",type="password")
    login =st.form_submit_button("login")
if login:
    st.success("login Successful")
    
#coloumns method to create cols
col1, col2, col3 =st.columns(3)
with col1:
    st.header("column 1")
    st.write("This is sridvika")
with col2:
    st.header("column 2")
    st.write("This is manasa")
with col3:
    st.header("column 3")
    st.write("This is suppu")
    
st.divider()
#container method to create container
container = st.container()
container.write("inside container")
container.button("click")
st.divider()
data = {
    'Name': ['Anurag', 'Sumit', 'Rohit'],
    'Age': [21, 22, 20],
    'Course': ['B.Tech', 'M.Tech', 'BBA']
}
st.table(data)

st.divider()
#sidebar method to create sidebar method
st.sidebar.title("Menu")
option = st.sidebar.selectbox(
"Choose page",
["Home", "About", "Contact"]
)
st.sidebar.write(f"You selected: {option}")

@st.cache_data
def load_data():
    return[1,2,3,4]
data =load_data()
st.write(data)
 



    


