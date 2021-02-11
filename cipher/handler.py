import worker

class Handler():

    def on_button_code_choice_clicked(self, dropdown, button):
        # Set code type property.
        dropdown.code_type = button.text
        # Set button text to code_type.
        for child in dropdown.parent.children:
            try:
                child.code_options.text = button.text
            except AttributeError:
                pass
        # Make dropdown disappear.
        dropdown.dismiss()
        print(f"Using code '{dropdown.code_type}'.")
        return button.text

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
        # Reset the text on the code choice button and clear code type variable.
        window.code_options.text = 'Choose your code:'
        window.dropdown.code_type = ''
