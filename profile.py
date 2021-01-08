'''
email address
username
online/offline
status
friend list
streak
interest with tags
location
'''


from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.clock import Clock

from kivy.network.urlrequest import UrlRequest
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, ListProperty, ObjectProperty
from kivymd.theming import ThemableBehavior
from kivymd.uix.list import OneLineIconListItem, MDList
from kivymd.uix.chip import MDChip
from kivymd.toast import toast

from kivymd.uix.menu import MDDropdownMenu

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

import datetime

# Use the application default credentials
cred = credentials.Certificate('Chatty/chatty-y-firebase-adminsdk-zb1ow-7b79045fa0.json')
default_app = firebase_admin.initialize_app(cred)

# initialize firestore
db = firestore.client() 

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


class ProfileView(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen = Builder.load_string(profile_KV)
        self.username = "nilay"
        self.user_ref = db.collection(u'users').document(self.username)
        self.user = self.get_by_username(self.username)
        self.screen.ids.username.text = self.username
        self.screen.ids.fname.text = self.user['fname']
        self.screen.ids.lname.text = self.user['lname']
        self.screen.ids.email.text = self.user['email']
        self.screen.ids.status.text = self.user['status']
        self.screen.ids.bio.text = self.user['bio']
        self.screen.ids.streak.secondary_text = str(self.user['streak'])
        # self.screen.ids.location.secondary_text = self.user['city']
        self.screen.ids.location.secondary_text = "istanbul"
        for t in self.user['tags']:
            self.screen.ids.tag_box.add_widget(TagChip(label=t,icon="coffee"))
    
    def set_item(self, instance):
        def set_item(interval):
            self.screen.ids.status.text = instance.text
        Clock.schedule_once(set_item, 0.3)

    def set_item_tag(self, instance):
        def set_item_tag(interval):
            self.screen.ids.tags.text = instance.text
        Clock.schedule_once(set_item_tag, 0.3)

    def build(self):
        menu_items = [{"icon_right": None, "text": "online"},
        {"icon": "mail", "text": "offline"},
        {"icon": "email", "text": "happy"},
        {"icon": "git", "text": "sad"},
        {"icon": "git", "text": "away"},]
        self.menu = MDDropdownMenu(
            caller=self.screen.ids.status,
            items=menu_items,
            position="bottom",
            callback=self.set_item,
            width_mult=3,
        )

        tag_menu_items = [{"text": "coffee"},
        { "text": "coding"},
        {"text": "chilling"},
        {"text": "dancing"},
        {"text": "music"},]
        self.tag_menu = MDDropdownMenu(
            caller=self.screen.ids.tags,
            items=tag_menu_items,
            position="bottom",
            callback=self.set_item_tag,
            width_mult=3,
        )
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.primary_hue ='600'
        self.theme_cls.theme_style="Light"
        
        return self.screen

    # edit profile info
    def update_profile(self,**kwargs):
        print(kwargs)
        user_ref = db.collection(u'users').document(kwargs['username'])
        user_ref.update(kwargs)
        user_ref.update({
            u'timestamp': firestore.SERVER_TIMESTAMP
        })
        toast("updated!")
        
    def new_tag(self):
        tag = self.screen.ids.tags.text
        if len(self.user['tags']) >= 4:
                toast("you can have 4 tags at most :( ")
                return
        if tag:
            self.screen.ids.tag_box.add_widget(TagChip(label=tag,icon="coffee"))
            self.user['tags'].append(tag)
            self.tag_add([tag])
        else:
            toast("type something!")
    
    def hey(self):
        toast("hey")


#####################DATABASE##################
    # get user info
    def get_by_username(self, username):
        doc = db.collection(u'users').where(u'username', u'==',username).stream()
        for d in doc:
            return d.to_dict()

    def tag_add(self,tags):
        user_ref = db.collection(u'users').document(self.username)

        # Atomically add a new tag to the 'tags' array field. you can add multiple.
        user_ref.update({u'tags': firestore.ArrayUnion(tags)})

        user_ref.update({
            u'timestamp': firestore.SERVER_TIMESTAMP
        })

    def tag_remove(self,instance,value):
    #  remove a tag from the 'tags' array field.
        self.screen.ids.tag_box.remove_widget(instance)
        self.user['tags'].remove(value)
        self.user_ref.update({u'tags': firestore.ArrayRemove([value])})
        
        self.user_ref.update({
            u'timestamp': firestore.SERVER_TIMESTAMP
        })
        toast(f"{value} removed")



ProfileView().run()
