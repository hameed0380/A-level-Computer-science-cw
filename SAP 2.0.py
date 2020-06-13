# Code For Survival Rate Application
'''Firstly, we import the relevant libraries. Tkinter to build the GUI for
the app,SQLite3 for interaction with the database. Tkinter and SQLite3 are
libraries that come with the standard Python library. Time for delays and
pauses, PIL for adding images.'''

'''---Import Modules---'''
# To import everything from tkinter
from tkinter import *
# To import font from tkinter
from tkinter import font
# To import messagebox from tkinter
import tkinter.messagebox     

# To be able to use string. values
import string
# Importing everything from random module
from random import *
# To copy items to clipboard
import pyperclip 

# Imports time from the webbrowser which allows use to create delays in code.
import time,webbrowser
import time

# To import and show images
from PIL import Image, ImageTk

# For tables and database(interactions)
import sqlite3 as sq

#To import pygame module to run simulation
import pygame
# To import random module
import random
# To use mathematical equations
import math


'''---Program Window---'''
# Creating the class, Window, and inheriting from the Frame which is a class from tkinter
# class. Frame is a class from the tkinter module 
class Window(Frame):

    # Define settings upon initialization. At this point you can specify
    def __init__(self, master=None):
        
        # parameters that you want to send through the Frame class 
        Frame.__init__(self, master)   

        #reference to the master widget created, which is the tk window                 
        self.master = master

        #To run init_window, which does not exist yet
        self.init_window()

    #Creation of init_window
    def init_window(self):

        #changing the title of the master widget to Survival Rate Application     
        self.master.title("Survival Application Project")

        '''allowing the widget to take the full space of the root window
        so widgit is continuously shown even when root window has been changed
        in size'''
        self.pack(fill=BOTH, expand=1)

        #creating a menu instance
        menu = Menu(self.master, tearoff=False)
        self.master.config(menu=menu)

        #create the calculator object
        calculator = Menu(menu)
        #added "Calculator" to the menu that has been created
        menu.add_command(label="Calculator", command=self.TCalculator)

        '''Labels the part of the menu Calculator performs the command which
        is the function TCalculator, runs the calculator program'''
        
        #create the Simulator object
        Simulator = Menu(menu)
        #added "Simulator" to the menu created
        menu.add_command(label="Simulator", command=self.Run)

        '''Labels the part of the menu Simulator performs the command which
        is the function Run, the simulation'''

        #create the edit object
        edit = Menu(menu)
        '''In this section have chosen not to show the edit object 
        in the menu as we are not including it in the menu bar'''
        
        '''adds a command to the menu option, calling it show the image chosen
        (image must fit the dimensions of the User Interface)'''    
        #command it runs on event is showImg
        edit.add_command(command=self.showImg())
        #command it runs on event is showText
        edit.add_command(command=self.showText())

        '''In this section I created the oject edit to be able to show the title
        of the window and display the image, this will not appear on the menu'''

        #create the Database object
        Database = Menu(menu, tearoff=False)
        #added "database" to the menu that has been created as a cascade
        menu.add_cascade(label="Database", menu=Database)
        Database.add_command(label="Store", command=self.Store)
        Database.add_command(label="Unique-ID", command=self.unique_id)


        '''In this section I created the oject database with the label store
        this will run the function store, runs the database program'''

        #create the help_centre object
        help_centre = Menu(menu, tearoff=False)
        #added "Help Centre" to the menu that has been created
        menu.add_cascade(label="Help Centre", menu=help_centre)
        '''When the help centre button is clicked the Help object should be
        shown, carry out its command in the function Help'''
        help_centre.add_command(label="Help", command=self.Help)
        help_centre.add_command(label="Instructions", command=self.mess)


        '''In this section I created the oject help_centre with the label Help
        this will run the function Help, runs the help centre program'''

        '''---About section---'''
        # Function to run messagebox for button
        def info():
            tkinter.messagebox.showinfo('About', 'SAP is an application dedicated to finding \nthe survival rate of organisms and storing \nthem in a database')
        # Create the title about for the messagebox
        
        Button(text='About', command=info).place(x=350,y=270)
        # Button to open the messagebox

        #run the mainloop / keeps the root window open, this loop is set to the root window
        root.mainloop()

    '''---Instructions---'''
    # Function to run instriction page in help centre
    def mess(self):
        window = Tk() # Creating window for instructions
        window.title("Instructions") # Title of the root window is set to SAP Database
        S = Scrollbar(window) # create scrollbar widget within window
        T = Text(window, height=20, width=50) # Creating text box
        S.pack(side=RIGHT, fill=Y) # Pack scrollbar winthin window
        T.pack(side=LEFT, fill=Y) # Pack text box winthin window
        S.config(command=T.yview)
        T.config(yscrollcommand=S.set) #Set the scrollbar to scroll with text box
        quote = """---Instructions---

SAP is an application dedicated to finding
the survival rate of organisms and storing
them in a database.

The Survival calculator is a program that
allows the user to input different conditions
that result in an output.
1. The organism name must be in text no numbers
2. The environment must be in text no numbers
3. The no. of chromosomes must be an integer
4. The temperature must be an integer 
5. The allele frequency must be an integer
6. The amount of nutrients must be an integer
7. The light intensity must be an integer
8. The water available must be an integer
9. The Wind per day must be an integer
10. The Rain per day must be an integer
11. Do not enter text in survival rate box

The simulation is run when clicked by the 
user in the menu. To proceed in the simulation
use the mouse to click the screen. The moving 
heads are the organisms while the green objects
are food.

The database has certain restrictions and 
validations.
- The OrganismName must be letters only
- The SurvivalRate must be integers only
- The UniqueID does not have restrictions
To generate a Unique ID sequence use the
unique-ID Program.
-To see the database click Open DB.
The help centre provides support to the
user in 2 ways. It both gives the instructions
and provides the help section which is a keyword 
search for solutions.

To search for a query use the help section."""
        T.insert(END, quote) # Place in text box
        #run the mainloop / keeps the root window open, this loop is set to the root window 
        window.mainloop()
        
    # Function to show the image in the window
    def showImg(self): # Pass through self parameter
        load = Image.open("SurviveImage.png")# Retrieves the image / identifies image
        render = ImageTk.PhotoImage(load)# Loads the image into the window (Displays image)
        # Generating the image

        # labels can be text or images
        img = Label(self, image=render) # Gives the label of images
        img.image = render # Defines img.image as render, so performs render
        img.place(x=100, y=30)# Location of the image and placement within the window

    # Function for displaying the text onto the window
    def showText(self): # Pass through self parameter
        text = Label(self, text="Welcome to the Survival Application Project", font="none 12 bold")
        text.pack()# Makes sure the text is stored in the window
        '''organizes widgets in blocks before placing them in
           the parent widget'''

    '''---Calculator---'''
    # Function for the calculator program
    def TCalculator(self): # Pass through self parameter

        #Code For Survival Rate calculator
        def show_answer():# Function for the addition of all the input besides the string
            blank.delete(0, END)
            Ans = int(num1.get()) + int(num2.get()) + int(num3.get()) + int(num4.get()) + int(num5.get()) + int(num6.get()) + int(num7.get()) + int(num8.get())   
            AnsA = Ans / 80  # Takes the answer generated and uses the survival rate formula to find the survival rate
            blank.insert(0, AnsA)# Displays the answer into the textbox once the button show has been clicked

        

        window = Tk() # creates a window for the program
        window.title("SAP Calculator")# Gives the title of the window SAP Calculator 
        window.geometry('330x270')# Sets the dimensions of the window

        
        Label(window, text = "Organism Name:").grid(row=0)
        Label(window, text = "Environment:").grid(row=1)
        Label(window, text = "Number of Chromosome:").grid(row=2)
        Label(window, text = "Temperature:").grid(row=3)
        Label(window, text = "Allele Frequency:").grid(row=4)
        Label(window, text = "Amount of nutrients:").grid(row=5)
        Label(window, text = "Light Intensity:").grid(row=6)
        Label(window, text = "Water Available:").grid(row=7)
        Label(window, text = "Wind per day:").grid(row=8)
        Label(window, text = "Rain per day:").grid(row=9)

        Label(window, text = "The Survival Rate is:").grid(row=10)

        # function created to prevent user from entering letters
        def validateV(self, *args):
                if not organism1.get().isalpha():
                        corrected = ''.join(filter(str.isalpha, organism1.get()))
                        organism1.set(corrected)# Set the box to not accept numbers

        
        # Create variables for each value we want to enter
        organism1 = StringVar(window)# Variable for organism
        organism1.trace('w', validateV)
        
        environment = StringVar(window)# Variable for survival

        '''Set the text boxes so that users can input the data.
        Tkinter provides the 'Entry' function so we can place text boxes into
        the GUI.'''

        #For the other user inputs
        organism12 = Entry(window, textvariable=organism1)# textbox for organism name
        environment = Entry(window)# textbox for the environment
        num1 = Entry(window)# textbox for the Number of Chromosome
        num2 = Entry(window)# textbox for the Temperature
        num3 = Entry(window)# textbox for the Allele Frequency
        num4 = Entry(window)# textbox for the Amount of nutrients
        num5 = Entry(window)# textbox for the Light Intensity
        num6 = Entry(window)# textbox for the Water Available
        num7 = Entry(window)# textbox for the Wind per day
        num8 = Entry(window)# textbox for the Rain per day
        # For the results
        blank = Entry(window)

        organism12.grid(row=0, column=1)
        environment.grid(row=1, column=1)
        num1.grid(row=2, column=1)
        num2.grid(row=3, column=1)
        num3.grid(row=4, column=1)
        num4.grid(row=5, column=1)
        num5.grid(row=6, column=1)
        num6.grid(row=7, column=1)
        num7.grid(row=8, column=1)
        num8.grid(row=9, column=1)

        blank.grid(row=10, column=1)


        Button(window, text='Quit', command=window.destroy).grid(row=14, column=0, sticky=W, pady=4)
        Button(window, text='Show', command=show_answer).grid(row=14, column=1, sticky=W, pady=4)

        #run the mainloop / keeps the root window open, this loop is set to the root window
        window.mainloop()
        

        
        
    '''---Help Centre---'''
    #The Help centre function linking to the help centre 
    def Help(self):      
        #  The SAP Help Centre
        
        # Function to collect data once clicked
        def click():
            entered_text=textentry.get() # Collect the text from the text entry box
            output.delete(0.0, END)
            '''A defintion based on the input will be displayed on the output box
               if it is in the dictionary'''
            try:   # If the word is in the dictionary this will happen
                definition = my_helpdictionary[entered_text]

             # If the word is not in the dictionary this will happen
            except:    
                definition = "Please type in whether it is the gui simulation, calculator or database you have a problem with.\nIt must be 1 word and lower case i.e simulation, calculator, database, gui"
            output.insert(END, definition)
            '''Definition in this case will be displayed in the ouput box'''
      
        #main window
        window = Tk() # Creating the window
        window.title("SAP Help")# Creating the title of the window 
        window.geometry("445x320")# Have the window at this size
        window.config(background="light blue")# Set background to light blue

