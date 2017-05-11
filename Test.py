import Tkinter as tk

LARGE_FONT = ("Verdana", 12)


class SeaofBTCapp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PageOne, PageTwo):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(PageOne)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        TITLE_FONT = ("Helvetica", 18, "bold")
        LARGE_FONT = ("Verdana", 12)

        label = tk.Label(text="This is the start page", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(text="Start Game", command=lambda: controller.show_frame(PageOne))

        button2 = tk.Button(text="Go to Scoreboard")

        button1.pack()
        button2.pack()



class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        img = tk.PhotoImage(file="skull.gif")

        panel = tk.Label(self, image=img)
        panel.image = img
        panel.grid(row=0, column=0, columnspan=3, sticky=tk.W + tk.E + tk.N + tk.S)

        panel2 = tk.Label(self, image=img)
        panel2.image = img
        panel2.grid(row=0, column=4, columnspan=3, sticky=tk.W + tk.E + tk.N + tk.S)

        var = tk.StringVar()
        panel3 = tk.Label(self, textvariable=var).grid(row=2, column=0, columnspan=1)

        var2 = tk.StringVar()
        panel4 = tk.Label(self, textvariable=var2).grid(row=2, column=1, columnspan=1)

        var3 = tk.StringVar()
        panel5 = tk.Label(self, textvariable=var3).grid(row=2, column=2, columnspan=1)

        tk.Button(self, text="Quit", command=lambda: controller.show_frame(PageOne)).grid(row=2, column=4, columnspan=1)
        tk.Button(self, text="Quit", command=lambda: controller.show_frame(PageTwo)).grid(row=2, column=5, columnspan=1)

        var.set("Score:0000(1)")
        var2.set("Score:0000(2)")
        var3.set("Score:0000(3)")


class PageTwo(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page Two!!!", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = tk.Button(self, text="Page One",
                            command=lambda: controller.show_frame(PageOne))
        button2.pack()


app = SeaofBTCapp()
app.mainloop()