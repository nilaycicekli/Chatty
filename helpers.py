from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivy.properties import StringProperty, ListProperty, ObjectProperty
from kivymd.uix.list import OneLineIconListItem, MDList, OneLineAvatarIconListItem
from kivymd.theming import ThemableBehavior
from kivymd.uix.chip import MDChip
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.card import MDCard
from kivymd.uix.list import IRightBodyTouch
from kivymd.toast import toast





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
                    # root.manager.current = "welcomescreen"
                    app.logout()
                

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
                            text: "nilay"
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
# the whole chat screen.
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
                        msg_log: msg_log    
                        MDGridLayout:
                            rows: 2
                            MDGridLayout:
                                cols: 1
                                rows: 0
                                ScrollView:
                                    size: self.size
                                    do_scroll_x: False
                                    MDLabel:
                                        id: msg_log
                                        text_size: self.width,None
                                        size_hint_y: None
                                        height: self.texture_size[1]
                                        font_size: root.height / 30
                    GridLayout:
                        size_hint_y: 0.1
                        cols: 3
                        rows: 1
                        AnchorLayout:
                            TextInput:
                                id: input
                                hint_text: 'message...'
                                on_text_validate: 
                                    app.send_message(input.text)
                                    input.text=""
                                multiline: False
                        AnchorLayout:
                            size_hint: (0.1,0)
                            anchor_x: 'center'
                            Button:
                                text: 'send'
                                on_release: 
                                    app.send_message(input.text)
                                    input.text=""
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
                            ScrollView:
                                MDList:
                                    id: privatelist
                        GroupWindow:
                            name: "group_window"
                            ScrollView:
                                MDList:
                                    id: grouplist
                        FriendList:
                            name: "friends_window"
                            ScrollView:
                                MDList:
                                    id: friendlist
                            
<PrivateWindow>:
    MDLabel:
        halign: 'center'
<GroupWindow>:
    MDLabel:
        halign: 'center'
<FriendList>:
    MDLabel:
        halign: 'center'     

<FriendItem>:
    id: frienditem
    text: ""
    font_style: 'H6'
    size_hint_y: None
    IconLeftWidget:
        icon: "account-minus-outline"
        on_release: 
            root.delete_friend()
            app.delete_friend(frienditem)                                    
