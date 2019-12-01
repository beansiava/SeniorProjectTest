from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen


class ScreenManagement(ScreenManager):
    pass


class StartPage(Screen):
    pass

class InputPage(Screen):

    def analyzeline(self, semantic):
        #TODO: call external function for analysis of first line input
        #TODO: call external function for analysis of second line input
        #TODO: combine the two and output into GUI
        return "hello"




class HistoryPage(Screen):

    def evaluatehistory():
        pass

    pass

class FeedbackPage(Screen):
    pass

class TestApp(App):
    title = "Welcome to Hue"

    def build(self):
        return ScreenManagement()


if __name__ == "__main__":
    TestApp().run()