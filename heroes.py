from guizero import App, Text, ButtonGroup, Combo, PushButton, TextBox
app = App(title="Hero-o-matic", width=300)

def make_hero_name():
    adjective = bgp_adjective.value
    colour = txt_colour.value
    animal = cmb_animal.value
    hero = adjective + " " + colour + " " + animal
    lbl_output.value = "You are... The " + hero + "."

message1 = Text(app, text="Choose an adjective")
bgp_adjective = ButtonGroup(app, options=["Amazing", "Bonny", "Charming", "Delightful"], selected="Amazing")

message2 = Text(app, text="Enter a colour?")
txt_colour = TextBox(app)

message3 = Text(app, text="Pick an animal?")
cmb_animal = Combo(app, options=["Aardvark", "Badger", "Cat", "Dolphin" , "Velociraptor"])

btn_make_name = PushButton(app, text='Make a heroe', command=make_hero_name)

lbl_output = Text(app, text="A hero name will appear here")

app.display()