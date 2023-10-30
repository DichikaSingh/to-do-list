import tkinter as tk 
from tkinter import messagebox
di={}
dic={}
key=0
top= None
Enter_task= None

def ADD():
    global key
    Tasks= Enter_task.get()

    if Tasks:
        di[key]=Tasks
        Enter_task.delete(0, tk.END)
        
        
        for i in di.keys():
            if i==key:

                var=tk.BooleanVar()
                checkbutton=tk.Checkbutton(top,text=di[i],font="Timesroman",fg="#000000",variable=var,onvalue=True,offvalue=False,command=lambda i=i: update(i))
                checkbutton.pack()
                dic[i]=[checkbutton, var]
        key+=1    

def update(i):
    if (dic[i][1].get()==True):
        dic[i][0].config(font=('Times',22,'overstrike'),fg='green')
    else:
        dic[i][0].config(font=('Times',22,'normal'),fg='#000000')

def delete():

    le=[]
    for i in dic.keys():

        if(dic[i][1].get()==True):
            le.append(i)
    for i in le:
        dic[i][0].destroy()    
        del dic[i]
        del di[i]
    if le==[]:
        messagebox.showwarning("message", "Please select a task to delete") 


def createList():
    global top
    top= tk.Tk()
    top.title("To Do List")
    top.geometry("300x250") 
    lebal=tk.Label(text="You can always change your plan but only if you have one",font="Zapfino",bg="pink").pack()
    leabl2=tk.Label(text="To Do list", font="Arial").pack()
    global Enter_task
    Enter_task=tk.Entry(top, font=("Helvetica", 14), bg="sky blue")
    Enter_task.pack()
    Add_task=tk.Button(top,text="Add Task", bg="pink", font="Arial", fg="#000000", command=ADD).pack()
   
    
    Del_task=tk.Button(top,text="Delete Task", bg="pink", font="Arial", fg="#000000",command=delete).pack()
    top.mainloop()

