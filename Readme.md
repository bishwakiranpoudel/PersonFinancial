# Personal Finance Manager with Speech Recognition

This Python application helps you manage your finances by allowing you to record income and expenses, both through manual input and voice commands using speech recognition. The recorded transactions are stored in a SQLite database and displayed in a graphical interface using the tkinter library.

## Features

1. **Manual Input:**
   You can manually input transactions by providing the type (income or expense), amount, and topic (description).

2. **Voice Recognition:**
   The application supports voice commands for entering transactions. Activate the voice command feature and speak your command, which should consist of three words: the action (income/expense), the amount, and the topic.

3. **SQLite Database:**
   All transactions are stored in an SQLite database named `finance.db`. The database contains a table named `transactions` with columns: `type`, `amount`, and `topic`.

4. **Graphical Interface:**
   The transactions are displayed in a table using the `ttk.Treeview` widget from tkinter. The table shows the type, amount, and topic of each transaction. A total row is displayed at the end, showing the sum of all recorded amounts.

## Prerequisites

- Python 3.x
- Required packages: `tkinter`, `speech_recognition`, and `sqlite3`. You can install them using:
```
pip install tkinter speech_recognition
```

## How to Run

1. Clone this repository to your local machine.
2. Navigate to the repository's directory.
3. Run the following command to start the application:
```
python personalFinanceManager.py
```

## Usage

- **Manual Input:**
1. Enter the transaction details (type, amount, and topic) in the provided input fields.
2. Click the "Submit" button to record the transaction.

- **Voice Recognition:**
1. Click the "Activate Voice" button.
2. Speak the command with the format: "[income/expense] [amount] [topic]".

- **Viewing Transactions:**
- All recorded transactions are displayed in the table.
- The total amount of all transactions is shown in the last row.


