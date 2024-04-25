import tkinter as tk
import random
window = tk.Tk()
window.geometry("700x700")
window.configure(bg="#103890")
label_title = tk.Label(window,text="NAMES:",font=('Arial',20,"bold"),bg="red")
label_title.pack()
names = ["jabir", "ilyas", "ashik", "parvesh", "thowfeeq"]
frame = tk.Frame(window,bg="light blue",width=200,height=200)
frame.pack()
for i in names:
    label = tk.Label(frame,text=i,font=(10),bg="light blue")
    label.pack()

def shuffle_name():
    name = random.choice(names)
    label_shuffle = tk.Label(window,text=name,bg="#103890",font=("bold",18))
    label_shuffle.pack()
    names.remove(name)

btn = tk.Button(window,text="SHUFFLE",command=shuffle_name)
btn.pack()

window.mainloop()
