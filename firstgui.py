from guizero import App, Text

app = App(title="This is my first GUI")

firstmessage = Text(app, text="guis are cool")
secondmessage = Text(app, text="this is green")
thirdmessage = Text(app, text="Hello world! This is cool!!")

firstmessage.size = 40
secondmessage.bg = "green"
thirdmessage.bg = "red"
thirdmessage.size = 30
thirdmessage.font = "times new roman"


app.display()