import streamlit as st 
import firebase_admin

from firebase_admin import credentials
from firebase_admin import auth
from datetime import datetime

cred = credentials.Certificate('hackathon/finance-tracker-9b7a5-f7442fcd31ec.json')
firebase_admin.initialize_app(cred)

def accountfinpage_func():

    st.header('Track :blue[Finance]')

    login_signup = st.selectbox('Login/Signup',['Select login/signup', 'Login', 'Signup'], index = 0)

    def login_check():
        try:
            user = auth.get_user_by_email(email_login)
            #print(user.uid)
            st.success('Login successful')

        except:
            st.warning('Login failed')

    if login_signup == 'Select login/signup':
        st.warning('Please select login/signup to continue')

    elif login_signup == 'Login':
        email_login = st.text_input('Enter your email', placeholder = 'username..')
        password = st.text_input('Enter your password', type = 'password')

        login_button = st.button('Login', on_click = login_check )



    else:
        name = st.text_input('Enter your name', placeholder = 'name here..')
        email = st.text_input('Enter your email', placeholder = 'email here..')
        dob = st.date_input('Enter your date of birth', min_value = datetime(1900,1,1))
        username_signup = st.text_input('Enter your username', placeholder = 'username here..')
        password_signup = st.text_input('Enter your password', placeholder = 'password here..', 
                                        type = 'password', max_chars = 18)
        
        if st.button('Create my account'):
            user = auth.create_user(email = email, password = password_signup, uid = username_signup)
                                    
            
            st.success('Account created succesfully!')
            st.markdown('Please login using your email and password')
            st.balloons()