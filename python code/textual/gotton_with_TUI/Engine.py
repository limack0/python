"""
    Application name : Limack gottom
    Author : <Limack zero>
    email : <mbeog@gmail.com>
    github : https://github.com/limack0/limack-gottom
    version : 0.0.1
    This class import the API from the project to laucnh the application
"""
from textual.app import * 
from textual.app import ComposeResult
from textual.widgets import *
from textual.containers import *
from enum import Enum

#----------------------Main class------------------------------------------
class GottomApp(App):
    ### Main class of the application
    CSS_PATH = "gottom.tcss"
    #Bindings for the application
    
    BINDINGS = [
        ("q","exit_game","Exit the game"),
    ]
    
    def compose(self):
        # Widgets of the app. wher we add the screen container and the user interface
        yield Header(id="mainScreenHeader", show_clock= True)
        yield Footer()
        # Declare the @screencontainer and the user container
        with Vertical(id="mainContainer"):
            yield ScreenContainer(id="screenContainer")
            yield UserContainer(id="userContainer")
            
    # Exit the game while typing "q"
    def action_exit_game(self):
        self.exit()
        
        
### USerContainer class     
class UserContainer(Static):
    def compose(self):
        with Horizontal():
            yield Button("Start", variant="default", id="startButton")
            yield Button("Stop", variant="warning", id="stopButton")
            yield Button("Ok", variant="success", id="okButton")
            yield inputContainer(id="inputContainer")
            
            

#Input container for the user        
class inputContainer(Static):
    
    input_message = {'name': 'enter your name',
                     'grade' : 'enter your grade',
                     'unlock_code' : 'enter the unlock code',
                     }

    def compose(self):
         yield Input(placeholder=" VESSEL COMMANDS BOARD.") 

### ScreenContainer class        
class ScreenContainer(Static):
    
    def compose(self):
        with Vertical():
            yield textContainer.msg(id = "textContainer")
            yield animationContainer(id = "animationContainer")
    
### textContainer content in Screencontainer
class textContainer(Static):
    def msg(self):
        self.msg=Static (""" Welcome to the VESSEL COMMANDS BOARD.
            For the moment you will just see that
            See you soon for the real content
            By the way i am Learning textualize
            Type 'q' to exit the game.
         """) 


### animationContainer content in Screencontainer
class animationContainer(Static):
    def compose(self):
        yield LoadingIndicator() 
    
    

        
        
if __name__ == '__main__':
    GottomApp().run()
        
        
        
        