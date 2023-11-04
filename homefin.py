import streamlit as st 


def homefin_func():


    st.header('Welcome to Finance :blue[Tracker]')


    st.title("Welcome to Finance Tracker App")
    st.write("Track your expenses and stay within your budget!")


    st.header("Key Features:")
    st.markdown("- **Expense Tracking**: Easily track your daily expenses.")
    st.markdown("- **Set Daily Limit**: Set a daily expenditure limit to stay within your budget.")
    st.markdown("- **Get Warnings**: Receive warnings when you exceed your daily limit.")
    st.markdown("- **View History**: Check your expense history over time.")


    st.header("How to Use:")
    st.markdown("1. Set your **Daily Expenditure Limit**.")
    st.markdown("2. Add your **daily expenses** to keep track of your spending.")
    st.markdown("3. View your **daily expenses** and **total expenses**.")
    st.markdown("4. Get **warnings** if you exceed your daily limit.")


    st.header("About Finance Tracker App:")
    st.write("Our app is designed to help you manage your daily expenses effectively. "
            "Track your spending, set limits, and stay in control of your finances.")


    st.header("Contact & Support:")
    st.write("If you have any questions or need support, please contact us at support@financetrackerapp.com.")


    if st.button("Get Started"):
        st.success("Start tracking your expenses now!")


    st.sidebar.write("Terms of Service | Privacy Policy | Help Center")



