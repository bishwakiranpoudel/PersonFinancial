import tkinter as tk
from tkinter import ttk
import speech_recognition as sr
import sqlite3

# Function to refresh the Treeview
def refresh_treeview():
    # Clear existing data
    tree.delete(*tree.get_children())

    # Retrieve data from the database
    c.execute("SELECT * FROM transactions")
    rows = c.fetchall()

    # Initialize total
    total_amount = 0

    # Insert data into Treeview and calculate total
    for row in rows:
        tree.insert("", "end", values=row)
        total_amount += row[1]  # Assuming amount is in the second column

    # Insert total row
    total_row = ("Total", total_amount, "")
    tree.insert("", "end", values=total_row)

    # Apply bold font tag to the total row
    tree.tag_configure("bold", font=("TkDefaultFont", 10, "bold"))
    tree.item(tree.get_children()[-1], tags=("bold",))

def validate_input(P):
    if P.isdigit():  # Allow only digits
        return True
    else:
        return False


def insert_text():
    type = typeentry.get()
    type = type.lower()
    amount = amountentry.get()
    topic = topicentry.get()
    topic = topic.lower()
    if type == "income" and amount.isdigit():
            c.execute("INSERT INTO transactions VALUES (?, ?, ?)", ('income', int(amount), topic))
            conn.commit()
            print(f"Income of {amount} recorded under topic: {topic}")
            refresh_treeview()
    elif type == "expense" and amount.isdigit():
            c.execute("INSERT INTO transactions VALUES (?, ?, ?)", ('expense', -int(amount), topic))
            conn.commit()
            print(f"Expense of {amount} recorded under topic: {topic}")
            refresh_treeview()
    else:
         print("Invalid Input")


def insert_voice():
    
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

        try:
        # Recognize speech using Google's speech recognition
            command = recognizer.recognize_google(audio)
            print("You said:", command)
        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))

    words = command.split() #split sentence to word 
    if len(words) == 3: #check if the length of sentence is 3 
        action, amount, topic = words
        if action == "income" and amount.isdigit():
            c.execute("INSERT INTO transactions VALUES (?, ?, ?)", ('income', int(amount), topic))
            conn.commit()
            print(f"Income of {amount} recorded under topic: {topic}")
            refresh_treeview()
        elif action == "expense" and amount.isdigit():
            c.execute("INSERT INTO transactions VALUES (?, ?, ?)", ('expense', -int(amount), topic))
            conn.commit()
            print(f"Expense of {amount} recorded under topic: {topic}")
            refresh_treeview()
        else:
            print("Invalid command format")
    else:
        print("Invalid command format")


# Create a connection to the SQLite database
conn = sqlite3.connect('finance.db')
c = conn.cursor()

# Create a table to store records
c.execute('''CREATE TABLE IF NOT EXISTS transactions
             (type TEXT, amount REAL, topic TEXT)''')
conn.commit()

# Initialize the recognizer
recognizer = sr.Recognizer()

# Creating Application Window
root = tk.Tk()
root.title("Finances")

# Set the size of the window
root.geometry("800x600") 

validate_func = root.register(validate_input)

typelabel = tk.Label(root, text="Type:")
typelabel.pack()
typeentry = tk.Entry(root)
typeentry.pack()

amountlabel = tk.Label(root, text="Amount:")
amountlabel.pack()
amountentry = tk.Entry(root, validate="key", validatecommand=(validate_func, "%P"))
amountentry.pack()

topiclabel = tk.Label(root, text="Topic")
topiclabel.pack()
topicentry = tk.Entry(root)
topicentry.pack()

submitButton = tk.Button(root, text="Submit", command=insert_text)
submitButton.pack()

voiceButton = tk.Button(root, text="Activate Voice", command=insert_voice)
voiceButton.pack()


# Display table with total of amount
# Create Treeview widget
tree = ttk.Treeview(root, columns=("Type", "Amount", "Topic"), show="headings")
tree.heading("Type", text="Type")
tree.heading("Amount", text="Amount")
tree.heading("Topic", text="Topic")
tree.pack()

# Retrieve data from the database
c.execute("SELECT * FROM transactions")
rows = c.fetchall()

# Initialize total
total_amount = 0

# Insert data into Treeview and calculate total
for row in rows:
    tree.insert("", "end", values=row)
    total_amount += row[1]  # Assuming amount is in the second column

# Insert total row
total_row = ("Total", total_amount, "")
tree.insert("", "end", values=total_row)

# Apply bold font tag to the total row
tree.tag_configure("bold", font=("TkDefaultFont", 10, "bold"))
tree.item(tree.get_children()[-1], tags=("bold",))

# Create a custom cell renderer for the border
tree.column("#0", stretch=tk.NO, width=2)  # Hide the first (icon) column

root.mainloop()