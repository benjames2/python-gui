# Import the GUI widgets that you'll be using, and create the 'app' for your program.
from guizero import App, TextBox, PushButton, Text, info
app = App()

# Function definitions for your events go here.
def btn_go_clicked():
    info("Greetings","Hello, " + txt_name.value + " - I hope you're having a nice day")

def btn_animal_clicked():
    info("Favorite Animal", "The " + txt_animal.value + " is also one of my favorite")

def btn_age_clicked():
    if int(txt_age.value) < 30:
        info("Age", "you're still young. Make the right choices")
    elif int(txt_age.value) > 30 and int(txt_age.value) < 60:
        info("Age", "Nice. you are not old yet.")
    else:
        info("Age", "You are pretty old")

# Your GUI widgets go here
lbl_name = Text(app, text="Hello. What's your name?")
txt_name = TextBox(app)
btn_go = PushButton(app, command=btn_go_clicked, text="Done")
lbl_name = Text(app, text="What is your favorite animal?")
txt_animal = TextBox(app)
btn_go_animal = PushButton(app, command=btn_animal_clicked, text="OK")
lbl_name = Text(app, text="How old are you?")
txt_age = TextBox(app)
btn_go = PushButton(app, command=btn_age_clicked, text="DONE")

# Show the GUI on the screen
app.display()