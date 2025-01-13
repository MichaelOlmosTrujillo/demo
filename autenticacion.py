import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader
import streamlit as st

# url documentación: 
# https://pypi.org/project/streamlit-authenticator/#5-creating-a-login-widget

# # Usando el modelo Hasher para convertir el texto completo de contraseñas
# # en hashed contraseñas.

with open('./config.yaml') as file:
    config = yaml.load(file, Loader = SafeLoader)

# # hashed_passwords = stauth.Hasher(['redlac']).generate()

# st.write(config['credentials'])

authenticator = stauth.Authenticate(
    credentials = config['credentials'],
    cookie_name = config['cookie']['name'],
    cookie_key = config['cookie']['key'],
    cookie_expiry_days = config['cookie']['expiry_days'])
# 
# st.write(help(authenticator))
authenticator.login()
# st.write(authenticator)
# st.write("st.session_state['name']: ", st.session_state['name'])
# st.write(st.session_state['authentication_status'])
# st.session_state['failed_login_attempts'] = 0
# st.write(st.session_state['failed_login_attempts'])
if st.session_state['authentication_status']:
    authenticator.logout()
    st.write(f'Welcome *{st.session_state["name"]}*')
    st.title('Some content')
elif st.session_state['authentication_status'] is False:
    st.write(authenticator)
    st.error('Username/password is incorrect')
elif st.session_state['authentication_status'] is None:
    st.warning('Please enter your username and password')

# name, authentication_status, username = authenticator.login('Login', 'main')


# import streamlit as st
# import streamlit_authenticator as stauth

# # Hash the passwords
# passwords = ['password1', 'password2']
# # Hash each password individually
# hashed_passwords = [stauth.Hasher(passwords).hash() for password in passwords]
# # hashed_passwords = ['passowrd1', 'passowrd2']
# credentials = {
#     "usernames": {
#         "user1": {
#             "name": "John Doe",
#             "password": hashed_passwords[0]
#         },
#         "user2": {
#             "name": "Jane Smith",
#             "password": hashed_passwords[1]
#         }
#     }
# }

# # Create authenticator
# authenticator = stauth.Authenticate(
#     credentials,
#     "my_app_cookie_name",
#     "my_app_signature_key",
#     cookie_expiry_days=30
# )

# # Login
# name, authentication_status, username = authenticator.login('Login', 'main')

# if authentication_status:
#     st.success(f"Welcome {name}!")
#     if st.button("Logout"):
#         authenticator.logout("Logout", "main")
#         st.success("You have successfully logged out!")
# elif authentication_status == False:
#     st.error("Username/password is incorrect")
# elif authentication_status == None:
#     st.warning("Please enter your username and password")
