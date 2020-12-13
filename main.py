# python3 version 3.7.9
# pip3 version 20.1.1
# interpreter python 3.7
# kivy => pip install kivy
# run

import kivy
from kivy.app import App
from kivy.uix.label import Label
kivy.require("2.0.0")


class Chatty(App):
    def build(self):
        return Label(text="Hello World")


if __name__ == '__main__':
    Chatty().run()
