import streamlit as st
from datetime import date


def trackfin_func():
    

    # Initialize expenses list in session state
    if 'expenses' not in st.session_state:
        st.session_state.expenses = []

    # Function to reset expenses at the beginning of each day
    def reset_expenses():
        today = date.today()
        return today

    # Streamlit app
    st.title("Expense :blue[Tracker]")

    # Check and update expenses at the beginning of a new day
    current_date = reset_expenses()
    st.write(f"Today's Date: {current_date}")

    daily_expenses_limit = st.number_input('Set your expenditure limit')
    daily_expenses_limit_button = st.button('Set limit')


    if st.button("Reset Expenses for Today"):
        current_date = reset_expenses()
        st.session_state.expenses = [expense for expense in st.session_state.expenses if expense["date"] == current_date]

    # Expense input
    expense = st.text_input("Expense:")
    amount = st.number_input("Amount:", value=0.0, min_value=0.0)

    if st.button("Add Expense"):
        if amount > 0:
            st.session_state.expenses.append({"date": current_date, "expense": expense, "amount": amount})

    # Display expenses for the current day
    st.write("Expenses for Today:")
    current_day_expenses = [expense for expense in st.session_state.expenses if expense["date"] == current_date]
    for expense in current_day_expenses:
        st.write(f"- {expense['expense']}: {expense['amount']:.2f} rupees")

    # Total expenses for the current day
    total_expense = sum(expense["amount"] for expense in current_day_expenses)
    st.write(f"Total Expenses for Today: {total_expense:.2f} rupees")

    # Show expense history
    st.subheader("Expense History:")
    st.write("Date, Expense, Amount")
    for expense in st.session_state.expenses:
        st.write(f"{expense['date']}, {expense['expense']}, {expense['amount']:.2f} rupees")

    if total_expense < daily_expenses_limit:
        st.success('Great!, your expenses are in limit!')
    
    if total_expense > daily_expenses_limit:
        st.warning("You've crossed your daily expenses limit. Please use money according to your needs")