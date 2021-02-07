
import kivy
kivy.require('2.0.0')
import sys

from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.dropdown import DropDown
from pathlib import Path

# Add app's parent directory to PYTHONPATH.
sys.path.append(str(Path(__file__).parents[0]))

from handler import Handler


class CustomDropDown(DropDown):

    def __init__(self, **kwargs):
        super(CustomDropDown, self).__init__()

    def handle_code_choice(self, button):
        Handler().on_button_code_choice_clicked(self, button)

    code_type = ObjectProperty(None)


class CipherBoxLayout(BoxLayout):

    def __init__(self, **kwargs):
        super(CipherBoxLayout, self).__init__()
        #self.code_options = ObjectProperty(None)
        #self.text_input = ObjectProperty(None)
        self.dropdown = CustomDropDown()

    def handle_clear_clicked(self, button):
        Handler().on_button_clear_clicked(self, button)

    def handle_encode_clicked(self, button):
        Handler().on_button_encode_clicked(self, button)

    def handle_decode_clicked(self, button):
        Handler().on_button_decode_clicked(self, button)

    text_input = ObjectProperty(None)
    text_output = ObjectProperty(None)
    code_options = ObjectProperty(None)


class CipherApp(App):

    def __init__(self, **kwargs):
        super(CipherApp, self).__init__()
        self.kv_directory = '../data/ui'

    def build(self):
        return CipherBoxLayout()


if __name__ == '__main__':
    CipherApp().run()
