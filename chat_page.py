
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window

screen_helper = """
Screen:
    NavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: 'chats'
                        left_action_items: [["menu", lambda x: nav_drawer.set_state()]]
                        elevation: 5
                    Screen:
                        MDLabel:
                            text: 'messaging here!'
                            halign: 'center'
        MDNavigationDrawer:
            id: nav_drawer
            Screen:
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: 'private/group'
                    Screen:
                        MDLabel:
                            text: 'ongoing chats'
                            halign: 'center'
            
"""


class Chatty(MDApp):
    def build(self):
        screen = Builder.load_string(screen_helper)
        return screen


if __name__ == '__main__':
    Chatty().run()