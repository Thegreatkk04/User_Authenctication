from sys import exception

import streamlit as st
from supabase import client , create_client
from dotenv import load_dotenv
import os
load_dotenv()
url=os.getenv("SUP_URL")
key=os.getenv("SUP_KEY")
supabase: client=create_client(url,key)

def sign_up(email,password):
    try:
        user=supabase.auth.sign_up({"email":email, "password":password})
        return user
    except Exception as e:
        st.error(f"registration failed {e}")

def sign_in(email,password):
    try:
        user=supabase.auth.sign_in_with_password({"email":email , "password":password})
        return user
    except Exception as e:
        st.error(f"login failed {e}")

def sign_out():
    try:

        supabase.auth.sign_out()
        st.session_state.user_email=None
        st.rerun()
    except Exception as e:
        st.error(f"logout failed {e}")


def main_app(user_mail):
    st.title("Welcome to the page")
    st.success(f"Welcome {user_mail}")
    if st.button("logout"):
        sign_out()

def auth_screen():
    st.title("Streamlit Authentication page")
    option=st.selectbox("Choose an action",["LogIn","SignUp"])
    email=st.text_input("Email")
    password=st.text_input("Password")

    if option=="SignUp" and st.button("Register"):
        user1=sign_up(email,password)
        if user1 and user1.user:
            st.success("Registration Successfull")
            
    if option=="LogIn" and st.button("login"):
        user1=sign_in(email,password)
        if user1 and user1.user:
            st.session_state.user_email=user1.user.email
            st.success("Welcome back !")
            st.rerun()
    
if "user_email" not in st.session_state:
    st.session_state.user_email=None
if st.session_state.user_email:
    main_app(st.session_state.user_email)
else:
    auth_screen()
