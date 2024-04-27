import tkinter as tk
from tkinter import ttk

app = tk.Tk()
app.configure(bg="skyblue")
app.geometry("300x300")
app.resizable(False,False)
app.title("Mobile")

# frame intput
frame = ttk.Frame(app)
# penempatan Grid,pack,place
frame.pack(padx=10,pady=10,fill="x",expand=True)

# komponen-komponen
# 1.label front name
label = ttk.Label(frame,text="Name")
label.pack(padx=5,fill="x",expand=True)
# 2. entry front name 
varEntry = tk.StringVar()
entry = ttk.Entry(frame,textvariable=varEntry)
entry.pack(padx=5,pady=10,fill="x",expand=True)

app.mainloop()