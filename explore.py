import kivy
from kivy.app import runTouchApp
from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.screen import Screen
from kivy.uix.scrollview import ScrollView
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDFlatButton, MDIconButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.label import MDLabel, MDIcon
from kivymd.font_definitions import theme_font_styles
from kivy.core.window import Window
#from helpers import username_helper


kivy.require("2.0.0")

# Window.clearcolor=(1,1,1,1) # color white 
Window.size=(700,600) # fixed size
#Window.size=(360,600) # mobile ratio

class Chatty(MDApp):
    
    def build(self):
        #theme
        self.theme_cls.primary_palette = "Gray"
        self.theme_cls.primary_hue ='200'
        self.theme_cls.theme_style="Light"

        # screen 
        screen = Screen()

         # scroll view
        scroll = ScrollView(size_hint=(1, None), size=(Window.width, Window.height))
        
        # grid layout with 2 columns
        layout = MDGridLayout(cols=2, spacing=50,  adaptive_height= True, padding=50,
        md_bg_color = (39.0/255,41.0/255,43.0/255,1))
        # Make sure the height is such that there is something to scroll.
        #layout.bind(minimum_height=layout.setter('height'))

        # add layout into root
        scroll.add_widget(layout)

        # add root into screen
        screen.add_widget(scroll)
   
        for i in range(40):

            # user box layout
            user_box = MDBoxLayout(orientation='vertical',padding=20,spacing=30,adaptive_height= True, radius=[10,10,10,10],
    md_bg_color =(245.0/255,245.0/255,245.0/255,1) )


            # fields to display in user box
            label_username = MDLabel(text=f"username {i}", halign= 'center',theme_text_color='Primary',font_style="Button")
            label_user_bio = MDLabel(text="hello, text me. ok?", font_style="Caption", halign= 'center')


            # streak box layout
            streak_box = MDBoxLayout(radius= [25, 25,25, 25])

            # streak icon and number of days
            icon_streak = MDIcon(icon='fire', halign="right", valign= 'center',size_hint=(.25,1), theme_text_color= "Custom", text_color=(234.0/255,35.0/255,0.0/255,1))  
            label_streak = MDLabel(text=f"{i}",halign="left", valign= 'center',size_hint=(.25,1),font_style="Caption",theme_text_color='Primary')
            
            # add friend button
            add_btn = MDIconButton(icon="plus-circle", theme_text_color= "Custom", text_color=(27.0/255,71.0/255,117.0/255,1),
            pos_hint={'center_x':1,'center_y':0.2},on_release=self.add_friend,size_hint=(.5,1))

            # add fields in the streak box
            streak_box.add_widget(icon_streak)
            streak_box.add_widget(label_streak)
            streak_box.add_widget(add_btn)

            # add fields in the user box
            user_box.add_widget(label_username)
            user_box.add_widget(label_user_bio)
            user_box.add_widget(streak_box)

            # add user box in the layout
            layout.add_widget(user_box)

        # return the main parent
        runTouchApp(screen)

    def add_friend(self,obj):
        close_button = MDFlatButton(text="close",on_release= self.close_dialog)
        more_button = MDFlatButton(text="more")
        self.dialog = MDDialog(title="Message Sent", text='Keep Exploring!', size_hint=(0.7,1),buttons=[close_button,more_button])
        self.dialog.open()
        print("Friend Added")
        #print(self.username.text)
    
    def close_dialog(self,obj):
        self.dialog.dismiss()
       
if __name__ == '__main__':
    Chatty().run()
