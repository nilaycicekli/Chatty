
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager


the_chat_page = """
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


sm = ScreenManager()
sm.add_widget(PrivateWindow(name='private'))
sm.add_widget(GroupWindow(name='group'))
sm.add_widget(FriendList(name='friends'))


class Chatty(MDApp):
    def build(self):
        screen = Builder.load_string(the_chat_page)
        return screen


if __name__ == '__main__':
    Chatty().run()
