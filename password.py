#import GUI widgets needed
from guizero import App, Text, PushButton, TextBox, info
app = App("Password")

#Function definition
def button_pushed():
    if text_box.value == text_box2.value:
        info("Password check", text="Great! The passwords you entered are the same")
    else:
        info("Password check", text="Sorry! The passwords do not match. Try again")

#GUI Widgets
txt = Text(app, text="Hello! Please enter a password")
text_box = TextBox(app)
txt = Text(app, text="Please! Enter your password again")
text_box2 = TextBox(app)
btn_push = PushButton(app, command=button_pushed, text="Submit")

#Display GUI on the screen
app.display()