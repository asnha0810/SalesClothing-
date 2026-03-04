import streamlit as st
import json
import requests
import main


st.set_page_config(page_title='Customer analytics',
                   page_icon=":bar_chart:",
                   layout="centered")
class MultiApp:
    st.title("Group 7 website")

    def __init__(self):
        self.apps = []

    def run():
        if 'main' not in st.session_state:
            st.session_state.main = False
        if st.session_state.main ==True:
            main.app()
        elif st.session_state.main == False:
            
            page_bg_img = f"""
            <style>
            [data-testid="stAppViewContainer"] > .main {{
            background-image: url("https://i.postimg.cc/4xgNnkfX/Untitled-design.png");
            background-size: cover;
            background-position: center center;
            background-repeat: no-repeat;
            background-attachment: local;
            }}
            [data-testid="stHeader"] {{
            background: rgba(0,0,0,0);
            }}
            </style>
            """

            st.markdown(page_bg_img, unsafe_allow_html=True)

            if 'username' not in st.session_state:
                st.session_state.username = ''
            if 'useremail' not in st.session_state:
                st.session_state.useremail = ''


            def sign_up_with_email_and_password(email, password, username=None, return_secure_token=True):
                try:
                    rest_api_url = "https://identitytoolkit.googleapis.com/v1/accounts:signUp"
                    payload = {
                        "email": email,
                        "password": password,
                        "returnSecureToken": return_secure_token
                    }
                    if username:
                        payload["displayName"] = username 
                    payload = json.dumps(payload)
                    r = requests.post(rest_api_url, params={"key": "AIzaSyCtKdWIp_Q2Srz-YXZrNLi0yLzmqxpsDIs"}, data=payload)
                    try:
                        return r.json()['email']
                    except:
                        st.warning(r.json())
                except Exception as e:
                    st.warning(f'Signup failed: {e}')

            def sign_in_with_email_and_password(email=None, password=None, return_secure_token=True):
                rest_api_url = "https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword"

                try:
                    payload = {
                        "returnSecureToken": return_secure_token
                    }
                    if email:
                        payload["email"] = email
                    if password:
                        payload["password"] = password
                    payload = json.dumps(payload)
                    print('payload sigin',payload)
                    r = requests.post(rest_api_url, params={"key": "AIzaSyCtKdWIp_Q2Srz-YXZrNLi0yLzmqxpsDIs"}, data=payload)
                    try:
                        data = r.json()
                        user_info = {
                            'email': data['email'],
                            'username': data.get('displayName')
                        }
                        return user_info
                    except:
                        st.warning(data)
                except Exception as e:
                    st.warning(f'Signin failed: {e}')

            def reset_password(email):
                try:
                    rest_api_url = "https://identitytoolkit.googleapis.com/v1/accounts:sendOobCode"
                    payload = {
                        "email": email,
                        "requestType": "PASSWORD_RESET"
                    }
                    payload = json.dumps(payload)
                    r = requests.post(rest_api_url, params={"key": "AIzaSyCtKdWIp_Q2Srz-YXZrNLi0yLzmqxpsDIs"}, data=payload)
                    if r.status_code == 200:
                        return True, "Reset email Sent"
                    else:
                        error_message = r.json().get('error', {}).get('message')
                        return False, error_message
                except Exception as e:
                    return False, str(e)


            def f(): 
                try:
                    userinfo = sign_in_with_email_and_password(st.session_state.email_input,st.session_state.password_input)
                    st.session_state.username = userinfo['username']
                    st.session_state.useremail = userinfo['email']

                    
                    global Usernm
                    Usernm=(userinfo['username'])
                    st.session_state.signedout = True
                    st.session_state.main = True    
          
                    
                except: 
                    st.warning('Login Failed')

            def t():
                st.session_state.signedout = False
                st.session_state.main = False
                st.session_state.username = ''  
            def forget():
                email = st.text_input('Email')
                if st.button('Send Reset Link'):
                    print(email)
                    success, message = reset_password(email)
                    if success:
                        st.success("Password reset email sent successfully.")
                    else:
                        st.warning(f"Password reset failed: {message}") 

            if "signedout"  not in st.session_state:
                st.session_state["signedout"] = False                               
            
            if  not st.session_state["signedout"]:
                choice = st.selectbox('Login/Signup',['Login','Sign up'])
                email = st.text_input('Email Address')
                password = st.text_input('Password',type='password')
                st.session_state.email_input = email
                st.session_state.password_input = password

                

                
                if choice == 'Sign up':
                    username = st.text_input("Enter  your unique username")
                    
                    if st.button('Create my account'):
                        user = sign_up_with_email_and_password(email=email,password=password,username=username)
                        
                        st.success('Account created successfully!')
                        st.markdown('Please Login using your email and password')
                else:       
                    st.button('Login', on_click=f)
                    forget()               

                    
    run()



                