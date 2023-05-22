from tkinter import *
import sqlite3
import ttkbootstrap as ttk
from ttkbootstrap.tableview import Tableview
from ttkbootstrap.constants import *

root = ttk.Window()
root.geometry("800x700")  # width and height
root.configure(bg="#1c1c1c")
colors = root.style.colors

# Connect to database and retrieve data
conn = sqlite3.connect('ppajo.db')
cursor = conn.cursor()
cursor.execute('SELECT * FROM tabel')
rows = cursor.fetchall()

# Define table columns
columns = [
    {"text": "id", "stretch": False},
    {"text": "eesnimi", "stretch": True},
    {"text": "perenimi", "stretch": True},
    {"text": "email", "stretch": True},
    {"text": "car_make", "stretch": True},
    {"text": "car_model", "stretch": True},
    {"text": "car_year", "stretch": True},
    {"text": "car_price", "stretch": True},
]

# Create tableview with retrieved data
tableview = Tableview(
    master=root,
    paginated=True,
    coldata=columns,
    rowdata=rows,
    searchable=True,
    bootstyle=SUCCESS,
    pagesize=10,
    height=10,
    stripecolor=(colors.light, None),
)

tableview.grid(row=0, column=0, padx=10, pady=5)
tableview.autofit_columns()

# Create a form to add new data
form_frame = ttk.Frame(root, padding=10, relief='raised', style='Primary.TFrame')
form_frame.grid(row=1, column=0, padx=10, pady=10)

# Define entry widgets for each field in the database table
fields = ['eesnimi', 'perenimi', 'email', 'car_make', 'car_model', 'car_year', 'car_price']
entries = {}
for i, field in enumerate(fields):
    label = ttk.Label(form_frame, text=field.capitalize() + ':', style='Primary.TLabel')
    label.grid(row=i, column=0, sticky='w', pady=5)
    entry = ttk.Entry(form_frame, width=40, style='Primary.TEntry')
    entry.grid(row=i, column=1, padx=5, pady=5)
    entries[field] = entry

# Define function to add data to database
def add_data():
    values = tuple(entry.get() for entry in entries.values())
    cursor.execute('INSERT INTO tabel VALUES (NULL,?,?,?,?,?,?,?)', values)
    conn.commit()
    tableview.delete_all()
    cursor.execute('SELECT * FROM tabel')
    rows = cursor.fetchall()
    tableview.insert_rows(rows)

# Create button to submit the form
submit_button = ttk.Button(form_frame, text='Add Data', command=add_data, style='Primary.TButton')
submit_button.grid(row=len(fields), column=1, pady=10)
#UURI KAS TÖÖTAB
def delete_data():
    # Get the entry widget (ID) and retrieve its value
    id_entry = entries['id']
    id_value = id_entry.get()

    # Delete the row from the database
    cursor.execute('DELETE FROM tabel WHERE id=?', (id_value,))
    conn.commit()

    # Refresh the tableview to show the updated data
    tableview.delete_all()
    cursor.execute('SELECT * FROM tabel')
    rows = cursor.fetchall()
    tableview.insert_rows(rows)

# Define entry widgets for each field in the database table
fields = ['id', 'eesnimi', 'perenimi', 'email', 'car_make', 'car_model', 'car_year', 'car_price']
entries = {}
for i, field in enumerate(fields):
    label = ttk.Label(form_frame, text=field.capitalize() + ':', style='Primary.TLabel')
    label.grid(row=i, column=0, sticky='w', pady=5)
    entry = ttk.Entry(form_frame, width=40, style='Primary.TEntry')
    entry.grid(row=i, column=1, padx=5, pady=5)
    entries[field] = entry

# Create button to submit the form
submit_button = ttk.Button(form_frame, text='Add Data', command=add_data, style='Primary.TButton')
submit_button.grid(row=len(fields), column=1, pady=10)

# Create a button to delete data by ID
delete_button = ttk.Button(form_frame, text='Delete by ID', command=delete_data, style='Primary.TButton')
delete_button.grid(row=len(fields)+1, column=1, pady=10)


root.mainloop()