import tkinter
from tkinter import *
from pymongo import MongoClient

client=MongoClient("mongodb://localhost:27017/")
db=client["Employees"]
collection=db["data"]
def getAllData(name):
    totaldata=collection.find_one({"Name":name})
    return totaldata

def Employee_details():
    data=box.get()
    alldata=getAllData(data)
    if alldata:
        result.config(text=f"Name:{alldata['Name']}\nAge:{alldata['age']}")
    else:
        result.config(text="Employee not found")

root=tkinter.Tk()
root.title("Employee")
root.geometry("500x500")

label=tkinter.Label(root,text="Enter your Name")
label.pack()
box=tkinter.Entry(root)
box.pack(pady=5)
button_submit=tkinter.Button(root,text="Submit",command=Employee_details)
button_submit.pack()

result=tkinter.Label(root,text="")
result.pack()
root.mainloop()

