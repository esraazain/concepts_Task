import time
from tkinter import *
from tkinter import messagebox
 

root = Tk()
  
root.geometry("300x250")
root.configure(bg='black')
  

# title 
root.title("counntdown clock and Timer")
  
# Declaration of variables
hour=StringVar()
minute=StringVar()
second=StringVar()
  
# setting the default value as 0
hour.set("00")
minute.set("00")
second.set("00")
  
# class to take input from the user
hourEntry= Entry(root, width=3, font=("Arial",18,""),
                 textvariable=hour)
hourEntry.place(x=80,y=20)
  
minuteEntry= Entry(root, width=3, font=("Arial",18,""),
                   textvariable=minute)
minuteEntry.place(x=130,y=20)
  
secondEntry= Entry(root, width=3, font=("Arial",18,""),
                   textvariable=second)
secondEntry.place(x=180,y=20)
  
  
def countdown():
    try:
        # the input provided by the user is
        # stored in here :temp
        temp = int(hour.get())*3600 + int(minute.get())*60 + int(second.get())
    except:
        print("Please input the right value")
    while temp >-1:
        
 
         
        mins,secs = divmod(temp,60) 
  
        hours=0
        if mins >60:
             
            hours, mins = divmod(mins, 60)
      
        # two decimal places
        hour.set("{0:2d}".format(hours))
        minute.set("{0:2d}".format(mins))
        second.set("{0:2d}".format(secs))
  
      
        # update
        root.update()
        #sleep 1 
        time.sleep(1)
  
        # when temp = 0 then a message will show ->"Time Has Ended "
        
        if (temp == 0):
            messagebox.showinfo("Time Countdown", "Time Has Ended ")
         
        # after every one sec the value will be decremented
        # by one
        temp -= 1
        
 
# button 
btn = Button(root, text='Set a timer', bd='40',width='10',
                                command= countdown)
btn.place(x = 70,y = 120)
  

root.mainloop()
