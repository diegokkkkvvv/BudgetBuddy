# BudgetBuddy

#### Video Demo: <https://youtu.be/yBbrnbUP5Gg>

#### Team Members: Isabela Meza and Amelia Jorge

#### Description:
BudgetBuddy is a personal expense-tracking application built using Python and Streamlit. It allows users to log daily expenses, categorize them, and visualize their spending habits over time. The project leverages CSV file storage for data persistence and provides a simple, user-friendly interface.

## File Structure and Contents:

```
BUDGETBUDDY
├── data
│   ├── expenses.csv       # CSV file storing logged expenses
├── project.py             # Main application logic
├── README.md              # Project documentation
├── requirements.txt       # Dependencies for running the project
├── test_project.py        # Unit tests for core functionality
```

## Features

- **Expense Logging:** Users can input expenses including date, category, and amount.
- **Data Storage:** All expense data is stored in a CSV file for persistence.
- **Visualization:** Generates visual insights into spending habits.
- **User-Friendly Interface:** Built using Streamlit for an interactive and accessible web experience.
- **Testing:** Ensures functionality with unit tests in `test_project.py`.

## Getting Started

### Prerequisites
Ensure you have Python installed (version 3.10 or later). You also need to install the required dependencies.

### Installation & Setup

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/BudgetBuddy.git
   cd BudgetBuddy
   ```

2. **Create a Virtual Environment (Optional but Recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   venv\Scripts\activate     # On Windows
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application:**
   ```bash
   streamlit run project.py
   ```

5. **Run Tests (Optional):**
   ```bash
   pytest test_project.py
   ```

## Design Decisions and Challenges

### Key Design Choices
- **CSV Storage:** A simple way to persist data without requiring a database.
- **Streamlit UI:** Provides an intuitive web-based interface for users.
- **Modular Code Structure:** Functions are modular and reusable, making future improvements easier.

### Challenges and Solutions
- **File Handling:** Ensuring the CSV file is correctly accessed and updated required exception handling.
- **User Input Validation:** Implemented checks to prevent incorrect entries.
- **Data Visualization:** Streamlit’s built-in charting features were leveraged for ease of implementation.

## Future Improvements
- **Database Integration:** Upgrade from CSV storage to SQLite or PostgreSQL.
- **Mobile Compatibility:** Optimize the UI for mobile devices.
- **Expense Categories & Budgeting:** Allow users to set spending limits for different categories.
- **Authentication:** Add user login functionality to save data for individual users.

## Conclusion
BudgetBuddy provides an easy and efficient way to track personal finances with minimal setup. With future improvements, it has the potential to become a fully-fledged budgeting tool.

### Developed by: Diego Knocehnhauer & Andre Ambrosi

*(CHATGPT was used as a helper tool to resolve certain design challenges and amplify aspects of this)*