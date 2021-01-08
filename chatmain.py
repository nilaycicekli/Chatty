from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy import Config
Config.set('graphics', 'multisamples', '0') 
from kivy.utils import get_color_from_hex
############
import socket,threading
global s
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "127.0.0.1";port = 5005
#######
global name
name = "bilal"

KV="""

<Chat>:
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
                    font_size: root.height / 20

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
            MDTextInput:
                id: message
                hint_text: "Type here"
                multiline: False
                on_text_validate: root.send_message(message.text)

Chat:
    name:'chatscreen'
"""

class Chat(Screen):
    pass

class  Talkie(MDApp):
    def build(self):
        self.screen = Builder.load_string(KV)
        s.connect((host,port))
        welcome = s.recv(512).decode('utf-8')
        self.screen.ids.msg_log.text +=str(welcome +  '\n')
        threading.Thread(target=self.handle_messages).start()
        return self.screen

    def start_messaging(self):
        s.connect((host,port))
        welcome = s.recv(512).decode('utf-8')
        self.screen.ids.msg_log.text +=str(welcome +  '\n')
        threading.Thread(target=self.handle_messages).start()
        
    def handle_messages(self):
        while True:
            try:
                data = s.recv(1024).decode('utf-8')
                self.screen.ids.msg_log.text += data + "\n"
            except Exception as e:
                print (e)

    def send_message(self,to_send_out):
        try:
            print('sent')
            s.send((name+" - "+to_send_out).encode('utf-8'))
            
        except Exception as e:
            print("Error sending: ",e)

if __name__ == "__main__":
    Talkie().run()