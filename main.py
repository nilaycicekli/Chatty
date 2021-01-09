# python3 version 3.7.9
# pip3 version 20.1.1
# interpreter python 3.7
# kivy => pip install kivy
# kivyMD => pip install kivy
# run

import kivy
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.clock import Clock
from kivy.network.urlrequest import UrlRequest
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivy.properties import StringProperty, ListProperty, ObjectProperty
from kivymd.theming import ThemableBehavior
from kivymd.uix.list import OneLineIconListItem, MDList, OneLineListItem, TwoLineAvatarIconListItem , IconLeftWidget, OneLineAvatarIconListItem
from kivymd.uix.chip import MDChip
from kivymd.toast import toast
from kivymd.utils import asynckivy
from kivymd.uix.menu import MDDropdownMenu

import datetime
import json
import random
import requests




# for profile
from helpers import profile_KV, TagChip

# for chat page
from helpers import chat_KV, PrivateWindow, GroupWindow, FriendList, WindowManager, FriendItem

# for explore
from helpers import explore_KV, UserCard, Container

# for explore
from helpers import login_KV, WelcomeScreen, MainScreen, LoginScreen, SignupScreen

import socket,threading

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from firebase_admin import auth
# Use the application default credentials
cred = credentials.Certificate('Chatty/chatty-y-firebase-adminsdk-zb1ow-7b79045fa0.json')
default_app = firebase_admin.initialize_app(cred)

# initialize firestore
db = firestore.client() 
kivy.require("2.0.0")

############

global s
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "127.0.0.1";port = 5005
#######

# bottom navigation - main screen - the tab structure
screen_helper = """

<MyScreen>:
    name: 'myscreen'
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
    
            MDBottomNavigationItem:
                name: 'screen 2'
                id: chatscreen
    
            MDBottomNavigationItem:
                name: 'screen 3'
                id: profilescreen

MyScreen:

"""
class MyScreen(Screen):
    pass

sm = ScreenManager()
sm.add_widget(PrivateWindow(name='private'))
sm.add_widget(GroupWindow(name='group'))
sm.add_widget(FriendList(name='friends'))

sm.add_widget(WelcomeScreen(name = 'welcomescreen'))
sm.add_widget(MainScreen(name = 'mainscreen'))
sm.add_widget(LoginScreen(name = 'loginscreen'))
sm.add_widget(SignupScreen(name = 'signupscreen'))

sm.add_widget(MyScreen(name = 'myscreen'))




