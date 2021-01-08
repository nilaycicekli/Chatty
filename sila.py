from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRectangleFlatButton, MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivy.lang import Builder



LoginPage = """
MDFloatLayout:
    MDLabel:
        text: "Login"
        post_hint: {'center_y': 0.85}
        font_style: "H3"
        halign: "center"
        theme_text_color: "Custom"
        text_color: 0, 0, 0, 1
    MDLabel:
        text: "Welcome to Chatty"
        post_hint: {'center_y': 0.75}
        font_style: "H5"
        halign: "center"
        theme_text_color: "Custom"
        text_color: 0, 0, 0, 1
    MDTextField:
        id: username
        hint_text: "Enter your username"
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        current_hint_text_color: 0, 0, 0, 1
        size_hint_x: 0.8
    MDTextField:
        id: password
        hint_text: "Password"
        pos_hint: {'center_x': 0.5, 'center_y': 0.45}
        current_hint_text_color: 0, 0, 0, 1
        size_hint_x: 0.8
        password: True
 
"""

class Chatty(MDApp):

    def build(self):
        screen = Screen()
        self.theme_cls.primary_palette = "Red"


        button = MDRectangleFlatButton(text='Log In', pos_hint={'center_x': 0.5, 'center_y': 0.4},
                                       on_release=self.show_data)
        self.username = Builder.load_string((LoginPage))
        screen.add_widget(self.username)
        screen.add_widget(button)
        return screen

    def show_data(self, obj):
        if self.username.ids.username.text is "":
            check_string = 'Please enter a username'
        else:
            check_string = self.username.ids.username.text + ' does not exist'
        close_button = MDFlatButton(text='Close', on_release=self.close_dialog)
        self.dialog = MDDialog(title='Username Check',text=check_string,
                          size_hint=(0.7,1),
                          buttons=[close_button])
        self.dialog.open()

    def close_dialog(self,obj):
        self.dialog.dismiss()

Chatty().run()