##        #Image
##        photo1 = PhotoImage(file="Smallville.png")
##        Label (window, image=photo1) .place(x=300, y=30)

        # Create Label for Title of the program
        Label (window, text="SAP HELP"
               ,bg="light blue", fg="dark green", font="none 14 bold") .grid(row=1, column=0, sticky=W)
        # .grid to position the label for Title of the program

        # Create Label for asking question
        Label (window, text="Enter the part of the program\n that you have a problem with:"
               ,bg="light blue", fg="black", font="none 12 bold") .grid(row=2, column=0, sticky=W)
        # .grid to position the label for asking questions

        # Create text box to enter query
        textentry=Entry(window, width=20, bg="white") # Create the text box within the window
        textentry.grid(row=3, column=0, sticky=W) # Set the location for the text box

        # add submit button to run function click
        Button(window, text="SUBMIT", width=6, command=click) .grid(row=4, column=0, sticky=W)
        # .grid to position the button submit

        # create label for the solution section
        Label (window, text="\nSolution:",bg="light blue", fg="black",
               font="none 12 bold") .grid(row=5, column=0, sticky=W)
        # .grid to position the button submit

        # Create another text box for the response and the output
        output = Text(window, width=55, height=6, wrap=WORD, background="white")
        output.grid(row=6, column=0, columnspan=2, sticky=W)
        # .grid to position the output box

        # create label for the solution section
        Label (window, text="\nMake sure it is lower case and 1 word",bg="light blue", fg="red",
               font="none 10 bold") .grid(row=7, column=0, sticky=W)
        # .grid to position the button submit

        # The dictionary for the input and response generated for the help centre
        my_helpdictionary = {
            'simulation': 'Please set the conditions you would like then click start.',
            'calculator': 'Type in the correct values whether it is a letter or number',
            'database': 'The database is where you store the results for the survival rate programs.',
            'gui': 'The GUI is the screen the user interacts with to go to the programs they would like to use.' 
            } 
        # word , followed by the response that should be generated in output box
            
        #run the mainloop / keeps the root window open, this loop is set to the root window
        window.mainloop()

    '''---Database---'''
    # Function for running the database
    def Store(self): # Pass through self parameter
        #creating the table for the database
        table_survival = 'table_survival' # Called table_survival

        window = Tk()# Root window is created and assigned to 'window'
        window.title("SAP Database") # Title of the root window is set to SAP Database
        window.geometry('700x420') # Size of the window is set
        #variable to create header
        header = Label(window, text="SAP DATABASE", # Text to form a header for the GUI
                       font=("arial",20,"bold"), fg="medium spring green").pack()# Makes sure the text is stored in the window

        '''Specificities of the label and the typeface of the text'''

        con = sq.connect('Sap.db') # dB browser for sqlite needed, connects to Sap.db database
        c = con.cursor() # SQLite command, to connect to db Sap,db so 'execute' method can be called
        '''To connect to the database, created a 'connect'
        object and name the database.
        Cursor will allow us to call 'execute' method, which allows for
        SQL commands. The execute method allows for a table
        to be created.'''

        # Get labels for the desired information we want to input
        L1 = Label(window, text = "OrganismName", font=("arial",18)).place(x=10,y=150) # Specify Position
        L2 = Label(window, text = "SurvivalRate", font=("arial",18)).place(x=10,y=200) # Specify Position
        L3 = Label(window, text = "UniqueID", font=("arial",18)).place(x=10,y=250) # Specify Position
        # To set the labels in the window, apply '.place' to each label
        # To get The buttons in place trial and error was required


        # Create variables for each value we want to enter
        
        # function created to prevent user from entering numbers
        def validate(self, *args):
                if not organism.get().isalpha():
                        corrected = ''.join(filter(str.isalpha, organism.get()))
                        organism.set(corrected)# Set the box to not accept numbers

        # function created to prevent user from entering letters
        def validate2(self, *args):
                if not survival.get().isnumeric():
                        corrected = ''.join(filter(str.isnumeric, survival.get()))
                        survival.set(corrected)# Set the box to not accept letters


        # Create variables for each value we want to enter
        organism = StringVar(window)# Variable for organism
        organism.trace('w', validate)
        
        survival = StringVar(window)# Variable for survival to keep as integer
        survival.trace('w', validate2)

        unique = StringVar(window)# Variable for unique id to keep as string

        '''Set the text boxes so that users can input the data.
        Tkinter provides the 'Entry' function so we can place text boxes into
        the GUI.'''
        # Entry for 'organismO' in GUI
        organismO = Entry(window, textvariable=organism) # Variable for entry box
        organismO.place(x=220,y=155)# To determine location of text boxes

        # Entry for 'survivalS' in GUI
        survivalS = Entry(window, textvariable=survival) # Variable for entry box
        survivalS.place(x=220,y=205)# To determine location of text boxes

        # Entry for 'uniqueU' in GUI
        uniqueU = Entry(window, textvariable=unique) # Variable for entry box
        uniqueU.place(x=220,y=255)# To determine location of text boxes

        def get():
                print("You have submitted a record")# Tell the user that they have entered the relevant data

                '''To create table in table_survival in the database if not created
                with the field names OrganismName, SurvivalRate, UniqueID'''
                c.execute('create table if not exists ' + table_survival + '(OrganismName text,  SurvivalRate integer,  UniqueID text)') #SQL syntax        

                # To insert the data into database in called the table called table_survival
                # Isolating the text/option with .get()
                c.execute('insert into ' + table_survival + '(OrganismName, SurvivalRate, UniqueID) VALUES (? , ? , ?)',
                          (organism.get() ,survival.get() ,unique.get())) # Insert record into database Sap.db in the table table_survival.
                con.commit() 

        # To clear boxes when submit button is clicked
        # Reset fields after submit
        def clear(): #Function for clearing entry boxes
            organism.set('')# Set organism to clear
            survival.set('')# Set survival to clear
            unique.set('')# Set unique to clear

        def record():
            c.execute('SELECT * FROM  table_survival')
            # Select all data from the table_survival database

            frame = Frame(window)# Create a frame within the window
            frame.place(x= 360, y = 150)
            # To set the frame in the window and it's location
            
            Lb = Listbox(frame, height = 8, width = 35,font=("arial", 12))# To create the listbox
            Lb.pack(side = LEFT, fill = Y)# To make sure the widget is in the window
            # Specifiy location
            
            scroll = Scrollbar(frame, orient = VERTICAL)
            # Set scrollbar to list box for when entries exceed size of list box
            scroll.config(command = Lb.yview)# Make the scrollbar
            scroll.pack(side = RIGHT, fill = Y)# Positioning of the scrollbar
            Lb.config(yscrollcommand = scroll.set)

            Lb.insert(0, 'OrganismName | SurvivalRate | UniqueID')
            # first row in listbox
            
            data = c.fetchall()
            # Gets(fetches) all the data from the table table_surivial
            
            for row in data: # For loop, for all data in the row specified
                Lb.insert(1,row)
                # Inserts record row by row in list box

            # Display this label that has been positioned under the frame
            L8 = Label(window, text = "From the most recent", 
                       font=("arial", 12)).place(x=400,y=330)# Location of Label
            con.commit()# Sends a COMMIT statement to MySQL server committing the current transaction.


        # To create the button to submit the entry value
        button_1 = Button(window, text="Submit",command=get)
        button_1.place(x=100,y=300)# Perform Get Function to retrieve the data from the database

        # To create the button to clear the entered values
        button_2 = Button(window,text= "Clear",command=clear)
        button_2.place(x=10,y=300)# Perform Clear Function To clear the data entered in text boxes

        # To create the button to open the database and show entered values and fieldnames
        button_3 = Button(window,text="Open DB",command=record)
        button_3.place(x=10,y=350)# Perform Record Function To display stored data in the database and fieldnames

        #Keep the root window open, loop set to the root window
        window.mainloop()

    '''---Unique Identifier---'''
    # Create Random Unique Identifier
    def unique_id(self):
        def generate():
            unique2.delete(0, END) # Removes/deletes existing content in entry box blank
            min_char = 8 # Set minimum length
            max_char = 8 # Set maximum length
            allchar = string.ascii_letters + string.digits # creates random string with letters and numbers
            uni_code = "".join(choice(allchar) for x in range(randint(min_char, max_char)))
            unique2.insert(0, uni_code)# Places the unique id into entry box

        # Function for copying unique id to clipboard 
        def copy1(): 
                random_id = unique2.get() 
                pyperclip.copy(random_id) 

        window = Tk()
        # Title of your GUI window 
        window.title("SAP Unique ID")
        window.geometry('260x80')

        # create label for the title of the window
        Label(window, text = "SAP Unique ID").place(x=11,y=1)
        # create label for the unique id
        Label(window, text = "Unique ID:").place(x=10,y=20)

        # create entry box for entering the unique id 
        unique2 = Entry(window)
        unique2.place(x=70,y=20) # places the box in a particular position
        # this section required trial and error 

        # create Button Copy which will copy the contents of the blank entry box
        # unique identifier copied to clipboard
        copy_button = Button(window, text="Copy", command=copy1).place(x=200,y=50)

        # create button which will exit window
        Button(window, text='Quit', command=window.destroy).place(x=10,y=50)
        # create button which will generate the unique id 
        Button(window, text='Generate', command=generate).place(x=200,y=20)

        #run the mainloop / keeps the root window open, this loop is set to the root window
        window.mainloop()


        
    '''---Simulation---'''
    #The simulation
    def Run(self):
        # Colors defined with variables
        BLACK = (0, 0, 0) # Black colour
        WHITE = (255, 255, 255) # White colour
        GREEN = (0, 255, 0) # Green colour
        RED = (255, 0, 0) # Red colour
        BLUE = (0, 0, 255) # Blue colour
         
        # Class for food
        class Food(pygame.sprite.Sprite):
            '''
            This class represents the Food.
            It derives from the "Sprite" class in Pygame.
            '''
         
            def __init__(self, color, width, height):
                ''' Constructor. Pass in the color of the food,
                and its size. '''
         
                # Call the parent class (Sprite) constructor
                super().__init__()

                # Create an image of the Food, and fill it with a color.
                # This could also be an image loaded from the disk.
                self.image = pygame.Surface([width, height])
                self.image.fill(WHITE)
                self.image.set_colorkey(WHITE) # Stops the colour white being shown
                pygame.draw.ellipse(self.image,color, [0,0,width,height])
                # Draws ellipses shape

         
                # Update the position of this object by setting the values
                # of rect.x and rect.y
                self.rect = self.image.get_rect()
         

         
        class Organism(pygame.sprite.Sprite):
            '''Class to represent the organism. '''
            def __init__(self):
                ''' Create the organism image. '''
                
                # Call the parent class (Sprite) constructor (super function)
                super().__init__()
                # Loads the image for the organism(rabbit1)
                self.image = pygame.image.load("rabbit1.png").convert()
                # Removes the colour black, adds transparency
                self.image.set_colorkey(BLACK)
                
                '''This updates the position of the object create by setting the values
                of rect.x and rect.y'''
                self.rect = self.image.get_rect()

                # The "center" the sprite will orbit
                self.center_x = 0 # Position on screen
                self.center_y = 0 # Position on screen
         
                # Current angle in radians
                self.angle = 0
         
                # How far away from the center to orbit, in pixels
                self.radius = []
         
                # How fast to orbit, in radians per frame
                self.speed = 0.05
         
            def update(self):
                ''' Update the organism's position. '''
                # Calculate a new x, y
                self.rect.x = self.radius * math.sin(self.angle) + self.center_x
                self.rect.y = self.radius * math.cos(self.angle) + self.center_y
         
               # Increase the angle
                self.angle += self.speed


                
         
        # Initialize Pygame
        pygame.init()
         
        # Set the height and width of the screen
        SCREEN_WIDTH = 700 # Width
        SCREEN_HEIGHT = 400 # Height
        screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT]) # set screen size
        pygame.display.set_caption("SAP Simulation") # Sets title of screen

        # The background image for the simulation has been set
        gameplaybackground_img = pygame.image.load("grasss.png").convert()
        # The logo that will be displayed on the start page
        sap_imag = pygame.image.load("SurviveImage.png").convert()
        
        # This is a list of 'sprites.' Each object in the program is
        # added to this list. The list is managed by a class called 'Group.'
        food_group = pygame.sprite.Group()
        organism_group = pygame.sprite.Group()
         
        # This is a list of every sprite. All food and the organisms
        all_sprites_list = pygame.sprite.Group()
         
        for i in range(50):
            # This represents the food
            food = Food(GREEN, 20, 15)
         
            # Set a random location for the food
            food.rect.x = random.randrange(SCREEN_WIDTH)
            food.rect.y = random.randrange(SCREEN_HEIGHT)
         
            # Add the food to the list of objects
            food_group.add(food)
            all_sprites_list.add(food)

        # For the number of organisms
        for i in range(70): 
            # Create the RED organism block
            organism = Organism()

            # Set a random center location for the organism to orbit
            organism.center_x = random.randrange(SCREEN_WIDTH)
            organism.center_y = random.randrange(SCREEN_HEIGHT)
            # Random radius from 10 to 200
            organism.radius = random.randrange(10, 200)
            # Random start angle from 0 to 2pi
            organism.angle = random.random() * 2 * math.pi
            # radians per frame
            organism.speed = 0.010
            # Add the organism to the list of objects
            organism_group.add(organism)
            all_sprites_list.add(organism)
          
         
        # Loop until the user clicks the close button
        done = False
        # False so the organism will not disappear when collides
        dokillb = False
         
        # Used to manage how fast the screen updates
        clock = pygame.time.Clock()

        # To store the survival rate 
        score = 0
        # To set the generation of the organism
        generation = 1
        # This is a font used to draw text on the screen (size 36)
        font = pygame.font.SysFont('Calibri', 26, True, False)
         
        display_instructions = True
        instruction_page = 1

        simulation_page = 1

        # Event Processing 
        #  Instruction Page Loop 
        while not done and display_instructions:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True 
                if event.type == pygame.MOUSEBUTTONDOWN:
                    instruction_page += 1
                    if instruction_page == 3:
                        display_instructions = False
         
            # Set the screen background
            screen.fill(WHITE)
         
            if instruction_page == 1:
                # Draw instructions, page 1
                # This could also load an image created in another program.
                # That could be both easier and more flexible.
         
                text = font.render("Welcome to the Survival simulation", True, BLACK)
                screen.blit(text, [130, 10])# Displays text
         
                text = font.render("Click To Proceed", True, BLACK)
                screen.blit(text, [270, 40])# Displays text

                image = pygame.image.load("SurviveImage.png").convert()
                image.set_colorkey(BLACK)# Removes the colour black to hide colour around image
                screen.blit(image, [250, 60])# Displays image
         
            if instruction_page == 2:
                # Draw instructions, page 2
                text = font.render("Instructions", True, BLACK)
                screen.blit(text, [10, 10])# Displays text

                
                text = font.render("The moving objects are the organism", True, BLACK)
                screen.blit(text, [10, 70])# Displays text

         
                text = font.render("The green stationary object is the food", True, BLACK)
                screen.blit(text, [10, 100]) # Displays text

                text = font.render("The generation and survival rate are shown in the top corner", True, BLACK)
                screen.blit(text, [10, 130]) # Displays text
         
            # Limit to 60 frames per second
            clock.tick(60)
         
            # Go ahead and update the screen with what we've drawn.
            pygame.display.flip()

        # Event Processing 
        # Main Program Loop
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    simulation_page += 1
                    if simulation_page == 3:
                        display_instructions = False
                        
            if simulation_page == 1:
                all_sprites_list.update()
             
                # Clear the screen so the organism and food can be seen
                screen.fill(WHITE)
                # Select the font to use, size, bold, italics
                font = pygame.font.SysFont('Arial', 12, True, False)
             
                # Render the text. "True" means anti-aliased text.
                # Black is the color. This creates an image of the
                # letters, but does not put it on the screen
                text = font.render("Survival Rate Simulator", True, RED)
                text1 = font.render("Generation "+str(generation), True, RED)
                text2 = font.render("Survival Rate "+str(score)+"%", True, RED)
             
                # Put the image of the text on the screen at 250x250
                screen.blit(gameplaybackground_img, [0,0])
                screen.blit(text, [10, 10])
                screen.blit(text1, [10, 25])
                screen.blit(text2, [10, 40])

        
                # See if the organism has collided with anything then it will be added to the returned list
                food_eat_list = pygame.sprite.groupcollide(organism_group, food_group, dokillb, True)
             
                # Check the list of collisions
                for food in food_eat_list:
                    score += 1.5
                        # Check to see if all the blocks are gone.
            # Draw all the spites
            all_sprites_list.draw(screen)

            
            if simulation_page == 2:
                font = pygame.font.SysFont('Arial', 30, True, False)
                screen.fill(BLACK)

             
                # Render the text. "True" means anti-aliased text.
                # Black is the color. This creates an image of the
                # letters, but does not put it on the screen
                text = font.render("Survival Rate Simulator", True, RED)
                text1 = font.render("Generation "+str(generation), True, RED)
                text2 = font.render("Survival Rate "+str(score)+"%", True, RED)
                 
                # Put the image of the text on the screen at 250x250
                screen.blit(text, [200, 70])
                screen.blit(text1, [200, 120])
                screen.blit(text2, [200, 170])
         
            # Update the screen with what has been drawn
            pygame.display.flip()
         
            # Limit to 60 frames per second
            clock.tick(60)
        # Ends pygame 
        pygame.quit()

 



''' root window created. Here, that would be the only window, but
 you can later have windows within windows.'''

root = Tk()# Creating the window
root.geometry("400x300")# Defining and setting the dimesions of the window/client

#creation of an instance
app = Window(root)


#mainloop 
root.mainloop()  