"""
class FriendItem(OneLineAvatarIconListItem):
    def delete_friend(self):
        toast(self.text+" removed from friends")
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


# explore page
explore_KV = '''
<ItemDrawerExplore>:
    theme_text_color: "Custom"
    on_release: self.parent.set_color_item(self)
    on_press: lambda x: self.on_press()

    IconLeftWidget:
        id: icon
        icon: root.icon
        theme_text_color: "Custom"
        text_color: root.text_color

<ContentNavigationDrawerExplore>:
    orientation: "vertical"
    padding: "8dp"
    spacing: "8dp"
    ScrollView:
        DrawerList:
            id: md_list_explore_menu_items
            ItemDrawerExplore:
                icon: "earth"
                text: "World Wide"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "scr 1"
            ItemDrawerExplore:
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
                app.add_friend(username.text)
        Container:
            id: container
          
            MDIcon:
                icon: "fire"
                theme_text_color: 'Custom'
                text_color: (234.0/255,35.0/255,0.0/255,1)
            MDLabel:
                id: streak
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

            ContentNavigationDrawerExplore:
                screen_manager: screen_manager
                nav_drawer: nav_drawer
                    
'''
class ContentNavigationDrawerExplore(BoxLayout):
    screen_manager = ObjectProperty()

class UserCard(MDCard):
    def add_friend(self):
        close_button = MDFlatButton(text="close",on_release= self.close_dialog)
        more_button = MDFlatButton(text="more")
        self.dialog = MDDialog(title="Friend Added", text='Message sent. You can keep exploring!', size_hint=(0.7,1),buttons=[close_button,more_button])
        self.dialog.open()
        print("Friend Added")
        
        #print(self.username.text)
    
    def close_dialog(self,obj):
        self.dialog.dismiss()

class Container(IRightBodyTouch, MDBoxLayout):
    adaptive_width = True


class ItemDrawerExplore(OneLineIconListItem):
    icon = StringProperty()
    text_color = ListProperty((0, 0, 0, 1))

# login and register
login_KV = '''
<WelcomeScreen>:
    name:'welcomescreen'
    MDLabel:
        text:'Login'
        font_style:'H2'
        halign:'center'
        pos_hint: {'center_y':0.9}
    MDLabel:
        text:'&'
        font_style:'H2'
        halign:'center'
        pos_hint: {'center_y':0.7}
    MDLabel:
        text:'Signup'
        font_style:'H2'
        halign:'center'
        pos_hint: {'center_y':0.5}
    MDRaisedButton:
        text:'Login'
        pos_hint : {'center_x':0.4,'center_y':0.3}
        size_hint: (0.13,0.1)
        on_press: 
            root.manager.current = 'loginscreen'
            root.manager.transition.direction = 'left'
    MDRaisedButton:
        text:'Signup'
        pos_hint : {'center_x':0.6,'center_y':0.3}
        size_hint: (0.13,0.1)
        on_press:
            root.manager.current = 'signupscreen'
            root.manager.transition.direction = 'left'
        
<LoginScreen>:
    name:'loginscreen'
    MDLabel:
        text:'Login'
        font_style:'H2'
        halign:'center'
        pos_hint: {'center_y':0.9}
    MDTextField:
        id: login_email
        pos_hint: {'center_y':0.6,'center_x':0.5}
        size_hint : (0.7,0.1)
        hint_text: 'Email'
        helper_text:'Required'
        helper_text_mode:  'on_error'
        icon_right: 'account'
        icon_right_color: app.theme_cls.primary_color
        required: True
        mode: "rectangle"
    MDTextField:
        id:login_password
        pos_hint: {'center_y':0.4,'center_x':0.5}
        size_hint : (0.7,0.1)
        hint_text: 'Password'
        helper_text:'Required'
        helper_text_mode:  'on_error'
        icon_right: 'account'
        icon_right_color: app.theme_cls.primary_color
        required: True
        mode: "rectangle"
    MDRaisedButton:
        text:'Login'
        size_hint: (0.13,0.07)
        pos_hint: {'center_x':0.5,'center_y':0.2}
        on_press:
            app.login()
            app.after_login()
            root.manager.current = 'myscreen'

            
        
    MDTextButton:
        text: 'Create an account'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press:
            root.manager.current = 'signupscreen'
            root.manager.transition.direction = 'up'
<SignupScreen>:
    name:'signupscreen'
    MDLabel:
        text:'Signup'
        font_style:'H2'
        halign:'center'
        pos_hint: {'center_y':0.9}
    MDTextField:
        id:signup_email
        pos_hint: {'center_y':0.6,'center_x':0.5}
        size_hint : (0.7,0.1)
        hint_text: 'Email'
        helper_text:'Required'
        helper_text_mode:  'on_error'
        icon_right: 'account'
        icon_right_color: app.theme_cls.primary_color
        required: True
        mode: "rectangle"
        text:''
    MDTextField:
        id:signup_username
        pos_hint: {'center_y':0.75,'center_x':0.5}
        size_hint : (0.7,0.1)
        hint_text: 'Username'
        helper_text:'Required'
        helper_text_mode:  'on_error'
        icon_right: 'account'
        icon_right_color: app.theme_cls.primary_color
        required: True
        text:''
    MDTextField:
        id:signup_password
        pos_hint: {'center_y':0.4,'center_x':0.5}
        size_hint : (0.7,0.1)
        hint_text: 'Password'
        helper_text:'Required'
        helper_text_mode:  'on_error'
        icon_right: 'account'
        icon_right_color: app.theme_cls.primary_color
        required: True
        mode: "rectangle"
        min_length: 6
        text:''
    MDRaisedButton:
        text:'Signup'
        size_hint: (0.13,0.07)
        pos_hint: {'center_x':0.5,'center_y':0.2}
        on_press: app.signup()
    MDTextButton:
        text: 'Already have an account'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press:
            root.manager.current = 'loginscreen'
            root.manager.transition.direction = 'down'

<MainScreen>:
    name: 'mainscreen'
    BoxLayout:
        orientation: 'vertical'
        # MDToolbar:
        #     halign: 'center'
        #     title: 'Chatty'
        #     md_bg_color: .2, .2, .2, 1
        #     specific_text_color: 1, 1, 1, 1
            
        MDBottomNavigation:
            panel_color: .2, .2, .2, 1
            
            MDBottomNavigationItem:
                name: 'screen 1'
                id: explorescreen
                text:"hey"
    
            MDBottomNavigationItem:
                name: 'screen 2'
                id: chatscreen
    
            MDBottomNavigationItem:
                name: 'screen 3'
                id: profilescreen

Screen:
    manager: main_screen_manager
    ScreenManager:
        id: main_screen_manager
        WelcomeScreen:
            id: welcomescreen
        LoginScreen:
            id: loginscreen
        SignupScreen:
            id: signupscreen
        MainScreen:
            id: mainscreen


'''


class WelcomeScreen(Screen):
    pass
class MainScreen(Screen):
    pass
class LoginScreen(Screen):
    pass
class SignupScreen(Screen):
    pass




