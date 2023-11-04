import streamlit as st


def budget_planner_func():
    
    # Initialize session state to store the budget data
    if 'budget' not in st.session_state:
        st.session_state.budget = {}

    # Title and description
    st.title("Budget Planner")
    st.write("Enter your budget for different categories below.")

    # Create input fields for budget categories and their allocated amounts
    category = st.text_input("Category:", "")
    amount = st.number_input("Allocated Amount:", 0.0)

    if st.button("Add Category"):
        if category and amount > 0:
            st.session_state.budget[category] = amount
            st.success(f"Category '{category}' added with an allocated amount of ${amount:.2f}")
        else:
            st.error("Please enter a valid category and allocated amount.")

    # Display the budget summary
    st.header("Budget Summary")

    # Calculate and display the total budget
    total_budget = sum(st.session_state.budget.values())
    st.write(f"Total Budget: ${total_budget:.2f}")

    for category, amount in st.session_state.budget.items():
        st.write(f"{category}: ${amount:.2f}")

    # Calculate and display the remaining budget
    remaining_budget = total_budget - sum(st.session_state.budget.values())
    st.write(f"Remaining Budget: ${remaining_budget:.2f}")

    # Save the budget data in JSON format
    st.text(st.session_state.budget)