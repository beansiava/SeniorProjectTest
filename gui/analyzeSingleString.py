from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from textblob import TextBlob


class InputText(App):

    def build(self):
        self.box = BoxLayout(orientation='horizontal', spacing=20)
        self.txt = TextInput(hint_text='Write here', size_hint=(.5, .1))
        self.btn = Button(text='send text', on_press=self.clearText, size_hint=(.1, .1))
        self.box.add_widget(self.txt)
        self.box.add_widget(self.btn)

        return self.box

    def clearText(self, instance):
        save = self.txt.text
        print(save)
        opinion = TextBlob(save)
        print(opinion.sentiment)
        self.txt.text = ''


InputText().run()