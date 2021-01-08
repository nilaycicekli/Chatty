from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivy.properties import StringProperty, ListProperty, ObjectProperty
from kivymd.uix.list import OneLineIconListItem, MDList
from kivymd.theming import ThemableBehavior
from kivymd.uix.chip import MDChip
from kivy.uix.screenmanager import Screen, ScreenManager



profile_KV = '''
<TagChip>:
    callback: app.tag_remove
    icon: ""
    pos_hint: {'center_y':0.5}
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
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "user_info"
            ItemDrawer:
                icon: "account-multiple-outline"
                text: "My friends"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "my_friends"
            ItemDrawer:
                icon: "account-cog-outline"
                text: "Settings"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "settings"
            ItemDrawer:
                icon: "help-circle-outline"
                text: "Help"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "help"
            ItemDrawer:
                icon: "logout"
                text: "Log out"
                theme_text_color: "Custom"
                text_color: (234.0/255,35.0/255,0.0/255,1)
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "logout"
                

Screen:

    MDToolbar:
        id: toolbar
        pos_hint: {"top": 1}
        title: "Profile"
        elevation: 10
        left_action_items: [['menu', lambda x: nav_drawer.set_state('open')]]  
  

    NavigationLayout:
        x: toolbar.height

        ScreenManager:
            id: screen_manager

            Screen:
                name:"user_info"
                MDBoxLayout:
                    orientation: 'vertical'
                    spacing: 12
                    padding: 60
                    size_hint_y: 0.98
                    MDBoxLayout:
                        spacing: 30
                        MDTextField:
                            id: username
                            text: "john"
                            hint_text: "username"
                            helper_text: "edit your username"
                            helper_text_mode: "on_focus"
                            required: True
                            max_text_length: 20
                            color_mode: 'custom' 
                            icon_right: 'account-outline'
                            disabled: True
                        MDTextField:
                            id: status
                            size_hint_x: None
                            text: ""
                            hint_text: "status"
                            helper_text: "how you feel"
                            helper_text_mode: "on_focus"
                            color_mode: 'custom' 
                            icon_right: 'face'
                            on_focus: if self.focus: app.menu.open()
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
                    MDTextField:
                        id: bio
                        text: "Hello this is my bio"
                        hint_text: "bio"
                        helper_text: "tell us about yourself"
                        helper_text_mode: "on_focus"
                        max_text_length: 150
                        color_mode: 'custom' 
                        icon_right: 'comment-edit-outline'
                        multiline: True
                    MDRaisedButton:
                        text: "Save"
                        md_bg_color: (52.0/255,142.0/255,201.0/255,1) 
                        pos_hint: {'center_x':0.93,'center_y':1}
                        on_release: app.update_profile(username=username.text,status=status.text,fname=fname.text,lname=lname.text,email=email.text,bio=bio.text)
                    MDBoxLayout:
                        id: tag_box
                        spacing: 15
                        MDTextField:
                            id: tags
                            size_hint_x: None
                            text: ""
                            hint_text: "tag"
                            helper_text: "find your peers"
                            helper_text_mode: "on_focus"
                            color_mode: 'custom' 
                            icon_right: 'label-outline'
                            on_focus: if self.focus: app.tag_menu.open()
                        MDIconButton:
                            icon: 'plus-circle'
                            theme_text_color: 'Custom' 
                            text_color: (27.0/255,71.0/255,117.0/255,1)
                            on_release: 
                                app.new_tag()
                    MDBoxLayout:
                        size_hint_y: 0.8
                        TwoLineIconListItem:
                            id: location
                            text: "Location"
                            secondary_text: "Istanbul,TR"
                            on_release: app.hey()

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

class TagChip(MDChip):
    pass

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

chat_KV = """
# the whole screen.
Screen:
    window_manager: window_manager
    NavigationLayout:
        ScreenManager:
            
            # this is out chat screen.
            Screen:
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: "chat"
                        left_action_items: [["menu", lambda x: nav_drawer.set_state()]]
                        elevation: 5
                    Screen:    
                        MDLabel:
                            text: 'messaging here!'
                            halign: 'center'
                    GridLayout:
                        size_hint_y: 0.1
                        cols: 3
                        rows: 1
                        AnchorLayout:
                            TextInput:
                                id: input
                                hint_text: 'message...'
                        AnchorLayout:
                            size_hint: (0.1,0)
                            anchor_x: 'center'
                            Button:
                                text: 'send'
                        AnchorLayout:
                            size_hint: (0.1,0)
                            anchor_x: 'center'
                            Button:
                                text: 'media'
                            
                
                            
# this is the panel that pops out of the left                   
        MDNavigationDrawer:
            id: nav_drawer

            MDScreen:
                BoxLayout:
                    orientation: 'vertical'
                    # choose chat list (personal/private)
                    
                    BoxLayout:
                        orientation: 'horizontal'
                        size_hint_y: 0.1
                        padding: 8
                        
                        Button:
                            text: 'friends'
                            on_press:
                                root.window_manager.current = "friends_window"
                        Button:
                            text: 'private'
                            on_press:
                                root.window_manager.current = "private_window"
                        Button:
                            on_press:
                                root.window_manager.current = "group_window"
                            text: 'group'
                            
                    WindowManager:
                        id: window_manager
                        PrivateWindow:
                            name: "private_window"
                        GroupWindow:
                            name: "group_window"
                        FriendList:
                            name: "friends_window"
                            
<PrivateWindow>:
    MDLabel:
        text: 'it works but wont switch!'
        halign: 'center'
<GroupWindow>:
    MDLabel:
        text: 'it works!'
        halign: 'center'
<FriendList>:
    MDLabel:
        text: 'it works!'
        halign: 'center'                                         
"""

# private-chats.
class PrivateWindow(Screen):
    pass
# group-chats.
class GroupWindow(Screen):
    pass
# friends-list.
class FriendList(Screen):
    pass
# enables the screen manager to work.
class WindowManager(ScreenManager):
    pass