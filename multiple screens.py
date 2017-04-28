from Tkinter import *   


TITLE_FONT = ("Helvetica", 18, "bold")
## * args is a list of arguments -as positional arguments
## ** kwargs = dictionary - whose keys become separate keyword arguments and the values become values of these arguments. 

class SampleApp(Tk):

    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, PageOne, PageTwo):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        label = Label(self, text="This is the start page", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=10)

        button1 = Button(self, text="Start Game",
                            command=lambda: controller.show_frame("PageOne"))
        button2 = Button(self, text="Go to Scoreboard",
                            command=lambda: controller.show_frame("PageTwo"))
        button1.pack()
        button2.pack()

#when button one is pressed
class PageOne(Frame):
            
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        label = Label(self, text="This is The game", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=10)
        button = Button(self, text="Go to Scoreboard",
                           command=lambda: controller.show_frame("PageTwo"))
        button.pack()
        
            
#when button two is pressed
class PageTwo(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        label = Label(self, text="Score Board", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=10)
        button = Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()
        button = Button(self, text="Go to Game",
                           command=lambda: controller.show_frame("PageOne"))
        button.pack()
       


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()

