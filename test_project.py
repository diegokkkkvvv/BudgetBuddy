import pytest
import pandas as pd
from project import load_expenses, save_expense

@pytest.fixture
def mock_expense_file(monkeypatch, tmp_path):
    """Mock CSV file for testing"""
    test_file = tmp_path / "test_expenses.csv"
    test_file.write_text("Date,Category,Amount\n2024-02-25,Food,10.5\n")
    monkeypatch.setattr("project.EXPENSES_FILE", str(test_file))
    return test_file

def test_load_expenses(mock_expense_file):
    """Test loading expenses"""
    df = load_expenses()
    assert not df.empty
    assert df.iloc[0]["Category"] == "Food"

def test_save_expense(mock_expense_file):
    """Test saving an expense"""
    save_expense("2024-02-26", "Transport", 20.0)
    df = load_expenses()
    assert "Transport" in df["Category"].values
