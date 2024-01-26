leet_dict = {
    'a': '4',
    'b': '8',
    'e': '3',
    'g': '6',
    'i': '1',
    'o': '0',
    's': '5',
    't': '7',
    'h': '2'
}

def to_leet_speak(text):
    return ''.join(leet_dict.get(c.lower(), c) for c in text)

print(to_leet_speak("Hello, World!"))
