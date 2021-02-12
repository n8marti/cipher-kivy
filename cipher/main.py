
import kivy
kivy.require('2.0.0')

from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.dropdown import DropDown
from kivy.uix.image import Image


class Worker():

    # Define the code system.
    alphabet = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
        'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
    ]

    # Create reverse alphabet.
    opt1 = sorted(alphabet, reverse=True)
    opt2 = [
        'f', 'b', 'c', 'o', 'd', 'w', 'n', 'x', 'l', 'h', 'k', 'j', 'e',
        't', 'a', 'g', 'p', 'z', 'q', 'i', 'v', 'm', 'u', 's', 'y', 'r'
    ]


    def transform_text(self, text_to_convert, transformation):
        converted_text = []
        for c in text_to_convert:
            if c not in transformation.keys():
                converted_text.append(c)
            else:
                converted_text.append(transformation[c])
        return converted_text

    def encode_opt1(self, orig_phrase):
        encode_pairs = dict(zip(self.alphabet, self.opt1))
        output = self.transform_text(orig_phrase, encode_pairs)
        return output

    def decode_opt1(self, orig_phrase):
        encode_pairs = dict(zip(self.alphabet, self.opt1))
        output = self.transform_text(orig_phrase, encode_pairs)
        return output

    def encode_opt2(self, orig_phrase):
        encode_pairs = dict(zip(self.alphabet, self.opt2))
        output = self.transform_text(orig_phrase, encode_pairs)
        return output

    def decode_opt2(self, orig_phrase):
        decode_pairs = dict(zip(self.opt2, self.alphabet))
        output = self.transform_text(orig_phrase, decode_pairs)
        return output

    def encode_opt3(self, orig_phrase):
        out1 = self.encode_opt1(orig_phrase)
        out2 = self.encode_opt2(out1)
        return out2

    def decode_opt3(self, orig_phrase):
        out2 = self.decode_opt2(orig_phrase)
        out1 = self.decode_opt1(out2)
        return out1

    def get_uppers(self, orig_phrase):
        # Note which characters are capitalized.
        num = 0
        uppers = []
        for l in orig_phrase:
            if l.isupper():
                uppers.append(num)
            num += 1
        return uppers

    def convert_text(self, text_to_convert, picked_code, action):
        # Convert the text (output as a list) using the dictionary.
        if picked_code == 'Option 1':
            converted_text = self.encode_opt1(text_to_convert)
        elif picked_code == 'Option 2':
            if action == 'Encode':
                converted_text = self.encode_opt2(text_to_convert)
            if action == 'Decode':
                converted_text = self.decode_opt2(text_to_convert)
        elif picked_code == 'Option 3':
            if action == 'Encode':
                converted_text = self.encode_opt3(text_to_convert)
            if action == 'Decode':
                converted_text = self.decode_opt3(text_to_convert)
        return converted_text

    def set_uppers(self, converted_text, uppers):
        # Prepare the output with correct capitalization.
        output_text = converted_text
        for i in uppers:
            output_text[i] = output_text[i].upper()
        return output_text

    def encode_or_decode_text(self, window, button):
        action = button.text
        # First, clear any text in the output box.
        window.text_output.text = ''
        # Get text in entry box.
        original_phrase = window.text_input.text
        # Store indexes of upper case characters.
        uppers = self.get_uppers(original_phrase)
        # Set all characters to lower case for conversion.
        text_to_convert = original_phrase.lower() if original_phrase else ''
        picked_code = window.dropdown.code_type
        # Convert text.
        converted_text = self.convert_text(text_to_convert, picked_code, action)
        # Set correct upper case characters.
        output_text = self.set_uppers(converted_text, uppers)
        output_phrase = ''.join(output_text)
        # Set encoded/decoded text in output box.
        window.text_output.text = output_phrase


class CustomDropDown(DropDown):

    code_type = ObjectProperty(None)

    def handle_code_choice(self, button):
        # Set code type property.
        self.code_type = button.text
        # Set button text to code_type.
        for child in self.parent.children:
            try:
                child.code_options.text = button.text
            except AttributeError:
                pass
        # Make dropdown disappear.
        self.dismiss()
        print(f"Using code '{self.code_type}'.")
        return button.text


class CipherBoxLayout(BoxLayout):

    text_input = ObjectProperty(None)
    text_output = ObjectProperty(None)
    code_options = ObjectProperty(None)
    icon_path = "./cipher.png"

    def __init__(self, **kwargs):
        super(CipherBoxLayout, self).__init__()
        self.dropdown = CustomDropDown()

    def handle_clear_clicked(self, button):
        # Reset the text in the TextInput and TextOutput boxes.
        self.text_input.text = ''
        self.text_output.text = ''
        # Reset the text on the code choice button and clear code type variable.
        self.code_options.text = 'Choose your code:'
        self.dropdown.code_type = ''

    def handle_encode_or_decode_clicked(self, button):
        # Ensure there is text to encode or decode.
        if not self.text_input.text:
            self.text_output.text = "Please enter some text to encode or decode."
        # Ensure that a code option has been selected.
        elif not self.dropdown.code_type:
                self.text_output.text = "Please choose your code option."
        else:
            worker = Worker()
            worker.encode_or_decode_text(self, button)


class CipherApp(App):

    def build(self):
        self.cipherbox = CipherBoxLayout()
        return self.cipherbox


if __name__ == '__main__':
    CipherApp().run()
