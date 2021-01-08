from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivy.properties import StringProperty, ListProperty, ObjectProperty
from kivymd.uix.list import OneLineIconListItem, MDList
from kivymd.theming import ThemableBehavior
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
                icon: "account-cog-outline"
                text: "Settings"
                on_press:
                    root.screen_manager.current = "settings"
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
                MDBoxLayout:
                    orientation: 'vertical'
                    spacing: 40
                    padding: 80
                    size_hint_y: 0.93
                    MDTextField:
                        id: username
                        text: "ncicekli"
                        hint_text: "username"
                        helper_text: "edit your username"
                        helper_text_mode: "on_focus"
                        required: True
                        max_text_length: 20
                        color_mode: 'custom' 
                        icon_right: 'account-outline'
                    MDBoxLayout:
                        spacing: 30
                        MDTextField:
                            id: fname
                            text: "Nilay"
                            hint_text: "first name"
                            helper_text: "edit your first name"
                            helper_text_mode: "on_focus"
                            max_text_length: 20
                            color_mode: 'custom' 
                            icon_right: 'pencil-outline'
                        MDTextField:
                            id: lname
                            text: "Cicekli"
                            hint_text: "last name"
                            helper_text: "edit your last name"
                            helper_text_mode: "on_focus"
                            max_text_length: 30
                            color_mode: 'custom' 
                            icon_right: 'pencil-outline'
                    MDTextField:
                        id: email
                        text: "ncicekli@gmail.com"
                        hint_text: "email"
                        helper_text: "edit your email"
                        helper_text_mode: "on_focus"
                        required: True
                        max_text_length: 50
                        color_mode: 'custom' 
                        icon_right: 'email-outline'
                    MDRaisedButton:
                        text: "Save"
                        md_bg_color: (52.0/255,142.0/255,201.0/255,1) 
                        pos_hint: {'center_x':0.93,'center_y':1}
                    MDBoxLayout:
                        TwoLineIconListItem:
                            id: location
                            text: "Location"
                            secondary_text: "Istanbul,TR"

                            IconLeftWidget:
                                icon: "map-marker-outline"
                                theme_text_color: 'Custom'
                                text_color: (234.0/255,35.0/255,0.0/255,1)
                        TwoLineIconListItem:
                            id: streak
                            text: "Streak"
                            secondary_text: "26"

                            IconLeftWidget:
                                icon: "fire"
                                theme_text_color: 'Custom'
                                text_color: (234.0/255,35.0/255,0.0/255,1)
            Screen:
                name:"my_friends"
                MDLabel:
                    text: "MY FRIENDS"
                    halign: "center"
            Screen:
                name:"settings"
                MDLabel:
                    text: "SETTINGS"
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