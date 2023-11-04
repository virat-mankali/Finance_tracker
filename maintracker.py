import streamlit as st 
import accountfin, homefin, trackfin, budgetplannerfin

from streamlit_option_menu import option_menu
from datetime import datetime

st.set_page_config(page_title = 'Finance Tracker', layout = 'centered')

class MultiApp():
    
    def __init__(self):
        self.apps = []
    
    def add_app(self, title, funtion):
         self.apps.append({"title": title, "funtion": funtion})
         
    def run():

        with st.sidebar:
            app = option_menu(

                menu_title = 'Finance Tracker',
                options = ['Account', 'Home', 'Track Finance', 'Budget Planner'],
                menu_icon = '/Users/viratmankali/Desktop/Screenshot 2023-10-31 at 9.52.56 AM.png',
                default_index = 1

                )
            
        if app == 'Account':
            accountfin.accountfinpage_func()
        if app == 'Home':
            homefin.homefin_func()
        if app == 'Track Finance':
            trackfin.trackfin_func()
        if app == 'Budget Planner':
            budgetplannerfin.budget_planner_func()
        
       
    run()
