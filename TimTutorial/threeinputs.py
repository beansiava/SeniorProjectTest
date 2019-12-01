import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button




# We can have a class to hold all of our design elements
# Note: there are also BoxLayouts & other types as well
class MyGrid(GridLayout):
#     Create initialization (kwargs handles input keywords)
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.cols = 1

        """IN ORDER TO GET THE LAYOUT WE WANT, WITH KIVY - WE NEED TO NEST GRIDS"""
        self.nestedgrid = GridLayout()
        self.nestedgrid.cols = 2


        self.nestedgrid.add_widget(Label(text="hello there"))
        self.name = TextInput(multiline=False)
        self.nestedgrid.add_widget(self.name)

        self.nestedgrid.add_widget(Label(text="these droids"))
        self.droids = TextInput(multiline=False)
        self.nestedgrid.add_widget(self.droids)

        self.nestedgrid.add_widget(Label(text="are not the ones"))
        self.last = TextInput(multiline=False)
        self.nestedgrid.add_widget(self.last)

        self.add_widget(self.nestedgrid)

        self.nextpagebutton = Button(text="next page", font_size=24)
        self.nextpagebutton.bind(on_press = self.nextpage)
        self.add_widget(self.nextpagebutton)
        self.x = 0

    """THE FIRST EVENT FUNCTION I'VE MADE"""
    def nextpage(self,instance):
        self.x = self.x + 1
        name = self.name.text
        droids = self.droids.text
        last = self.last.text
        print("number of inputs:", self.x, "name:", name,"droids:", droids, "last:", last)

# no need for __init__ so we can default call the constructor of the app frame
class MyApp(App):
    # Builds all inherited
    def build(self):
        return MyGrid()


"""This allows us to build the kivy window  [run() is configured in the import App]"""
if __name__ == "__main__":
    MyApp().run()