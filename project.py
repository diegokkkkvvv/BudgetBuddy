import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load or create an expenses file
EXPENSES_FILE = "data/expenses.csv"

def load_expenses():
    """Loads the expense data from CSV file"""
    try:
        return pd.read_csv(EXPENSES_FILE)
    except FileNotFoundError:
        return pd.DataFrame(columns=["Date", "Category", "Amount"])

def save_expense(date, category, amount):
    """Saves an expense entry to the CSV file"""
    df = load_expenses()
    new_entry = pd.DataFrame([[date, category, amount]], columns=["Date", "Category", "Amount"])
    df = pd.concat([df, new_entry], ignore_index=True)
    df.to_csv(EXPENSES_FILE, index=False)

def show_expense_chart():
    """Displays a bar chart of expenses by category"""
    df = load_expenses()
    if df.empty:
        st.warning("No expenses to show.")
        return
    
    df["Amount"] = df["Amount"].astype(float)
    summary = df.groupby("Category")["Amount"].sum()

    fig, ax = plt.subplots()
    summary.plot(kind="bar", ax=ax)
    ax.set_ylabel("Total Spent ($)")
    st.pyplot(fig)

def main():
    """Main Streamlit App"""
    st.title("💰 BudgetBuddy - Expense Tracker")

    menu = ["Log Expense", "View Expenses", "Analytics"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Log Expense":
        st.subheader("Log a New Expense")
        date = st.date_input("Date")
        category = st.selectbox("Category", ["Food", "Transport", "Entertainment", "Bills", "Other"])
        amount = st.number_input("Amount", min_value=0.01, format="%.2f")
        if st.button("Save Expense"):
            save_expense(date, category, amount)
            st.success("Expense saved!")

    elif choice == "View Expenses":
        st.subheader("All Expenses")
        df = load_expenses()
        st.dataframe(df)

    elif choice == "Analytics":
        st.subheader("Expense Summary")
        show_expense_chart()

if __name__ == "__main__":
    main()
