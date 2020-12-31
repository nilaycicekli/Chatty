# python3 version 3.7.9
# pip3 version 20.1.1
# interpreter python 3.7
# kivy => pip install kivy
# kivyMD => pip install kivy
# run

import kivy
from kivy.lang import Builder
from kivymd.app import MDApp

from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
kivy.require("2.0.0")

KV = '''

<UserBox>:
    orientation: 'vertical'
    padding: 20
    spacing: 30
    adaptive_height: True
    radius: [10,10,10,10]
    md_bg_color: (245.0/255,245.0/255,245.0/255,1) 

    MDLabel:
        id: username
        text: "username"
        halign: 'center'
        font_style: 'Caption'
        theme_text_color: 'Primary'
        font_style: "Button"
    
    MDLabel:
        id: bio
        text: "bio"
        halign: 'center'
        font_style: 'Caption'
    
    MDBoxLayout:
        radius: [25, 25,25, 25]
        MDIcon:
            icon: 'fire'
            halign: 'right'
            valign: 'center'
            size_hint: (.25,1)
            theme_text_color: 'Custom'
            text_color: (234.0/255,35.0/255,0.0/255,1)
        MDLabel:
            id: streak
            text: 'streak number'
            halign: 'left'
            valign: 'center'
            size_hint: (.25,1)
            font_style: 'Caption'
            theme_text_color: 'Primary'
        MDIconButton:
            icon: 'plus-circle'
            theme_text_color: 'Custom' 
            text_color: (27.0/255,71.0/255,117.0/255,1)
            pos_hint: {'center_x':1,'center_y':0.2}
            on_release: 
                root.add_friend()


Screen:
    ScrollView:
        size_hint: (1, None)
        size: (root.width, root.height)
        MDGridLayout:
            id: layout
            cols: 2
            spacing: 50
            adaptive_height: True
            padding: 50
            md_bg_color : (39.0/255,41.0/255,43.0/255,1)
           
'''


class UserBox(MDBoxLayout):

    def add_friend(self):
        close_button = MDFlatButton(text="close",on_release= self.close_dialog)
        more_button = MDFlatButton(text="more")
        self.dialog = MDDialog(title="Message Sent", text='Keep Exploring!', size_hint=(0.7,1),buttons=[close_button,more_button])
        self.dialog.open()
        print("Friend Added")
        #print(self.username.text)
    
    def close_dialog(self,obj):
        self.dialog.dismiss()


class Explore(MDApp):
    def build(self):

        #theme
        self.theme_cls.primary_palette = "Gray"
        self.theme_cls.primary_hue ='200'
        self.theme_cls.theme_style="Light"
        
        screen = Builder.load_string(KV)

        for i in range(20):
            userbox = UserBox()
            userbox.ids.username.text = f'username {i}'
            screen.ids.layout.add_widget(userbox)
        
        return screen



if __name__ == '__main__':
    Explore().run()
