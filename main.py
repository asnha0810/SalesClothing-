import streamlit as st
from streamlit_option_menu import option_menu

import home, CSandRS, account, dataset, Sales

def app():

        with st.sidebar:        
            app = option_menu(
                menu_title='Main Menu',
                options=['Home','Dataset','CSandRS','Sales','Account'],
                icons=['house-fill','bar-chart-fill', 'lightbulb','bar-chart-fill','person-circle'],
                menu_icon='cast',
                default_index=0,
                styles={
                    "container": {"padding": "5!important","background-color":'white'},
        "icon": {"color": "black", "font-size": "23px"}, 
        "nav-link": {"color":"black","text-align": "left", "margin":"0px", "--hover-color": "#f2f2f2"},
        "nav-link-selected": {"background-color": "lightgreen", "font-weight":"normal"},}
                
                )

        
        if app == "Home":
            home.app()
        if app == "CSandRS":
            CSandRS.app()
        if app == "Account":
            account.app()               
        if app == 'Dataset':
            dataset.app() 
        if app == 'Sales':
            Sales.app()

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
            
             
         
         
