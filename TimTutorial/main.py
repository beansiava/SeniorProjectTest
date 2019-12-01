from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen


class ScreenManagement(ScreenManager):
    pass


class FirstPage(Screen):

    def calculate(self, point_from, point_to):
        print("point_from={0}, point_to={1}".format(point_from, point_to))


class SecondPage(Screen):
    pass


class TestApp(App):
    title = "Login Screen"

    def build(self):
        return ScreenManagement()


if __name__ == "__main__":
    TestApp().run()