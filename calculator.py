from tkinter import *

# Create window
root = Tk()
root.title("Calculator")
root.geometry("320x420")
root.resizable(False, False)

# Entry widget
entry = Entry(root, width=18, font=("Arial", 22), bd=5, relief=RIDGE, justify=RIGHT)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Function to display button value
def click(value):
    entry.insert(END, value)

# Function to clear screen
def clear():
    entry.delete(0, END)

# Function to calculate result
def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, END)
        entry.insert(END, str(result))
    except:
        entry.delete(0, END)
        entry.insert(END, "Error")

# Button list
buttons = [
    ('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3),
    ('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3),
    ('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3),
    ('0',4,0), ('.',4,1), ('=',4,2), ('+',4,3),
]

# Create buttons
for (text,row,col) in buttons:
    if text == "=":
        Button(root,
               text=text,
               width=8,
               height=3,
               font=("Arial",12),
               command=calculate).grid(row=row,column=col)
    else:
        Button(root,
               text=text,
               width=8,
               height=3,
               font=("Arial",12),
               command=lambda t=text: click(t)).grid(row=row,column=col)

# Clear Button
Button(root,
       text="Clear",
       width=35,
       height=2,
       bg="red",
       fg="white",
       font=("Arial",12),
       command=clear).grid(row=5,column=0,columnspan=4,pady=10)

root.mainloop()