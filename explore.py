import kivy
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout

from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivymd.uix.card import MDCard
from kivymd.uix.list import IRightBodyTouch

from kivy.clock import Clock
from kivymd.utils import asynckivy

from helpers import DrawerList, ContentNavigationDrawer, ItemDrawer

kivy.require("2.0.0")

explore_KV = '''
<ItemDrawer>:
    theme_text_color: "Custom"
    on_release: self.parent.set_color_item(self)
    on_press: lambda x: self.on_press()

    IconLeftWidget:
        id: icon
        icon: root.icon
        theme_text_color: "Custom"
        text_color: root.text_color

<ContentNavigationDrawer>:
    orientation: "vertical"
    padding: "8dp"
    spacing: "8dp"
    ScrollView:
        DrawerList:
            ItemDrawer:
                icon: "earth"
                text: "World Wide"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "scr 1"
            ItemDrawer:
                icon: "map-marker-outline"
                text: "My location"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "scr 2"

<UserCard>:
    orientation: "vertical"
    padding: '15dp'
    spacing: '20dp'
    pos_hint: {"center_x": .5, "center_y": .5}
    size_hint: 1,None
    size: "280dp", "210dp"
    radius: [15,15,15,15]
    TwoLineAvatarIconListItem:
        id: username
        text: "nilayc"
        secondary_text: 'happy'
        font_style: 'H6'
        size_hint_y: None
        IconLeftWidget:
            icon: "account-plus-outline"
            on_release: 
                root.add_friend()
        Container:
            id: container
          
            MDIcon:
                icon: "fire"
                theme_text_color: 'Custom'
                text_color: (234.0/255,35.0/255,0.0/255,1)
            MDLabel:
                text: '5'
                halign: 'center'
            

    MDLabel:
        id: bio
        text: 'Hello, im nilay. I take photos. I like smart and funny people. I like talking about countries. text me!'
        theme_text_color: 'Secondary'
        size_hint_y: .8
        size_hint_x: .9
        pos_hint: {"center_x": .5, "center_y": 1}
    MDLabel:
        id: tag
        text: 'tag1 tag2 tag3 tag4 tag5'
        theme_text_color: 'Secondary'
        size_hint_x: .9
        pos_hint: {"center_x": .5, "center_y": 1}



Screen:
    MDToolbar:
        id: toolbar
        halign: 'center'
        title: 'explore'
        md_bg_color: .2, .2, .2, 1
        specific_text_color: 1, 1, 1, 1
        pos_hint: {"top": 1}
        left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]
    NavigationLayout:
        x: toolbar.height
        ScreenManager:
            id: screen_manager
            Screen:
                name: 'scr 1'
                MDScrollViewRefreshLayout:
                    id: refresh_layout
                    refresh_callback: app.refresh_callback
                    root_layout: root
                    size_hint: (1, .90)
                    MDGridLayout:
                        id: layout
                        cols: 2
                        spacing: 50
                        adaptive_height: True
                        padding: 50
                        md_bg_color : (39.0/255,41.0/255,43.0/255,1)
            Screen:
                name: 'scr 2'
                MDScrollViewRefreshLayout:
                    id: refresh_layout2
                    refresh_callback: app.refresh_callback_loc
                    root_layout: root
                    size_hint: (1, .90)
                    MDGridLayout:
                        id: layout2
                        cols: 2
                        spacing: 50
                        adaptive_height: True
                        padding: 50
                        md_bg_color : (39.0/255,41.0/255,43.0/255,1)

        MDNavigationDrawer:
            id: nav_drawer

            ContentNavigationDrawer:
                screen_manager: screen_manager
                nav_drawer: nav_drawer
            
           
           
'''

class UserCard(MDCard):
    def add_friend(self):
        close_button = MDFlatButton(text="close",on_release= self.close_dialog)
        more_button = MDFlatButton(text="more")
        self.dialog = MDDialog(title="Message Sent", text='Keep Exploring!', size_hint=(0.7,1),buttons=[close_button,more_button])
        self.dialog.open()
        print("Friend Added")
        #print(self.username.text)
    
    def close_dialog(self,obj):
        self.dialog.dismiss()

class Container(IRightBodyTouch, MDBoxLayout):
    adaptive_width = True


class Explore(MDApp):
    screen = None
    def build(self):

        #theme
        self.theme_cls.primary_palette = "Gray"
        self.theme_cls.primary_hue ='200'
        self.theme_cls.theme_style="Light"
        
        self.screen = Builder.load_string(explore_KV)

        self.set_list()
        self.set_list_loc()
        
        return self.screen

    def set_list(self):
        async def set_list():
            for i in range(20):
                await asynckivy.sleep(0)
                userbox = UserCard()
                userbox.ids.username.text = f'username {i}'
                self.screen.ids.layout.add_widget(userbox)
        asynckivy.start(set_list())

    def set_list_loc(self):
        async def set_list_loc():
            for i in range(20):
                await asynckivy.sleep(0)
                userbox = UserCard()
                userbox.ids.username.text = f'usernameloc {i}'
                self.screen.ids.layout2.add_widget(userbox)
        asynckivy.start(set_list_loc())
      

    def refresh_callback(self, *args,**kwargs):
        '''A method that updates the state of your application
        while the spinner remains on the screen.'''

        def refresh_callback(interval):
            self.screen.ids.layout.clear_widgets()
            self.set_list()
            self.screen.ids.refresh_layout.refresh_done()
            self.tick = 0

        Clock.schedule_once(refresh_callback, 1)

    def refresh_callback_loc(self, *args,**kwargs):
        '''A method that updates the state of your application
        while the spinner remains on the screen.'''

        def refresh_callback_loc(interval):
            self.screen.ids.layout2.clear_widgets()
            self.set_list_loc()
            self.screen.ids.refresh_layout2.refresh_done()
            self.tick = 0

        Clock.schedule_once(refresh_callback_loc, 1)

    

if __name__ == '__main__':
    Explore().run()
