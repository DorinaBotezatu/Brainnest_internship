''' The goal of this project is to create a personal budgeting app that allows users to track their income and expenses, set budget goals, and view their spending habits.

Here are the steps you can take to create this project:

    Use the sqlite3 library to create a database to store the user's budget data.

    Use the tkinter library to create a GUI for the app, including widgets such as labels, buttons, text boxes and tables.

    Use the pandas library to manipulate the data and generate charts and tables to visualize the user's budget data.

    Use the datetime library to store and display the date and time of the transactions. '''

from tkinter import *
from tkinter import ttk
from datetime import datetime
import pandas as pd
import sqlite3




connection = sqlite3.connect('User_buget.db')
cursor = connection.cursor()
cursor.execute('''create table IF NOT EXISTS Income_expenses(
               [Datetime] DATETIME,
               [Transaction_type] TEXT,
                [Details] TEXT,
                 [Value_transaction] FLOAT, 
               [Category] TEXT,
                [GOAL] INT)''')

connection.commit()  # To commit the changes in the database, use a connection.commit() method.
connection.close()  # The last step is to close the connection using the connection.close() function.

root = Tk()
root.title("Welcome to your budget app! ")
root.geometry("500x200")

e_type = Entry(root, width=30)
e_type.grid(row=0, column=1, padx=20, pady=(10, 0))
e_details = Entry(root, width=30)
e_details.grid(row=1, column=1)
e_category = Entry(root, width=30)
e_category.grid(row=2, column=1)
e_sum = Entry(root, width=30)
e_sum.grid(row=3, column=1)

# Create Text Box Labels
l_type_label = Label(root, text="Type of budget income/expenses: ")
l_type_label.grid(row=0, column=0, pady=(10, 0))
l_details_label = Label(root, text="Details: ")
l_details_label.grid(row=1, column=0)
l_category_label = Label(root, text="Category: ")
l_category_label.grid(row=2, column=0)
l_sum_label = Label(root, text="Amount: ")
l_sum_label.grid(row=3, column=0)

now = datetime.now()
dt_string = now.strftime("%A %d/%m/%Y %H:%M")


def add():
    conn = sqlite3.connect('User_buget.db') # Create a database or connect to one
    c = conn.cursor()# Create cursor
    c.execute(
        "INSERT INTO Income_expenses VALUES (:Datetime, :Transaction_type, :Details, :Value_transaction, :Category, :GOAL)",
        {
            'Datetime': dt_string,
            'Transaction_type': e_type.get(),
            'Details': e_details.get(),
            'Value_transaction': e_sum.get(),
            'Category': e_category.get(),
            'GOAL': 2000,
        })


    conn.commit() # Commit Changes
    conn.close()# Close Connection

    # Clear The Text Boxes
    e_type.delete(0, END)
    e_details.delete(0, END)
    e_sum.delete(0, END)
    e_category.delete(0, END)


def query():
    conn = sqlite3.connect('User_buget.db') #  connect to database
    c = conn.cursor() # Create cursor
    c.execute("SELECT * FROM Income_expenses") # Query the database
    records = c.fetchall()
    conn.commit() # Commit Changes
    conn.close() # Close Connection
    return records


def view_details():
    top = Toplevel()
    top.title("Welcome to your details ")
    top.geometry("700x300")
    my_frame = Frame(top)
    my_frame.grid(row=1, column=1)

    style = ttk.Style()
    style.configure("Treeview", background='silver')
    style.map("Treeview",
              background=[('selected', 'orange')])
    table = ttk.Treeview(my_frame)
    table.grid(row=1, column=1)

    table['columns'] = ('Date', 'Type', 'Details', 'Category', 'Amount') # define our column

    # format our column
    table.column("#0", width=0, stretch=NO)
    table.column("Date", anchor=CENTER, width=200)
    table.column("Type", anchor=CENTER, width=60)
    table.column("Details", anchor=CENTER, width=200)
    table.column("Category", anchor=CENTER, width=60)
    table.column("Amount", anchor=W, width=80)

    # Create Headings
    table.heading("#0", text="", anchor=CENTER)
    table.heading("Date", text="Date", anchor=CENTER)
    table.heading("Type", text="Type", anchor=CENTER)
    table.heading("Details", text="Details", anchor=CENTER)
    table.heading("Category", text="Category", anchor=CENTER)
    table.heading("Amount", text="Amount", anchor=CENTER)


    records = query() # add data

    for record in records:
        table.insert(parent='', index='end', text='', values=(
            str(record[0]), str(record[1]), str(record[2]), str(record[3]), str(record[4]), str(record[5])))


button_save = Button(root, text="Add", command=add).grid(row=5, column=1)
button_second_window = Button(root, text="Open Second Window", command=view_details).grid(row=6, column=1)

root.mainloop()


def clear_Income_expenses_table():
    conn = sqlite3.connect("User_buget.db")
    c = conn.cursor()
    c.execute("delete from Income_expenses")
    conn.commit()
    conn.close()


def read_using_pandas():
    conn = sqlite3.connect("User_buget.db")
    df = pd.read_sql_query("SELECT * FROM Income_expenses", conn)
    print(df.head())
    conn.close()

read_using_pandas()

#clear_Income_expenses_table()
