# when you run this file, you can see all the items that kivymd offers
from kivy.lang import Builder
from kivy.properties import StringProperty

from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.snackbar import Snackbar


KV_CODE = '''
#:import md_icons kivymd.icon_definitions.md_icons
#:set FONT_SIZE 64
RecycleView:
    viewclass: 'Item'
    data:
        [{
        'font_style': 'Icon',
        'text': value,
        'icon_name': key,
        'halign': 'center',
        'font_size': FONT_SIZE,
        } for key, value in md_icons.items()]
    RecycleGridLayout:
        cols: root.width // FONT_SIZE
        size_hint_y: None
        height: self.minimum_height
        default_size: FONT_SIZE, FONT_SIZE
        default_size_hint: None, None
'''


class Item(MDLabel):
    icon_name = StringProperty()

    def on_touch_down(self, touch):
        if self.collide_point(*touch.opos):
            Snackbar(text=self.icon_name, duration=1.5).show()

class ListingAllIconsApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def build(self):
        return Builder.load_string(KV_CODE)


if __name__ == '__main__':
    ListingAllIconsApp().run()