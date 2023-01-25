import streamlit as st

from dbconnect import DBConnection
import sqlite3
conn=sqlite3.connect('data.db')
c=conn.cursor()

class DBConnection:
    def create_usertable(self):
        c.execute('CREATE TABLE IF NOT EXISTS userstable(username TEXT, password TEXT) ')


    def add_userdata(self, username, password):
        c.execute('INSERT INTO userstable (username, password) VALUES (?, ?)', (username, password))
        conn.commit()


    def login_user(self, username, password):
        #valid data build:
        c.execute("SELECT * FROM userstable WHERE username=? AND password =?",(username, password))

        #vulnarable for injection
        c.execute(f"SELECT * FROM userstable WHERE username='{username}' AND password ='{password}'")
        #sql injection happens 'SELECT * FROM userstable WHERE username=junk'-- AND password=junkvalue'
        # password ='{password}'"
        data = c.fetchall()
        print (data)
        return (data)



    def view_all_users(self):
        c.execute('SELECT * FROM userstable')
        data = c.fetchall()
        return (data)

"""Simple Login App"""
st.title("Simple Login App")
menu = ["Home", "Login", "SignUp"]
choice = st.sidebar.selectbox("Menu", menu)
if choice == "Home":
    st.subheader("Home")
elif choice == "Login":
    st.subheader("Login Section")


db=DBConnection()

username = st.sidebar.text_input("User Name")
password = st.sidebar.text_input("Password")
print(f"data entered is {username},{password}")
data=db.login_user(username,password)
authenticated_users=db.view_all_users()
print ("this is the data", data)
if st.sidebar.checkbox("Login"):
    if (data):
        st.success (f"authenticated user, {username}")
        st.subheader(f"user is one of the authenticated user from Database users {authenticated_users}")

    else:
        st.fail(f"unauthenticated user, {username}")


