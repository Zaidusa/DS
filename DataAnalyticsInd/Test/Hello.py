import streamlit as st
import streamlit_authenticator as stauth

st.title('Threat Modeling_Assignment')
names=["zaid","zaid1","zaid2"]
usernames=["zaid","zaid1","zaid2"]
passwords=["zaid","zaid1","zaid2"]

#authenticator=stauth.Authenticate(names,usernames,passwords,"Threat Modeling_Assignment")

name,authentication_status, username=authenticator.login("login","main")
if authentication_status==False:
    st.error("log in falied")
if authentication_status== None:
    st.warning("enter login details")
if authentication_status== True:

    # give a title to our app
    st.title('Threat Modeling_Assignment')

    st.text(" we are applying hreat Modeling_Assignment for a mobile Application")

    authenticator.logout("Logout","sidebar")
    st.sidebar(f"welcome {name}")