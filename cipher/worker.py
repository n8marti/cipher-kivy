# TODO: Still a WIP.

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

def transform_text(text_to_convert, transformation):
    converted_text = []
    for c in text_to_convert:
        if c not in transformation.keys():
            converted_text.append(c)
        else:
            converted_text.append(transformation[c])
    return converted_text

def encode_opt1(orig_phrase):
    encode_pairs = dict(zip(alphabet, opt1))
    output = transform_text(orig_phrase, encode_pairs)
    return output

def decode_opt1(orig_phrase):
    encode_pairs = dict(zip(alphabet, opt1))
    output = transform_text(orig_phrase, encode_pairs)
    return output

def encode_opt2(orig_phrase):
    encode_pairs = dict(zip(alphabet, opt2))
    output = transform_text(orig_phrase, encode_pairs)
    return output

def decode_opt2(orig_phrase):
    decode_pairs = dict(zip(opt2, alphabet))
    output = transform_text(orig_phrase, decode_pairs)
    return output

def encode_opt3(orig_phrase):
    out1 = encode_opt1(orig_phrase)
    out2 = encode_opt2(out1)
    return out2

def decode_opt3(orig_phrase):
    out2 = decode_opt2(orig_phrase)
    out1 = decode_opt1(out2)
    return out1

def get_uppers(orig_phrase):
    # Note which characters are capitalized.
    num = 0
    uppers = []
    for l in orig_phrase:
        if l.isupper():
            uppers.append(num)
        num += 1
    return uppers

def convert_text(text_to_convert, picked_code, action):
    # Convert the text (output as a list) using the dictionary.
    if picked_code == 'Option 1':
        converted_text = encode_opt1(text_to_convert)
    elif picked_code == 'Option 2':
        if action == 'Encode':
            converted_text = encode_opt2(text_to_convert)
        if action == 'Decode':
            converted_text = decode_opt2(text_to_convert)
    elif picked_code == 'Option 3':
        if action == 'Encode':
            converted_text = encode_opt3(text_to_convert)
        if action == 'Decode':
            converted_text = decode_opt3(text_to_convert)
    return converted_text

def set_uppers(converted_text, uppers):
    # Prepare the output with correct capitalization.
    output_text = converted_text
    for i in uppers:
        output_text[i] = output_text[i].upper()
    return output_text

def on_code_choice_changed(button):
    tree_iter = code_choice.get_active_iter()
    if tree_iter is not None:
        model = code_choice.get_model()
        text = model[tree_iter][0]
        print(text)

def on_button_encode_clicked(button):
    encode_or_decode_text(button)

def on_button_decode_clicked(button):
    encode_or_decode_text(button)

def encode_or_decode_text(window, button):
    action = button.text
    # First, clear any text in the output box.
    window.text_output.text = ''
    # Get text in entry box.
    original_phrase = window.text_input.text
    # Store indexes of upper case characters.
    uppers = get_uppers(original_phrase)
    # Set all characters to lower case for conversion.
    text_to_convert = original_phrase.lower() if original_phrase else ''
    picked_code = window.dropdown.code_type
    # Convert text.
    converted_text = convert_text(text_to_convert, picked_code, action)
    # Set correct upper case characters.
    output_text = set_uppers(converted_text, uppers)
    output_phrase = ''.join(output_text)
    # Set encoded/decoded text in output box.
    window.text_output.text = output_phrase

def on_button_clear_clicked(button):
    entry_output.set_text('')
    entry_input.set_text('')
