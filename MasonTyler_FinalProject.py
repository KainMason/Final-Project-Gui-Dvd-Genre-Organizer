# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 13:09:27 2021

@author: 18122
"""
import tkinter as tk
drama=[] # dictionaries for each genre
fantasy=[]
action=[]
comedy=[]
animation=[]
horror=[]
# end of genre dictionaries

####### FUNCTIONS ###############


def popup():   ###### error pop up window when user doesnt enter all info 
    
    
        my_w=tk.Toplevel(gui) # pop up
        my_w.geometry("250x50") 
        my_w.title("pop up ")

        l1 = tk.Label(my_w,  text='Entry Incomplete ' ) 
        l1.grid(row=1,column=1) 

      
        b3 = tk.Button(my_w, text='Okay',
                        command=my_w.destroy)
        b3.grid(row=2,column=1)
everything =[]

# end of pop up window

def viewWindowDrama():    ######### Window for Drama List
    window1 = tk.Toplevel(gui)
    window1.title("DRAMA")
    window1.geometry("500x300")
    window1.configure(background="black")
  
    
    title= tk.Label(window1,text="DRAMA")
    title.pack()
    tbbDelete = tk.Button(window1,text="DELETE",background="black",fg="red")
    tbbDelete.bind("<Button-1>", lambda event: DeleteItem(event))
    tbbDelete.pack()
    closeBttn = tk.Button(window1,text="CLOSE",command=lambda:close())   ##### button to close window
    closeBttn.pack(pady=10,padx=10)
    lstbox1= tk.Listbox(window1) ### list box to hold catagory text 
    lstbox1.pack(fill="both",expand=1,padx=50,pady=50)

    for item in drama:
         lstbox1.insert(tk.END, item)
    def DeleteItem(event):       ############### Deleted user selected item from the list 
        selected = lstbox1.curselection() #holds the highlight item for deletion
        drama.pop(selected[0])
              
        lstbox1.delete(0, tk.END)
        for item in drama:
            lstbox1.insert(tk.END, item)
    def close():     # close window function
       window1.destroy()
    
def viewWindowComedy():
    window2 = tk.Toplevel(gui)# category window
    window2.title("COMEDY")
    window2.geometry("500x300")
    window2.configure(background="black")
    title= tk.Label(window2,text="COMEDY",background="black",fg="red")
    title.pack()
    buttDelete2 = tk.Button(window2,text="Delete",command=lambda:DeleteItem(None))
    buttDelete2.pack()
    closeBttn = tk.Button(window2,text="CLOSE",command=lambda:close())
    closeBttn.pack(pady=10,padx=10)
    lstbox2 = tk.Listbox(window2)### list box to hold catagory text 
    lstbox2.pack(fill="both",expand=1,padx=50,pady=50)

    for item in comedy:
         lstbox2.insert(tk.END, item)
    def DeleteItem(event):############### Deleted user selected item from the list 
        selected = lstbox2.curselection()#holds the highlight item for deletion
        comedy.pop(selected[0])
            
        lstbox2.delete(0, tk.END)
        for item in comedy:
            lstbox2.insert(tk.END, item)
    def close(): ###### CLOSE window
        window2.destroy()              

def viewWindowAction(): # category window
    window3 = tk.Toplevel(gui)
    window3.title("ACTION")
    window3.geometry("500x300")
    window3.configure(background="black")
    title= tk.Label(window3,text="ACTION",background="black",fg="red")
    title.pack()
    buttDelete3 = tk.Button(window3,text="Delete",command=lambda:DeleteItem(None))
    buttDelete3.pack()
    closeBttn = tk.Button(window3,text="CLOSE",command=lambda:close())
    closeBttn.pack(pady=10,padx=10)
    lstbox3 = tk.Listbox(window3)### list box to hold catagory text 
    lstbox3.pack(fill="both",expand=1,padx=50,pady=50)

    for item in action:
         lstbox3.insert(tk.END, item)
    def DeleteItem(event):############### Deleted user selected item from the list 
        selected = lstbox3.curselection()
        action.pop(selected[0])
              
        lstbox3.delete(0, tk.END)
        for item in action:
            lstbox3.insert(tk.END, item)
    def close(): # close window function
        window3.destroy()
         
def viewWindowAnimation():# category window
    window4 = tk.Toplevel(gui)
    window4.title("ANIMATION")
    window4.geometry("500x300")
    window4.configure(background="black")
    title= tk.Label(window4,text="ANIMATION",background="black",fg="red")
    title.pack()
    buttDelete4 = tk.Button(window4,text="Delete",command=lambda:DeleteItem(None))
    buttDelete4.pack() 
    closeBttn = tk.Button(window4,text="CLOSE",command=lambda:close())
    closeBttn.pack(pady=10,padx=10)
    lstbox4 = tk.Listbox(window4)### list box to hold catagory text 
    lstbox4.pack(fill="both",expand=1,padx=50,pady=50)

    for item in animation:
         lstbox4.insert(tk.END, item)
    def DeleteItem(event):############### Deleted user selected item from the list 
        selected = lstbox4.curselection()
        animation.pop(selected[0])
             
        lstbox4.delete(0, tk.END)
        for item in animation:
            lstbox4.insert(tk.END, item)
    def close(): # close window function
        window4.destroy()
def viewWindowHorry():# category window
    window5 = tk.Toplevel(gui)
    window5.title("HORRO")
    window5.geometry("500x300")
    window5.configure(background="black")
    title= tk.Label(window5,text="HORROR",background="black",fg="red")
    title.pack()
    buttDelete5 = tk.Button(window5,text="Delete",command=lambda:DeleteItem(None))
    buttDelete5.pack()
    closeBttn = tk.Button(window5,text="CLOSE",command=lambda:close())
    closeBttn.pack(pady=10,padx=10)
    lstbox5 = tk.Listbox(window5)### list box to hold catagory text 
    lstbox5.pack(fill="both",expand=1,padx=50,pady=50)

    for item in horror:
         lstbox5.insert(tk.END, item)
         
    def DeleteItem(event):############### Deleted user selected item from the list 
         selected = lstbox5.curselection()
         horror.pop(selected[0])
         
         lstbox5.delete(0, tk.END)
         for item in horror:
             lstbox5.insert(tk.END, item)
    def close(): # close window function
        window5.destroy()

def viewWindowFantasy():# category window
    window6 = tk.Toplevel(gui)
    window6.title("FANTASY")
    window6.geometry("500x300")
    window6.configure(background="black")
    title= tk.Label(window6,text="FANTASY",background="black",fg="red")
    title.pack()
    buttDelete6 = tk.Button(window6,text="Delete",command=lambda:DeleteItem(None))
    buttDelete6.pack()
    closeBttn = tk.Button(window6,text="CLOSE",command=lambda:close()) ### button to close window
    closeBttn.pack(pady=10,padx=10)
    lstbox6 = tk.Listbox(window6)### list box to hold catagory text 
    lstbox6.pack(fill="both",expand=1,padx=50,pady=50)
    
    for item in fantasy:
         lstbox6.insert(tk.END, item)
         
    def DeleteItem(event):############### Deleted user selected item from the list 
        selected = lstbox6.curselection()
        fantasy.pop(selected[0])
        
        lstbox6.delete(0, tk.END)
        for item in fantasy:
            lstbox6.insert(tk.END, item)
    def close(): # close window function
        window6.destroy()

def ViewWindowButtons():   ###### Alt window listing buttons for each genre 
    window7 = tk.Toplevel(gui)
    window7.title("GENRE SELECTION")
    window7.geometry("160x120")
    window7.configure(background="black")
  
    
    actionbttn = tk.Button(window7,text="ACTION",command=lambda:viewWindowAction())  #### Button to open another window
    actionbttn.grid(row=0,column=0)
    
    dramabttn = tk.Button(window7,text="DRAMA",command=lambda:viewWindowDrama())#### Button to open another window
    dramabttn.grid(row=0,column=1)
    
    combttn = tk.Button(window7,text="COMEDY",command=lambda:viewWindowComedy())#### Button to open another window
    combttn.grid(row=1,column=0)
    
    fanbttn = tk.Button(window7,text="FANTASY",command=lambda:viewWindowFantasy())#### Button to open another window
    fanbttn.grid(row=1,column=1)
    
    horbttn = tk.Button(window7,text="HORROR",command=lambda:viewWindowHorry())#### Button to open another window
    horbttn.grid(row=2,column=0)
    
    animbttn = tk.Button(window7,text="ANIMATION",command=lambda:viewWindowAnimation())#### Button to open another window
    
    animbttn.grid(row=2,column=1)
    closeBttn = tk.Button(window7,text="CLOSE",command=lambda:close())#### Button to close
    closeBttn.grid(row=3,column=0,columnspan=2,pady=10,padx=10)

    def close():##### Close function for Button Selection Window
        window7.destroy()
        


def AddPerson(event):   ######## Main function thats adds all user input into each 
                         ######## into each seperate list 
   name = entMovie.get()
   genre = omChoose.get()
   if name == "" or genre == "":
       popup()
   elif genre == "Drama":
       drama.append([name,genre])
   elif genre == "Action":
       action.append([name,genre])
   elif genre == "Animation":
        animation.append([name,genre])
   elif genre == "Comedy":
       comedy.append([name,genre])
   elif genre == "Horror":
       horror.append([name,genre])
   elif genre == "Fantasy":
       fantasy.append([name,genre])
   else:
       pass
   entMovie.delete(0,tk.END)
   omChoose.set("")
  
    
  
   ############ Main Gui #######################3 
  
    
  
gui = tk.Tk()
gui.geometry("300x200")
gui.title("DVD GENRE ORGANIZER")
gui.configure(background="black")








listgenre = ["Drama","Fantasy","Action","Comedy","Animation","Horror"]  ##### dictionary of genre list for main option menu 

titlelable = tk.Label(gui,text="DVD Genre Organizer",font="bold",fg="red",background="black")
titlelable.grid(row=0,columnspan=3,column=0)

titlelable = tk.Label(gui,text="DVD TITLE: ",font="bold",fg="red",background="black")
titlelable.grid(row=1,columnspan=1,column=0)

titlelable = tk.Label(gui,text="DVD Genre : ",font="bold",fg="red",background="black")
titlelable.grid(row=2,columnspan=1,column=0)

entMovie = tk.Entry(gui)     ###### Entrt box of DVD user input
entMovie.grid(row=1,column=1)

omChoose = tk.StringVar("")
omGenre = tk.OptionMenu(gui,omChoose,*listgenre)   ###### Option menu for the user to select Genre
omGenre.grid(row=2,column=1)
                                        



####### Button to add movie to indival lists 
bttEnter = tk.Button(gui, text= "ENTER",font="bold",fg="red",background="black",command=lambda: AddPerson(None))
bttEnter.configure(width=27)
bttEnter.grid(row=3,column=0,columnspan=2,padx=10,pady=10)

##### Button to open Genre Button Window 
bttEnter = tk.Button(gui, text= "View By Genre",command=lambda: ViewWindowButtons(),font="bold",fg="black",background="red")
bttEnter.configure(width=27)
bttEnter.grid(row=4,column=0,columnspan=2,padx=10,pady=10)

closeall = tk.Button(gui, text="CLOSE ALL",command= lambda: closeAll(None))
closeall.grid(row=5,column=0,columnspan=2)
def closeAll(event):
    gui.destroy()
gui.mainloop() #end of gui