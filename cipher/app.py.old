#!/usr/bin/env python3

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from pathlib import Path

class CipherApp(Gtk.Application):
    def __init__(self):
        super().__init__()

        repo = Path(__file__).parents[1]
        self.ui_dir = str(repo / 'data' / 'ui')

        # Define the code system.
        self.alphabet = [
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
        ]

        # Create reverse alphabet.
        self.opt1 = sorted(self.alphabet, reverse=True)
        self.opt2 = [
            'f', 'b', 'c', 'o', 'd', 'w', 'n', 'x', 'l', 'h', 'k', 'j', 'e',
            't', 'a', 'g', 'p', 'z', 'q', 'i', 'v', 'm', 'u', 's', 'y', 'r'
        ]
        self.opt3 = '3'
        self.action = 'encode'
        self.handlers = {
            "onDestroy": Gtk.main_quit,
            "on_button_encode_clicked": self.on_button_encode_clicked,
            "on_button_decode_clicked": self.on_button_decode_clicked,
            "on_button_clear_clicked": self.on_button_clear_clicked,
            "on_code_choice_changed": self.on_code_choice_changed,
        }

    def do_startup(self):
        Gtk.Application.do_startup(self)
        self.builder = Gtk.Builder()
        self.builder.add_from_file(self.ui_dir + '/cipher.glade')
        self.window = self.builder.get_object('cipher_window')
        self.entry_input = self.builder.get_object('entry_input')
        self.entry_output = self.builder.get_object('entry_output')
        self.code_choice = self.builder.get_object('code_choice')
        self.text_input = self.builder.get_object('text_input')
        self.text_output = self.builder.get_object('text_output')
        self.entry_input = self.text_input.get_buffer()
        self.entry_output = self.text_output.get_buffer()


    def do_activate(self):
        self.add_window(self.window)
        self.window.show()
        self.builder.connect_signals(self.handlers)

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
        if picked_code == 'opt1':
            converted_text = self.encode_opt1(text_to_convert)
        elif picked_code == 'opt2':
            if action == 'Encode':
                converted_text = self.encode_opt2(text_to_convert)
            if action == 'Decode':
                converted_text = self.decode_opt2(text_to_convert)
        elif picked_code == 'opt3':
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

    def on_code_choice_changed(self, button):
        tree_iter = self.code_choice.get_active_iter()
        if tree_iter is not None:
            model = self.code_choice.get_model()
            text = model[tree_iter][0]
            print(text)

    def on_button_encode_clicked(self, button):
        self.encode_or_decode_text(button)

    def on_button_decode_clicked(self, button):
        self.encode_or_decode_text(button)
        
    def encode_or_decode_text(self, button):
        action = button.get_label()
        self.entry_output.set_text('')
        start = self.entry_input.get_start_iter()
        end = self.entry_input.get_end_iter()
        original_phrase = self.entry_input.get_text(start, end, False)
        uppers = self.get_uppers(original_phrase)
        text_to_convert = original_phrase.lower() if original_phrase else ''
        self.picked_code = self.code_choice.get_active_id()
        converted_text = self.convert_text(text_to_convert, self.picked_code, action)
        output_text = self.set_uppers(converted_text, uppers)
        output_phrase = ''.join(output_text)
        self.entry_output.set_text(output_phrase)

    def on_button_clear_clicked(self, button):
        self.entry_output.set_text('')
        self.entry_input.set_text('')


app = CipherApp()
