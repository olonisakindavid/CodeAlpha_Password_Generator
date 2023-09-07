import random
import string
import PySimpleGUI as gui

gui.theme('BlueMono')
gui.set_options(font='verdana 15')

screen_layout = [
    [gui.Text('Password Length: '), gui.InputText(size=15, key='-LENGTH-')],
    [gui.Checkbox('Uppercase Letters🔠', default=True, key='-UPPER-')],
    [gui.Checkbox('Lowercase Letters 🔡', default=True, key='-LOWER-')],
    [gui.Checkbox('Digits 🔢', default=True, key='-DIGITS-')],
    [gui.Checkbox('Symbols 🔣', default=True, key='-SYMBOLS-')],
    [gui.Button('Generate Password')],
    [gui.Text('Password'), gui.Multiline(
        size=15, no_scrollbar=True, disabled=True, key='-PASS-')]
]

window = gui.Window('Password Generator', screen_layout)

while True:
    event, values = window.read()

    if event == gui.WIN_CLOSED:
        break

    if event == 'Generate Password':
        try:
            length = int(values['-LENGTH-'])

            use_upper = values['-UPPER-']
            use_lower = values['-LOWER-']
            use_digits = values['-DIGITS-']
            use_symbols = values['-SYMBOLS-']

            characters = ""
            if use_upper:
                characters += string.ascii_uppercase
            if use_lower:
                characters += string.ascii_lowercase
            if use_digits:
                characters += string.digits
            if use_symbols:
                characters += string.punctuation

            if characters:
                password = ''.join(random.choice(characters)
                                   for _ in range(length))
                window['-PASS-'].update(password)
            else:
                window['-PASS-'].update("Please select at least one character type")

        except ValueError:
            window['-PASS-'].update("Invalid, retry")

window.close()
