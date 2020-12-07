import tkinter
import tkinter.messagebox as box
import random

class MyGUI:
    def __init__(self):
        # Create the main window.
        self.mainWindow = tkinter.Tk()
        self.mainWindow.geometry("200x200")
        self.mainWindow.title("Rock Paper Scissors")

        # Create two frames. One for the Radiobuttons
        # and another for the regular Button widgets.
        self.radioFrame = tkinter.Frame(self.mainWindow)
        self.buttonFrame = tkinter.Frame(self.mainWindow)

        # Create an StringVar object to use with
        # the Radiobuttons.
        self.radioVar = tkinter.StringVar()

        # Set the StringVar object to 1.
        self.radioVar.set(1)

        # Create the Radiobutton widgets in the top_frame.
        self.rb1 = tkinter.Radiobutton(self.radioFrame, text='Rock', variable=self.radioVar, value='Rock')
        self.rb2 = tkinter.Radiobutton(self.radioFrame, text='Paper', variable=self.radioVar, value='Paper')
        self.rb3 = tkinter.Radiobutton(self.radioFrame, text='Scissors', variable=self.radioVar, value='Scissors')

        # Pack the Radiobuttons.
        self.rb1.pack()
        self.rb2.pack()
        self.rb3.pack()

        # Set up buttons
        self.okButton = tkinter.Button(self.buttonFrame, text='OK', command=self.showOption)
        self.quitButton = tkinter.Button(self.buttonFrame, text='Quit', command=self.mainWindow.destroy)

        # Pack the Buttons.
        self.okButton.pack(side='left')
        self.quitButton.pack(side='left')

        # Pack the frames.
        self.radioFrame.pack()
        self.buttonFrame.pack()

        # Start the mainloop.
        tkinter.mainloop()
    
    #create a function to show winner
    def showOption(self):
        #make list of options for computer
        options = ["Rock", "Paper", "Scissors"]
        #choose random computer option 
        option = random.choice(options)
        #show both the user and computer's choice
        box.showinfo('Selection', 'Computer selected: {}\nYou selected: {}'.format(option, self.radioVar.get()))
        
        #depict who is the winner based on their choices
        if option == "Rock" and self.radioVar.get() == "Scissors":
            box.showinfo('Winner', "Rock crushes scissors. Computer wins")
        elif option == "Rock" and self.radioVar.get() == "Paper":
            box.showinfo('Winner', "Paper beats rock. You win")
        elif option == "Rock" and self.radioVar.get() == "Rock":
            box.showinfo('Winner', "Tie. There is no winner")

        elif option == "Scissors" and self.radioVar.get() == "Rock":
            box.showinfo('Winner', "Rock crushes scissors. You win")
        elif option == "Scissors" and self.radioVar.get() == "Paper":
            box.showinfo('Winner', "Scissors beats paper. Computer wins")
        elif option == "Scissors" and self.radioVar.get() == "Scissors":
            box.showinfo('Winner', "Tie. There is no winner")

        elif option == "Paper" and self.radioVar.get() == "Scissors":
            box.showinfo('Winner', "Scissors beats paper. You win")
        elif option == "Paper" and self.radioVar.get() == "Rock":
            box.showinfo('Winner', "Paper beats rock. Computer wins")
        elif option == "Paper" and self.radioVar.get() == "Paper":
            box.showinfo('Winner', "Tie. There is no winner")
        
#call the class
demoGUI = MyGUI()
