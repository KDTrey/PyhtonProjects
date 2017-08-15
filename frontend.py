"""
A program that stores book information:
Title, Author, Year, ISBN

User can:

View all records
Search and add an entry
Update an entry
Delete an entry
And close the program
"""
from tkinter import *
from backend import Database
database=Database("books.db")

class Window(object):


    def __init__(self,window):
        self.window=window
        self.window.wm_title("BookStore")

        l1=Label(window,text="Title")
        l1.grid(row=0,column=0)
        self.title_value=StringVar()
        self.e1=Entry(window,textvariable=self.title_value)
        self.e1.grid(row=0,column=1)

        l2=Label(window,text="Author")
        l2.grid(row=0,column=2)
        self.author_value=StringVar()
        self.e2=Entry(window,textvariable=self.author_value)
        self.e2.grid(row=0,column=3)

        l3=Label(window,text="Year")
        l3.grid(row=1,column=0)
        self.year_value=StringVar()
        self.e3=Entry(window,textvariable=self.year_value)
        self.e3.grid(row=1,column=1)

        l4=Label(window,text="ISBN")
        l4.grid(row=1,column=2)
        self.isbn_value=StringVar()
        self.e4=Entry(window,textvariable=self.isbn_value)
        self.e4.grid(row=1,column=3)

        self.list1=Listbox(window,height=5,width=30)
        self.list1.grid(row=2,column=0,rowspan=8,columnspan=2)
        scroll=Scrollbar(window)
        scroll.grid(row=2,column=2,rowspan=6)
        #Pairs the scrollbar with the list
        self.list1.configure(yscrollcommand=scroll.set)
        scroll.configure(command=self.list1.yview)

        self.list1.bind('<<ListboxSelect>>',self.selected)

        b1=Button(window,text='View All',width=11,command=self.view_command)
        b1.grid(row=2,column=3)

        b2=Button(window,text='Search Entry',width=11,command=self.search_command)
        b2.grid(row=3,column=3)

        b3=Button(window,text="Add Entry",width=11,command=self.add_command)
        b3.grid(row=4,column=3)

        b4=Button(window,text='Update selected',width=11,command=self.update_command)
        b4.grid(row=5,column=3)

        b5=Button(window,text='Delete selected',width=11,command=self.delete_command)
        b5.grid(row=6,column=3)

        b6=Button(window,text='Close',width=11,command=window.destroy)
        b6.grid(row=7,column=3)

    def selected(self,event):
        #index returns a tuple with just the index ex. (2,)
        index=self.list1.curselection()[0]
        self.selected=self.list1.get(index)#selected is now a tuple
        self.e1.delete(0,END)
        self.e1.insert(END,self.selected[1])
        self.e2.delete(0,END)
        self.e2.insert(END,self.selected[2])
        self.e3.delete(0,END)
        self.e3.insert(END,self.selected[3])
        self.e4.delete(0,END)
        self.e4.insert(END,self.selected[4])

    def view_command(self):
        #deletes from index 0 to last of the list
        self.list1.delete(0,END)
        for row in database.view():
            #END keyword adds new rows to the end of the listbox
            self.list1.insert(END,row)

    def search_command(self):
        self.list1.delete(0,END)
        for row in database.search(self.title_value.get(),self.author_value.get(),self.year_value.get(),self.isbn_value.get()):
            self.list1.insert(END,row)

    def add_command(self):
        database.insert(self.title_value.get(),self.author_value.get(),self.year_value.get(),self.isbn_value.get())
        self.list1.delete(0,END)
        self.list1.insert(END,(self.title_value.get(),self.author_value.get(),self.year_value.get(),self.isbn_value.get()))
    def update_command(self):
        database.update(self.selected[0],self.title_value.get(),self.author_value.get(),self.year_value.get(),self.isbn_value.get())
        self.view_command()

    def delete_command(self):
        database.delete(self.selected[0])
        self.view_command()

window=Tk()
Window(window)
window.mainloop()
