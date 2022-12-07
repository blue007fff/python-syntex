from tkinter import*

def Call():
    msg = Label(window, text = "pressed")
    msg.place(x = 30, y = 50)
    button["bg"] = "blue"
    button["fg"] = "white"

def mypython_syntex_tkinter():
    window = Tk()
    window.geometry("300x150")
    button = Button(text = "press me", command = Call)
    button.place(x = 30, y = 20, width = 120, height = 30)
    logo = PhotoImage(file="동구리.gif")
    logoimage = Label(image = logo)
    logoimage.place(x = 150, y = 20, width=400, height=300)
    logoimage["bg"] = "blue"
    window.mainloop()


import turtle
def mypython_syntex_turtle():
    turtle.shape("turtle")
    for i in range(0, 5):
        turtle.forward(100)
        turtle.right(72)
    turtle.exitonclick()


mypython_syntex_tkinter()
#mypython_syntex_turtle()