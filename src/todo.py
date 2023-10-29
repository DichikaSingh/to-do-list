import tkinter as tk 
from PIL import ImageTk, Image
di={}
dic={}
key=0
def ADD():
    
    Tasks= Enter_task.get()

    if Tasks:
        di[key]=Tasks
        Enter_task.delete(0, tk.END)
        
        for i in di.keys():
            if i==key:
               var=tk.BooleanVar()
            checkbutton=tk.Checkbutton(top,text=di[i],
                                       font="Timesroman",
                                       bg="pink",
                                       variable=var,
                                       onvalue="true", 
                                       offvalue="false",
                                       command=lambda i=i: update(i))

            checkbutton.pack()
            dic[i]=[checkbutton, var]

def update(i):
    print(i)
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
                tk.messagebox.showwarning("message", "Please select a task to delete") 


def createList():
    top= tk.Tk()
    top.title("To Do List")
    top.geometry("300x250") 
    lebal=tk.Label(text="You can always change your plan but only if you have one",font="Zapfino",bg="pink").pack()
    leabl2=tk.Label(text="To Do list", font="Arial").pack()
    Enter_task=tk.Entry(top, font="Helvetica", bg="sky blue")
    Enter_task.pack()
    Add_task=tk.Button(top,text="Add Task", bg="pink", font="Arial", fg="#000000", command=ADD).pack()
    can= tk.Canvas(top,width=900,height=1550)
    can.pack()
    Bg_Image= ImageTk.PhotoImage(Image.open(r"C:\Users\shilp\OneDrive\Desktop\Doli\tkinter bg.jpg"))
    can.create_image(0,0, image= Bg_Image,anchor= tk.S)
    Del_task=tk.Button(top,text="Delete Task", bg="pink", font="Arial", fg="#000000").pack()
    top.mainloop()

