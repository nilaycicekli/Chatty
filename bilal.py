from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.app import MDApp
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty, ListProperty, ObjectProperty
from kivymd.uix.list import TwoLineListItem
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.list import IRightBodyTouch
from kivymd.uix.list import TwoLineAvatarIconListItem 
from kivymd.uix.list import IconLeftWidget
from kivymd.uix.list import IconRightWidget
from kivymd.uix.label import MDLabel




############
import socket,threading
global s
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "127.0.0.1";port = 5005
#######
global name
name = "bilal"


the_chat_page = """
<Chat>:
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

        MDBoxLayout:
            size_hint_y: None
            height: 40
            spacing: 15

            canvas:
                Color:
                    rgba: (0.746,0.8,0.86,1)
                Rectangle:
                    pos: self.pos
                    size: self.size
            TextInput:
                id: message
                hint_text: "Type here"
                multiline: False
                on_text_validate: root.send_message(message.text)

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
                    Chat:
                        id: chatscreen
                        name: 'chatscreen'
                
                            
        # this is the panel that pops out of the left                   
        MDNavigationDrawer:
            id: nav_drawer
            
            MDScreen:
                BoxLayout:
                    canvas:
                        Color: 
                            rgb: 1, 0, 0
                    orientation: 'vertical'
                    # choose chat list (personal/private)
                    BoxLayout:
                        orientation: 'horizontal'
                        size_hint_y: 0.1
                        padding: 8
                        Button:
                            text: 'private'
                            on_press:
                                root.window_manager.current = "privatewindow"
                        Button:
                            text: 'group'
                            on_release:
                                root.window_manager.current = "groupwindow"
                
                
                
                    # to view selected chat list
                    Screen:
                        WindowManager:
                            id: window_manager
                            PrivateWindow:
                                name: "privatewindow"
                                id: privatewindow
                                ScrollView:
                                    MDList:
                                        id: privatelist

                            GroupWindow:
                                name: "groupwindow"
                                id: groupwindow
                                ScrollView:
                                    MDList:
                                        id: grouplist


                                        
                            

<PrivateWindow>:
    MDLabel:
        halign: 'center'
<GroupWindow>:
    MDLabel:
        halign: 'center'    
                                            
"""


# private chats
class PrivateWindow(Screen):
    pass
# group chats
class GroupWindow(Screen):
    pass

class WindowManager(ScreenManager):
    pass

class GroupChatListBox(MDBoxLayout):
    pass

class Container(MDBoxLayout):
    pass
class Chat(Screen):
    global s
    msg_log= ObjectProperty()
        
    # def on_enter(self):
    #     s.connect((host,port))
    #     welcome = s.recv(512)
    #     self.msg_log.text += str(welcome + "\n")
    #     threading.Thread(target=self.handle_messages).start()

      
    def send_message(self,to_send_out):
        try:
            print('sent')
            s.send((name+" - "+to_send_out).encode('utf-8'))
            
        except Exception as e:
            print("Error sending: ",e)
        
    def handle_messages(obj):
        while True:
            try:
                data = s.recv(1024).decode('utf-8')
                obj.msg_log.text += data + "\n"
            except Exception as e:
                print (e)

# the page
sm = ScreenManager()
sm.add_widget(PrivateWindow(name='private'))
sm.add_widget(GroupWindow(name='group'))
sm.add_widget(Chat(name="main_screen"))

class Chatty(MDApp,App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen = Builder.load_string(the_chat_page)

        s.connect((host,port))
        welcome = s.recv(512).decode('utf-8')
        
        self.screen.ids.chatscreen.ids.msg_log.text += welcome + "\n"

    def on_start(self):
        # Set colors
        self.theme_cls.primary_palette = 'Red'
        self.theme_cls.primary_hue = '900'

        # Add messages
        self.new_message("girl power", "hello")
        self.new_message("travel", "istanbul this week?")
        self.new_message("weekend party", "wohoo")
        self.new_message("pyhon project", "pushed it to github")
        self.new_message("Whats App", "fine")
        self.new_message("Me Myself", "some notes...")
        self.new_message("hmmm", "what??")

        self.new_message_private("nilay", "heyoo")
        self.new_message_private("sila", "naber niloşş")
        self.new_message_private("bilal", "i am so sleepy")
        self.new_message_private("busra", "cuma geliyor musun kelebek")
        self.new_message_private("betul", "thx")
        self.new_message_private("ellen", "no")
        self.new_message_private("jack", "let me think")

    def build(self):
        # self.screen = Builder.load_string(the_chat_page)

        # s.connect((host,port))
        # welcome = s.recv(512).decode('utf-8')
        # self.screen.ids.chatscreen.ids.msg_log.text += str(welcome + "\n")
        threading.Thread(target=Chat.handle_messages,args=(self.screen.ids.chatscreen,)).start()

        return self.screen

    def new_message(self, name, message):
        new_message =TwoLineAvatarIconListItem(text=name, secondary_text=message)
        new_message.add_widget(IconLeftWidget(icon="message-outline"))
        self.screen.ids.grouplist.add_widget(new_message)


    def new_message_private(self, name, message):
        new_message = TwoLineAvatarIconListItem(text=name, secondary_text=message)
        new_message.add_widget(IconLeftWidget(icon="message-outline"))
        self.screen.ids.privatelist.add_widget(new_message)



if __name__ == '__main__':
    Chatty().run()