class Chatty(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # profile screen
        self.profilescreen = Builder.load_string(profile_KV)
        self.username = ""
        # self.user_ref = db.collection(u'users').document(self.username)
        # self.user = self.get_by_username(self.username)
        # self.profilescreen.ids.username.text = self.username
        # self.profilescreen.ids.fname.text = self.user['fname']
        # self.profilescreen.ids.lname.text = self.user['lname']
        # self.profilescreen.ids.email.text = self.user['email']
        # self.profilescreen.ids.status.text = self.user['status']
        # self.profilescreen.ids.bio.text = self.user['bio']
        # self.profilescreen.ids.streak.secondary_text = str(self.user['streak'])
        # # self.profilescreen.ids.location.secondary_text = self.user['city']
        # self.profilescreen.ids.location.secondary_text = "istanbul"
        # for t in self.user['tags']:
        #     self.profilescreen.ids.tag_box.add_widget(TagChip(label=t,icon="coffee"))
        # end profile screen

    def build(self):
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.primary_hue ='600'
        self.theme_cls.theme_style="Light"
        self.screen = Builder.load_string(screen_helper)

        # build for profile screen
        menu_items = [{ "text": "online"},
        {"text": "offline"},
        { "text": "happy"},
        { "text": "sad"},
        {"text": "away"},]

        self.menu = MDDropdownMenu(
            caller=self.profilescreen.ids.status,
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
            caller=self.profilescreen.ids.tags,
            items=tag_menu_items,
            position="bottom",
            callback=self.set_item_tag,
            width_mult=3,
        )
        # self.screen.ids.profilescreen.add_widget(self.profilescreen)
        # end build for profile screen


        # build for chat page
        self.chatscreen = Builder.load_string(chat_KV)
        
        # end build for chat page

        # build for explore page
        self.explorescreen = Builder.load_string(explore_KV)
        # self.friend_match_arr =  self.tag_match(self.user['tags'])
        # if len(self.friend_match_arr) < 3:
        #     self.friend_match_arr += self.get_all()

        # self.set_list()
        # self.set_list_loc()

        # self.screen.ids.explorescreen.add_widget(self.explorescreen)
        # end build for explore page

        # build for login and register
        self.startscreen = Builder.load_string(login_KV)
        self.url  = "https://chatty-y.firebaseio.com/.json"
        self.startscreen.manager.add_widget(self.screen)
        # self.startscreen.manager.current = 'loginscreen'
        # end build for login and register


        return self.startscreen

    # functions for profile screen
    def set_item(self, instance):
        def set_item(interval):
            self.profilescreen.ids.status.text = instance.text
        Clock.schedule_once(set_item, 0.3)

    def set_item_tag(self, instance):
        def set_item_tag(interval):
            self.profilescreen.ids.tags.text = instance.text
        Clock.schedule_once(set_item_tag, 0.3)

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
        tag = self.profilescreen.ids.tags.text
        if len(self.user['tags']) >= 4:
                toast("you can have 4 tags at most :( ")
                return
        if(tag in self.user['tags']):
                toast("you already have this one.")
                return
        if tag:
            self.profilescreen.ids.tag_box.add_widget(TagChip(label=tag,icon="coffee"))
            self.user['tags'].append(tag)
            self.tag_add([tag])
        else:
            toast("type something!")
    
    def hey(self):
        toast("hey")
    # end functions for profile


    # functions for explore
    def set_list(self):
        self.user = self.get_by_username(self.username)
        self.friend_match_arr =  self.tag_match(self.user['tags'])
        self.friends = self.user['friends']
        for u in self.friend_match_arr:
            if u['username']==self.username: 
                self.friend_match_arr.remove(u)
            if u['username'] in self.friends: 
                self.friend_match_arr.remove(u)

        if len(self.friend_match_arr) < 3:
            self.friend_match_arr += self.get_all()
            for u in self.friend_match_arr:
                if u['username']==self.username: 
                    self.friend_match_arr.remove(u)
                if u['username'] in self.friends: 
                    self.friend_match_arr.remove(u)

        random.shuffle(self.friend_match_arr)
        async def set_list():
            for u in self.friend_match_arr:
                await asynckivy.sleep(0)
                userbox = UserCard()
                userbox.ids.username.text = u['username']
                userbox.ids.username.secondary_text = u['status']
                userbox.ids.bio.text = u['bio']
                userbox.ids.streak.text = str(u['streak'])
                userbox.ids.tag.text = ', '.join(u['tags'])
                self.explorescreen.ids.layout.add_widget(userbox)
        asynckivy.start(set_list())

    def set_list_loc(self):
        async def set_list_loc():
            for i in range(20):
                await asynckivy.sleep(0)
                userbox = UserCard()
                userbox.ids.username.text = f'usernameloc {i}'
                self.explorescreen.ids.layout2.add_widget(userbox)
        asynckivy.start(set_list_loc())
      

    def refresh_callback(self, *args,**kwargs):
        '''A method that updates the state of your application
        while the spinner remains on the screen.'''

        def refresh_callback(interval):
            self.explorescreen.ids.layout.clear_widgets()
            self.set_list()
            self.explorescreen.ids.refresh_layout.refresh_done()
            self.tick = 0

        Clock.schedule_once(refresh_callback, 1)

    def refresh_callback_loc(self, *args,**kwargs):
        '''A method that updates the state of your application
        while the spinner remains on the screen.'''

        def refresh_callback_loc(interval):
            self.explorescreen.ids.layout2.clear_widgets()
            self.set_list_loc()
            self.explorescreen.ids.refresh_layout2.refresh_done()
            self.tick = 0

        Clock.schedule_once(refresh_callback_loc, 1)

    # end functions for explore

    # functions for login and register
    def signup(self):
        signupEmail = self.startscreen.ids.signupscreen.ids.signup_email.text
        signupPassword = self.startscreen.ids.signupscreen.ids.signup_password.text
        signupUsername = self.startscreen.ids.signupscreen.ids.signup_username.text
    
        if signupEmail.split() == [] or signupPassword.split() == [] or signupUsername.split() == []:
            cancel_btn_username_dialogue = MDFlatButton(text = 'Retry',on_release = self.close_username_dialog)
            self.dialog = MDDialog(title = 'Invalid Input',text = 'Please Enter a valid Input',size_hint = (0.7,0.2),buttons = [cancel_btn_username_dialogue])
            self.dialog.open()
        if len(signupUsername.split())>1:
            cancel_btn_username_dialogue = MDFlatButton(text = 'Retry',on_release = self.close_username_dialog)
            self.dialog = MDDialog(title = 'Invalid Username',text = 'Please enter username without space',size_hint = (0.7,0.2),buttons = [cancel_btn_username_dialogue])
            self.dialog.open()
   
        else:
            #  print(signupEmail,signupPassword)
            #  signup_info = str({f'\"{signupEmail}\":{{"Password":\"{signupPassword}\","Username":\"{signupUsername}\"}}'})
            #  signup_info = signup_info.replace(".","-")
            #  signup_info = signup_info.replace("\'","")
            #  to_database = json.loads(signup_info)
            #  print((to_database))
            #  requests.patch(url = self.url,json = to_database)
            #  self.startscreen.get_screen('loginscreen').manager.current = 'loginscreen'
            try:
                user = auth.create_user(
                email=signupEmail,
                email_verified=True,
                password=signupPassword,
                display_name=signupUsername,
                disabled=False)

                self.add(username=signupUsername,email=signupEmail)

                toast("success")
                print('Sucessfully created new user: {0}'.format(user.uid))
                # self.startscreen.get_screen('loginscreen').manager.current = 'loginscreen'
            except BaseException as err:
                print(err)
                toast("oops some error occured")
 
    def login(self):
        loginEmail = self.startscreen.ids.loginscreen.ids.login_email.text
        loginPassword = self.startscreen.ids.loginscreen.ids.login_password.text

        rest_api_url = f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword"
        web_api_key = 'AIzaSyDURk0eVsmw2wxqGQda0XqQfVrDNkmYAro'

        try:
            payload = json.dumps({
            "email": loginEmail,
            "password": loginPassword,
            "returnSecureToken":True
            })
            
            r = requests.post(rest_api_url,
                        params={"key": web_api_key},
                        data=payload)

            self.username = r.json()["displayName"]

        # supported_loginEmail = loginEmail.replace('.','-')
        # supported_loginPassword = loginPassword.replace('.','-')
        # request  = requests.get(self.url+'?auth='+self.auth)
        # data = request.json()
        # emails= set()
        # for key,value in data.items():
        #     emails.add(key)
        # if supported_loginEmail in emails and supported_loginPassword == data[supported_loginEmail]['Password']:
        #self.username = data[supported_loginEmail]['Username']
            # self.startscreen.get_screen('mainscreen').manager.current = 'mainscreen'
            

        except Exception as e:
            toast("not found")
            print("not found")
            print(e)

    def close_username_dialog(self,obj):
        self.dialog.dismiss()
   
    def after_login(self):

        try:
            # server connection
            s.connect((host,port))
            welcome = s.recv(512).decode('utf-8')

            # user info from firebase
            self.user_ref = db.collection(u'users').document(self.username)
            self.user = self.get_by_username(self.username)
            self.profilescreen.ids.username.text = self.username
            self.profilescreen.ids.fname.text = self.user['fname']
            self.profilescreen.ids.lname.text = self.user['lname']
            self.profilescreen.ids.email.text = self.user['email']
            self.profilescreen.ids.status.text = self.user['status']
            self.profilescreen.ids.bio.text = self.user['bio']
            self.profilescreen.ids.streak.secondary_text = str(self.user['streak'])
            # self.profilescreen.ids.location.secondary_text = self.user['city']
            self.profilescreen.ids.location.secondary_text = "istanbul"
            for t in self.user['tags']:
                self.profilescreen.ids.tag_box.add_widget(TagChip(label=t,icon="coffee"))

            self.screen.ids.profilescreen.add_widget(self.profilescreen)
            
            # end profile screen

            # build for explore page
            # self.friend_match_arr =  self.tag_match(self.user['tags'])
            # self.friends = self.user['friends']
            # if len(self.friend_match_arr) < 3:
            #     self.friend_match_arr += self.get_all()

            self.set_list()
            self.set_list_loc()


            self.screen.ids.explorescreen.add_widget(self.explorescreen)
            # end build for explore page
            
            # for chat
            self.screen.ids.chatscreen.add_widget(self.chatscreen)

            for u in self.friends:
                self.chatscreen.ids.friendlist.add_widget(FriendItem(text=u))

            # Add messages

            for m in self.user['messages']:
                self.new_message_private(m['from'],m['content'])

            for m in self.user['groups']:
                self.new_message(m,"..................")
            
            # server welcome message
            self.chatscreen.ids.msg_log.text += welcome + "\n"
        # end for chat

            self.startscreen.manager.current= 'myscreen'
            threading.Thread(target=self.handle_messages,args=(self.chatscreen,)).start()
            return

        except Exception as e:
            toast("oops something happened")
            print("something happened")
            print(e)
        
    def logout(self):
        self.startscreen.manager.current = 'loginscreen'


    # end functions for login and register
    def new_message(self, name, message):
        new_message =TwoLineAvatarIconListItem(text=name, secondary_text=message)
        new_message.add_widget(IconLeftWidget(icon="message-outline"))
        self.chatscreen.ids.grouplist.add_widget(new_message)


    def new_message_private(self, name, message):
        new_message = TwoLineAvatarIconListItem(text=name, secondary_text=message)
        new_message.add_widget(IconLeftWidget(icon="message-outline"))
        self.chatscreen.ids.privatelist.add_widget(new_message)

    


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
        self.profilescreen.ids.tag_box.remove_widget(instance)
        self.user['tags'].remove(value)
        self.user_ref.update({u'tags': firestore.ArrayRemove([value])})
        
        self.user_ref.update({
            u'timestamp': firestore.SERVER_TIMESTAMP
        })
        toast(f"{value} removed")

    # db functions for explore
     # get all the data in a collection
    def get_all(self,collection="users"):
        collection_ref = db.collection(f'{collection}')
        docs = collection_ref.stream()
        arr = []
        for doc in docs:
            print(f'{doc.id} => {doc.to_dict()}')
            arr.append(doc.to_dict())
        return arr

       # people with similar interests
    
    def tag_match(self,tag=[]):
        collection_ref = db.collection(u'users')
        query = collection_ref.where(u'tags', u'array_contains_any', tag)
        result = query.stream()
        arr = []
        for r in result:
            # print(f'{r.id} => {r.to_dict()}')
            arr.append(r.to_dict())
        return arr

    # end db functions for explore

    # login db
    def add(self,username, email,fname='', lname='',  bio='I am new here!', streak=0,  tags=[], status='happy', location=(),city='',friends=[]):
        # with specified document id.
        doc_ref = db.collection(u'users').document(f'{username}') 
        doc_ref.set({ # if you uncommented the line above, then chanhe this line to doc_ref.set({, default = db.collection(u'users').add({
            'username':username,
            'fname':fname,
            'lname':lname,
            'email':email,
            'streak':streak,
            'bio':bio,
            'tags':tags,
            'status': status,
            'location': location,
            'created': datetime.datetime.now(),
            'city':city,
            'friends': friends,
            'messages': [],
            'groups':[],
        })
    # end login db

    def add_friend(self,friend):

    # Atomically add a new friend to the 'friends' array field. you can add multiple.
        
        self.user_ref.update({u'friends': firestore.ArrayUnion([friend])})

        self.user_ref.update({
            u'timestamp': firestore.SERVER_TIMESTAMP
        })

        self.chatscreen.ids.friendlist.add_widget(FriendItem(text=friend))

        # automatically send a hello message to your new friend
        friend_ref = db.collection(u'users').document(friend)
        hello_msg =( {'from':self.username,'content':"hello! shall we chat?"},)
        friend_ref.update({u'messages': firestore.ArrayUnion(hello_msg)})

        friend_ref.update({
            u'timestamp': firestore.SERVER_TIMESTAMP
        })

        self.new_message_private(friend,"hello! shall we chat?")

    
    def delete_friend(self,friend):

    # Atomically add a new tag to the 'tags' array field. you can add multiple.
        self.chatscreen.ids.friendlist.remove_widget(friend)
           #  remove a friend
        self.user_ref.update({u'friends': firestore.ArrayRemove([friend.text])})

        self.user_ref.update({
            u'timestamp': firestore.SERVER_TIMESTAMP
        })

        # self.user_ref.update({u'friends': firestore.ArrayUnion([friend])})

        # self.user_ref.update({
        #     u'timestamp': firestore.SERVER_TIMESTAMP
        # })

    def send_private_message(self,message):
        self.user_ref.update({u'messages': firestore.ArrayUnion( (message,) )})

        self.user_ref.update({
            u'timestamp': firestore.SERVER_TIMESTAMP
        })



        # group chat message
    def send_message(self,to_send_out):
        try:
            print('sent')
            s.send((self.username+" - "+to_send_out).encode('utf-8'))
            
        except Exception as e:
            toast("oops error while sending message")
            print("Error sending: ",e)
        
    def handle_messages(self,obj):
        while True:
            try:
                data = s.recv(1024).decode('utf-8')
                self.chatscreen.ids.msg_log.text += data + "\n"
            except Exception as e:
                toast("oops error while handling the message")
                print (e)

        
            


if __name__ == '__main__':
    Chatty().run()
