import worker

class Handler():

    def on_button_code_choice_clicked(self, dropdown, button):
        dropdown.code_type = button.text
        print(f"Using code '{dropdown.code_type}'.")

    def on_button_encode_or_decode_clicked(self, window, button):
        # Ensure there is text to encode or decode.
        if not window.text_input.text:
            window.text_output.text = "Please enter some text to encode or decode."
        # Ensure that a code option has been selected.
        elif not window.dropdown.code_type:
            window.text_output.text = "Please choose your code option."
        else:
            worker.encode_or_decode_text(window, button)

    def on_button_clear_clicked(self, window, button):
        # Reset the text in the TextInput and TextOutput boxes.
        window.text_input.text = ''
        window.text_output.text = ''
