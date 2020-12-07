#Deena Dayal


import tkinter
import tkinter.messagebox as box

class MyGUI:
    def __init__(self):
        # Create the main window.
        self.mainWindow = tkinter.Tk()
        self.mainWindow.geometry("200x200")
        self.mainWindow.title("ATM")
        #counter for running total in account
        self.total = 0

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
        self.rb1 = tkinter.Radiobutton(self.radioFrame, text='Deposit', variable=self.radioVar, value='Deposit')
        self.rb2 = tkinter.Radiobutton(self.radioFrame, text='Withdrawal', variable=self.radioVar, value='Withdrawal')
        self.rb3 = tkinter.Radiobutton(self.radioFrame, text='Check Account Balance', variable=self.radioVar, value='Check Account Balance')

        # Pack the Radiobuttons.
        self.rb1.pack()
        self.rb2.pack()
        self.rb3.pack()

        # Set up buttons
        self.proceedButton = tkinter.Button(self.buttonFrame, text='Proceed', command=self.showOption)
        self.quitButton = tkinter.Button(self.buttonFrame, text='Quit', command=self.mainWindow.destroy)

        # Pack the Buttons.
        self.proceedButton.pack(side='left')
        self.quitButton.pack(side='left')

        # Pack the frames.
        self.radioFrame.pack()
        self.buttonFrame.pack()

        # Start the mainloop.
        tkinter.mainloop()
        

    #runs once user choose their bank option 
    def showOption(self):
        #if user chooses deposit
        if self.radioVar.get() == "Deposit":

            #create deposit window
            self.depositWindow = tkinter.Tk()
            self.depositWindow.geometry("250x80")
            self.depositWindow.title("Deposit")

            #give it a label, entry and button frame
            self.depositLabelFrame = tkinter.Frame(self.depositWindow)
            self.depositEntryFrame = tkinter.Frame(self.depositWindow)
            self.depositButtonFrame = tkinter.Frame(self.depositWindow)

            #create label, entry 
            self.depositLabel = tkinter.Label(self.depositLabelFrame, text="Enter the amount you want to deposit.")
            self.depositEntry = tkinter.Entry(self.depositEntryFrame)

            #create ok button uses balance method
            self.depositOkButton = tkinter.Button(self.depositButtonFrame, text='OK', command=self.balance)
            #create cancel button returns to main window
            self.depositCancelButton = tkinter.Button(self.depositButtonFrame, text='Cancel', command=self.depositWindow.destroy)

            #pack all widgets and frames
            self.depositOkButton.pack(side='left')
            self.depositCancelButton.pack(side='left')
            self.depositLabelFrame.pack()
            self.depositEntryFrame.pack()
            self.depositButtonFrame.pack()
            self.depositEntry.pack()
            self.depositLabel.pack()
    
        #if user chooses withdrawal
        elif self.radioVar.get() == "Withdrawal":
            
            #create withdrawal window
            self.withdrawalWindow = tkinter.Tk()
            self.withdrawalWindow.geometry("250x80")
            self.withdrawalWindow.title("Withdrawal")
            #give it a label, entry and button frame
            self.withdrawalLabelFrame = tkinter.Frame(self.withdrawalWindow)
            self.withdrawalEntryFrame = tkinter.Frame(self.withdrawalWindow)
            self.withdrawalButtonFrame = tkinter.Frame(self.withdrawalWindow)

            #create label, entry
            self.withdrawalLabel = tkinter.Label(self.withdrawalLabelFrame, text="Enter the amount you want to withdrawal")
            self.withdrawalEntry = tkinter.Entry(self.withdrawalEntryFrame)

            #create ok button uses balance method
            self.withdrawalOkButton = tkinter.Button(self.withdrawalButtonFrame, text='OK', command=self.balance)
            #create cancel button returns to main window
            self.withdrawalCancelButton = tkinter.Button(self.withdrawalButtonFrame, text='Cancel', command=self.withdrawalWindow.destroy)

            #pack all widgets and frames
            self.withdrawalOkButton.pack(side='left')
            self.withdrawalCancelButton.pack(side='left')
            self.withdrawalLabelFrame.pack()
            self.withdrawalEntryFrame.pack()
            self.withdrawalButtonFrame.pack()
            self.withdrawalEntry.pack()
            self.withdrawalLabel.pack()

        #if user chooses check account balance
        elif self.radioVar.get() == "Check Account Balance":

            #show current balance in account using running total
            balance = "You have ${:.2f} in your account.".format(self.total)
            box.showinfo("Check Account Balance", balance)

            
    #runs after user has clicked enter and deposited/withdrew amount 
    def balance(self):
        #if user chose deposit
        if self.radioVar.get() == "Deposit":
            #show amount they deposited
            deposit = "You have deposited ${:.2f} into your account.".format(float(self.depositEntry.get()))
            #add amount to running total
            self.total += float(self.depositEntry.get())
            box.showinfo("Deposit", deposit)
            
        #if user chose withdrawal
        elif self.radioVar.get() == "Withdrawal":
            #show amount they withdrew
            withdrawal = "You withdrew ${:.2f} from your account.".format(float(self.withdrawalEntry.get()))
            #subtract amount from running total
            self.total -= float(self.withdrawalEntry.get())
            box.showinfo("Withdrawal", withdrawal)
        
        #after user chooses either deposit or withdrawal, show updated balance
        finalBalance = "Your new balance is ${:.2f}".format(self.total)
        box.showinfo("Updated Account Balance", finalBalance)

#call class mygui
run = MyGUI()
