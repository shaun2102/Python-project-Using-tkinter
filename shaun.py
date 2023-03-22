from tkinter import *
import tkinter
import csv
from tkinter import ttk

window = Tk()
window.title(".....REGISTRATION PAGE.....")
window.geometry("1500x900+0+0")
window.configure(bg = "white")

def dis1():
    root3 = Tk()
    root3.geometry("900x700+550+50")
    root3.title("Displaying record")

    f1=Frame(root3,bd=10,relief=GROOVE)
    f1.place(x=50,y=0,height=100,width=800)

    f2=Frame(root3,bd=10,relief=GROOVE)
    f2.place(x=50,y=150,height=500,width=800)



    la1=Label(f1,text="Registration details",font="lucida 30 bold")
    la1.pack(fill=BOTH)



    he1 = ttk.Treeview(f2, columns=("l1", "l2", "l3", "l4"))
    he1.heading("l1", text="Username")
    he1.heading("l2", text="email")
    he1.heading("l3", text="Contact")
    he1.heading("l4", text="password")
    he1["show"] = "headings"
    he1.pack(fill=BOTH, expand=1)

    scrollx = ttk.Scrollbar(f2, orient=HORIZONTAL, command=he1.xview)
    scrolly = ttk.Scrollbar(f2, orient=VERTICAL, command=he1.yview)
    scrollx.pack(side=BOTTOM, fill=X)
    scrolly.pack(side=RIGHT, fill=Y)
    he1.configure(xscrollcommand=scrollx.set, yscrollcommand=scrolly.set)

    with open("shaun_record.csv", "r") as f:
        reader=csv.reader(f)
        for i, row in enumerate(reader):
            if i == 0:
                continue  # skip header row
            he1.insert("", "end", text=i, values=row)


    root3.mainloop()
#creating label
window_label = Label(window, text = "REGISTRATION FORM", bg = "white", font = ("Algerian", 32))
window_label.pack()
username_label =Label(window, text = "USERNAME", fg = "black"
                               , bg = "white", font = ("arial", 20), )
username_label.place(x= 600, y = 150)
username_entry = Entry(window)
username_entry.place(x = 800, y = 155)

email_label =Label(window, text = "EMAIL", fg = "black"
                               , bg = "white", font = ("arial", 20))
email_label.place(x= 600, y = 230)
email_entry = Entry(window)
email_entry.place(x = 800, y = 230)

contact_label =Label(window, text = "CONTACT", fg = "black"
                               , bg = "white", font = ("arial", 20))
contact_label.place(x= 600, y = 305)
contact_entry = Entry(window)
contact_entry.place(x = 800, y = 305)

password_label =Label(window, text = "PASSWORD", fg = "black"
                               , bg = "white", font = ("arial", 20))
password_label.place(x= 600, y = 380)
password_entry = Entry(window)
password_entry.place(x = 800, y = 380)
#button
register_button =Button(window, text = "show record ", width=10,
                            bg='white',command=dis1, fg='black', font = ("bold", 20))
register_button.place(x = 700, y = 550)

def record():
        with open("shaun_record.csv", "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([username_entry.get(), email_entry.get(), contact_entry.get(), password_entry.get()])
submit_botton=Button(window,text="Submit",width=10,
                            bg='white',command=record, fg='black', font = ("bold", 20))
submit_botton.place(x = 700, y = 650)



window.mainloop()
