'''
email address
username
online/offline
status
friend list
streak
interest with tags
stories
location
profile photos???
'''
from kivymd.app import MDApp
from kivy.lang import Builder

from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, ListProperty, ObjectProperty
from kivymd.theming import ThemableBehavior
from kivymd.uix.list import OneLineIconListItem, MDList


KV = '''
# Menu item in the DrawerList list.
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

    AnchorLayout:
        anchor_x: "left"
        size_hint_y: None
        height: avatar.height

        Image:
            id: avatar
            size_hint: None, None
            size: "56dp", "56dp"
            source: "data/logo/kivy-icon-256.png"

    MDLabel:
        text: "User Profile"
        font_style: "Button"
        size_hint_y: None
        height: self.texture_size[1]

    MDLabel:
        text: "nilaycicekli@gmail.com"
        font_style: "Caption"
        size_hint_y: None
        height: self.texture_size[1]

    ScrollView:

        DrawerList:
            id: md_list
            ItemDrawer:
                icon: "account-circle-outline"
                text: "User info"
                on_press:
                    root.screen_manager.current = "user_info"
            ItemDrawer:
                icon: "account-multiple-outline"
                text: "My friends"
                on_press:
                    root.screen_manager.current = "my_friends"
            ItemDrawer:
                icon: "bell-outline"
                text: "Notifications"
                on_press:
                    root.screen_manager.current = "notifications"
            ItemDrawer:
                icon: "account-cog-outline"
                text: "Settings"
                on_press:
                    root.screen_manager.current = "settings"
            ItemDrawer:
                icon: "camera-outline"
                text: "Stories"
                on_press:
                    root.screen_manager.current = "stories"
            ItemDrawer:
                icon: "map-marker-outline"
                text: "Find friends"
                on_press:
                    root.screen_manager.current = "find_friends"
            ItemDrawer:
                icon: "help-circle-outline"
                text: "Help"
                on_press:
                    root.screen_manager.current = "help"
            ItemDrawer:
                icon: "logout"
                text: "Log out"
                theme_text_color: "Custom"
                text_color: (234.0/255,35.0/255,0.0/255,1)
                on_press:
                    root.screen_manager.current = "logout"
                

Screen:
    BoxLayout:
        orientation: 'vertical'

        MDToolbar:
            id: toolbar
            pos_hint: {"top": 1}
            title: "Profile"
            elevation: 10
            left_action_items: [['menu', lambda x: nav_drawer.set_state('open')]]        
        Widget:
  

    NavigationLayout:
        x: toolbar.height

        ScreenManager:
            id: screen_manager

            Screen:
                name:"user_info"
                MDLabel:
                    text: "USER INFO"
                    halign: "center"
            Screen:
                name:"my_friends"
                MDLabel:
                    text: "MY FRIENDS"
                    halign: "center"
            Screen:
                name:"notifications"
                MDLabel:
                    text: "NOTIFICATIONS"
                    halign: "center"
            Screen:
                name:"settings"
                MDLabel:
                    text: "SETTINGS"
                    halign: "center"
            Screen:
                name:"stories"
                MDLabel:
                    text: "STORIES"
                    halign: "center"
            Screen:
                name:"find_friends"
                MDLabel:
                    text: "FIND FRIENDS"
                    halign: "center"
            Screen:
                name:"help"
                MDLabel:
                    text: "HELP"
                    halign: "center"
            Screen:
                name:"logout"
                MDLabel:
                    text: "LOGGED OUT. RETURN HOME PAGE. DELETE THIS PAGE LATER"
                    halign: "center"

        MDNavigationDrawer:
            id: nav_drawer

            ContentNavigationDrawer:
                id: content_drawer
                nav_drawer: nav_drawer
                screen_manager: screen_manager
'''


class ContentNavigationDrawer(BoxLayout):
    screen_manager = ObjectProperty()


class ItemDrawer(OneLineIconListItem):
    icon = StringProperty()
    text_color = ListProperty((0, 0, 0, 1))


class DrawerList(ThemableBehavior, MDList):
    def set_color_item(self, instance_item):
        """Called when tap on a menu item."""

        # Set the color of the icon and text for the menu item.
        for item in self.children:
            if item.text_color == self.theme_cls.primary_color:
                item.text_color = self.theme_cls.text_color
                break
        instance_item.text_color = self.theme_cls.primary_color


class ProfileView(MDApp):
    
    def build(self):
        self.theme_cls.primary_palette = "Orange"
        self.theme_cls.primary_hue ='600'
        self.theme_cls.theme_style="Light"
        return Builder.load_string(KV)


ProfileView().run()