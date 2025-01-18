from tkinter import*                # imports everything from tkinter module
tk = Tk()                           # creates a window
tk.title("calculator")              # title
tk.geometry('250x350')              # set the dimensions of the Tkinter window
tk['background'] = '#ced8e2'        # hex code for color   (html color codes)

# functions
def btnclick(number):                     
    textbox.insert(END, number)                         # inserts the number in the textbox     --> insert(index) – To insert a string at a specified index. 

def clearbtn():
    textbox.delete(0.0, END)                            # clears everything                 --> delete(startindex, endindex) – deletes characters within specified range.

def add():  
    first_number = textbox.get(0.0, END)                # saves the number in a variable    --> get(startindex, endindex) – to get characters within a given range. 
    global f_num
    f_num = float(first_number)                 
    textbox.delete(0.0, END)
    global op
    op = "+"

def subtract():
    first_number = textbox.get(0.0, END)         
    global f_num
    f_num = float(first_number)                    
    textbox.delete(0.0, END)
    global op                                                      
    op = "-"                        # saves the operator
    
def divide():
    first_number = textbox.get(0.0, END)
    global f_num
    f_num = float(first_number)
    textbox.delete(0.0, END)
    global op
    op = "/"

def multiply():
    first_number = textbox.get(0.0, END)
    global f_num
    f_num = float(first_number)
    textbox.delete(0.0, END)
    global op
    op = "*"

def equal():
    second_number = textbox.get(0.0, END)
    s_num = float(second_number)
    textbox.delete(0.0, END)
    if op == "+":
        textbox.insert(0.0, f_num + s_num)
    elif op == "-":
        textbox.insert(0.0, f_num - s_num)
    elif op == "/":
        textbox.insert(0.0, f_num / s_num)
    elif op == "*":
        textbox.insert(0.0, f_num * s_num)

# define numbers' buttons
btn7 = Button(tk, width=5, height=2, text="7", font=('Helvetica',10), command=lambda:btnclick(7))       # defines the button
btn7.place(x=25, y=100)                                                                                 # sets the button's position 

btn8 = Button(tk, width=5, height=2, text="8", font=('Helvetica',10), command=lambda:btnclick(8))
btn8.place(x=75, y=100)

btn9 = Button(tk, width=5, height=2, text="9", font=('Helvetica',10), command=lambda:btnclick(9))
btn9.place(x=125, y=100)

btn4 = Button(tk, width=5, height=2, text="4", font=('Helvetica',10), command=lambda:btnclick(4))
btn4.place(x=25, y=150)

btn5 = Button(tk, width=5, height=2, text="5", font=('Helvetica',10), command=lambda:btnclick(5))
btn5.place(x=75, y=150)

btn6 = Button(tk, width=5, height=2, text="6", font=('Helvetica',10), command=lambda:btnclick(6))
btn6.place(x=125, y=150)

btn1 = Button(tk, width=5, height=2, text="1", font=('Helvetica',10), command=lambda:btnclick(1))
btn1.place(x=25, y=200)

btn2 = Button(tk, width=5, height=2, text="2", font=('Helvetica',10), command=lambda:btnclick(2))
btn2.place(x=75, y=200)

btn3 = Button(tk, width=5, height=2, text="3", font=('Helvetica',10), command=lambda:btnclick(3))
btn3.place(x=125, y=200)

btn0 = Button(tk, width=5, height=2, text="0", font=('Helvetica',10), command=lambda:btnclick(0))
btn0.place(x=75, y=250)

btnclear = Button(tk, width=5, height=2, text="clear", font=('Helvetica',10), command=clearbtn)
btnclear.place(x=25, y=250)

# textbox
textbox = Text(tk, height = 1, width = 18, bg="#f4f7fa", font=(20))         # defines a textbox
textbox.place(x=26, y=45)                                                   # positions the textbox


# +*-/ buttons
btn11 = Button(tk, width=5, height=2, text="+", font=('Helvetica',10), command=add)
btn11.place(x=175, y=100)

btn12 = Button(tk, width=5, height=2, text="-", font=('Helvetica',10), command=subtract)
btn12.place(x=175, y=150)

btn13 = Button(tk, width=5, height=2, text="*", font=('Helvetica',10), command=multiply)
btn13.place(x=175, y=200)

btn14 = Button(tk, width=5, height=2, text="/", font=('Helvetica',10), command=divide)
btn14.place(x=175, y=250)

btn15 = Button(tk, width=5, height=2, text="=", font=('Helvetica',10), command=equal)
btn15.place(x=125, y=250)

# start the GUI
tk.mainloop()
