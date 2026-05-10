from tkinter import *
from tkinter import ttk

root = Tk()

class AutoExpensesSplitterFrame(Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)


        testLabel = Label(self, text='test 1') #testing purpose
        testLabel.pack(padx=10)
        self.controller = controller
        Button(self, text='Back to Main', command=lambda: self.controller.frameChange(0)).pack()

class ExpensesTrackerFrame(Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        testLabel = Label(self, text='test 2') #testing purpose
        testLabel.pack(padx=10)
        self.controller = controller
        Button(self, text='Back to Main', command=lambda: self.controller.frameChange(0)).pack()

class MainFrame(Frame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller

        #frame sectioning
        topframe = Frame(self)
        middleframe = Frame(self)
        bottomframe = Frame(self)

        #frame packing
        topframe.pack(padx=10, pady=5)
        middleframe.pack(fill=BOTH, expand=True)
        bottomframe.pack(padx=10, pady=10)

        #grid packing for middle frame
        middleframe.columnconfigure(0, weight=1)
        middleframe.columnconfigure(1, weight=1)

        #buttons
        autoExpensesSplitterButton = Button(middleframe, text='Automatic Expenses Splitter', command=lambda: self.controller.frameChange(1))
        expensesTrackerButton = Button(middleframe, text='Expenses Tracker', command=lambda: self.controller.frameChange(2))

        #labels
        title = Label(topframe, text='(title here)')

        #packing
        autoExpensesSplitterButton.pack(padx=10, pady=10)
        expensesTrackerButton.pack(padx=10, pady=10)
        title.pack(pady=10)

class FrameChanging:
    def __init__(self, root):
        self.root = root

        self.frameList = [MainFrame(root, self), AutoExpensesSplitterFrame(root, self), ExpensesTrackerFrame(root, self)] #setup the frame list
        self.currentIndex = 0 #default frame page
        self.frameList[0].pack(expand=True, fill=BOTH)

    def frameChange(self, index):
        self.frameList[self.currentIndex].pack_forget() #make the page blank
        self.currentIndex = index
        self.frameList[self.currentIndex].pack(expand=True, fill=BOTH) #fill in the new page

#function to senter the window
def centerWindow(window, width, height):
    #get screen width and height
    screenWidth = window.winfo_screenwidth()
    screenHeight = window.winfo_screenheight()

    #calculate position coordinates
    x = (screenWidth - width) // 2
    y = (screenHeight - height) // 3

    #set window geometry
    window.geometry(f"{width}x{height}+{x}+{y}")

centerWindow(root, 500, 400)
app = FrameChanging(root)
root.mainloop()