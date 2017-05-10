from Tkinter import *

root = Tk()

img = PhotoImage(file="skull.gif")
panel = Label(root, image=img)
panel.grid(row=0, column=0, columnspan=3, sticky=W + E + N + S)

panel2 = Label(root, image=img)
panel2.grid(row=0, column=4, columnspan=3, sticky=W + E + N + S)

var = StringVar()
panel3 = Label(root, textvariable=var).grid(row=2, column=0, columnspan=1)

var2 = StringVar()
panel4 = Label(root, textvariable=var2).grid(row=2, column=1, columnspan=1)

var3 = StringVar()
panel5 = Label(root, textvariable=var3).grid(row=2, column=2, columnspan=1)

Button(root, text="Quit", command=lambda: show_frame("StartPage")).grid(row=2, column=4, columnspan=1)
Button(root, text="Quit").grid(row=2, column=5, columnspan=1)

var.set("Score:0000(1)")
var2.set("Score:0000(2)")
var3.set("Score:0000(3)")


class PageOne(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        button = Button(self, text="Go to Main Menu",
                        command=lambda: controller.show_frame("StartPage"))

        button.pack()
        # creates the paned window
        m1 = PanedWindow(self)
        m1.pack(fill=BOTH, expand=1)

        left = Label(m1, text="Picture")
        m1.add(left)

        m2 = PanedWindow(m1, orient=VERTICAL)
        m1.add(m2)

        top = Label(m2, text="Answers")
        m2.add(top)

        bottom = Label(m2, text="Console")
        m2.add(bottom)

root.mainloop()
