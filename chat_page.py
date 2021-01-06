
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.app import MDApp
from kivy.app import App
from kivy.lang import Builder

the_chat_page = """
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
                        canvas:
                            Color:
                                rgb: 1, 0, 0        
                        MDLabel:
                            text: 'messaging here!'
                            halign: 'center'
                
                            
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
                            text: 'private'
                            on_press:
                                root.window_manager.current = "private_window"
                        Button:
                            on_press:
                                root.window_manager.current = "group_window"
                            text: 'group'
                
                    # to view selected chat list
                    WindowManager:
                        id: window_manager
                        PrivateWindow:
                            name: "private_window"
                        GroupWindow:
                            name: "group_window"
                            
<PrivateWindow>:
    MDLabel:
        text: 'it works but wont switch!'
        halign: 'center'
<GroupWindow>:
    MDLabel:
        text: 'it works!'
        halign: 'center'                                          
"""


# private chats
class PrivateWindow(Screen):
    pass
# group chats
class GroupWindow(Screen):
    pass
# annoying
class WindowManager(ScreenManager):
    pass

# the page
sm = ScreenManager()
sm.add_widget(PrivateWindow(name='private'))
sm.add_widget(GroupWindow(name='group'))


class Chatty(MDApp,App):
    def build(self):
        screen = Builder.load_string(the_chat_page)
        return screen


if __name__ == '__main__':
    Chatty().run()
