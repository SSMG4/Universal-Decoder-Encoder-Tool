import base64
import zlib
import binascii
import pyperclip

# Morse code dictionary (uppercase keys, but we’ll return lowercase later)
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',
    ',': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.', '-': '-....-',
    '(': '-.--.', ')': '-.--.-', ' ': '/'
}

# Reverse dictionary for Morse decoding
REVERSE_MORSE_DICT = {v: k for k, v in MORSE_CODE_DICT.items()}

def morse_to_text(morse_code):
    morse_code += ' '
    decipher = ''
    citext = ''
    space_count = 0  # track spaces to detect word gaps
    for letter in morse_code:
        if letter != ' ':
            citext += letter
            space_count = 0
        else:
            space_count += 1
            if citext != '':
                # decode Morse to uppercase letter, then convert to lowercase
                decipher += REVERSE_MORSE_DICT.get(citext, '')
                citext = ''
            if space_count == 2:
                decipher += ' '  # double space = space between words
    return decipher.lower()  # <-- lowercase output

def text_to_morse(text):
    text = text.upper()
    morse = ''
    for letter in text:
        morse += MORSE_CODE_DICT.get(letter, '') + ' '
    return morse.strip()

# Helper functions same as before
def base64_to_bytes(data):
    return base64.b64decode(data)

def bytes_to_base64(data):
    return base64.b64encode(data).decode()

def zlib_decompress(data):
    return zlib.decompress(data)

def zlib_compress(data):
    return zlib.compress(data)

def hex_to_bytes(data):
    return binascii.unhexlify(data)

def bytes_to_hex(data):
    return binascii.hexlify(data).decode()

def text_to_bytes(text):
    return text.encode('utf-8')

def bytes_to_text(data):
    return data.decode('utf-8', errors='ignore')

def multiline_input(prompt):
    print(prompt)
    lines = []
    while True:
        line = input()
        if line == '':
            break
        lines.append(line)
    return ''.join(lines).strip()

def run_decoder():
    while True:  # MAIN LOOP

        print("\n🔥 Universal Decoder/Encoder Tool 🔥")
        print("Choose an operation:")
        print("1) Base64 -> Zlib -> Text")
        print("2) Base64 -> Text")
        print("3) Zlib -> Text")
        print("4) Zlib -> Base64 -> Text")
        print("5) Binary -> Zlib -> Text")
        print("6) Binary -> Text")
        print("7) Binary -> Base64 -> Text")
        print("8) Hex -> Text")
        print("9) Hex -> Zlib -> Text")
        print("10) Hex -> Base64 -> Zlib -> Text")
        print("11) Hex -> Base64 -> Text")
        print("12) Text -> Morse")
        print("13) Morse -> Text")
        print("14) Exit")

        choice = input("Enter choice number: ").strip()

        if choice == '14':
            print("Exiting... Bye Bye! ✌️")
            break

        raw_input_data = multiline_input("Paste your input (end with blank line):")

        try:
            if choice == '1':
                result = bytes_to_text(zlib_decompress(base64_to_bytes(raw_input_data)))
            elif choice == '2':
                result = base64_to_bytes(raw_input_data).decode('utf-8', errors='ignore')
            elif choice == '3':
                result = bytes_to_text(zlib_decompress(raw_input_data.encode()))
            elif choice == '4':
                result = bytes_to_text(zlib_decompress(base64_to_bytes(raw_input_data)))
            elif choice == '5':
                result = bytes_to_text(zlib_decompress(raw_input_data.encode()))
            elif choice == '6':
                result = raw_input_data
            elif choice == '7':
                result = base64_to_bytes(raw_input_data).decode('utf-8', errors='ignore')
            elif choice == '8':
                result = bytes_to_text(hex_to_bytes(raw_input_data))
            elif choice == '9':
                result = bytes_to_text(zlib_decompress(hex_to_bytes(raw_input_data)))
            elif choice == '10':
                # This combo might be tricky, careful
                temp = hex_to_bytes(raw_input_data)
                temp2 = base64_to_bytes(temp.decode())
                result = bytes_to_text(zlib_decompress(temp2))
            elif choice == '11':
                result = base64_to_bytes(hex_to_bytes(raw_input_data).decode()).decode('utf-8', errors='ignore')
            elif choice == '12':
                result = text_to_morse(raw_input_data)
            elif choice == '13':
                result = morse_to_text(raw_input_data)
            else:
                print("Invalid option or not implemented yet.")
                continue

            print("\n==== Result ====\n")
            print(result)
            print("\n================")

            copy = input("Copy result to clipboard? (y/n): ").lower()
            if copy == 'y':
                pyperclip.copy(result)
                print("Copied to clipboard! 🚀")

        except Exception as e:
            print(f"\n❌ Error: {e}")

        # After done, give user choice to continue or exit
        cont = input("\nWhat do you want to do now? [M]enu / [E]xit: ").strip().lower()
        if cont == 'e':
            print("Exiting... Catch you later! 👋")
            break
        # else continue looping

if __name__ == "__main__":
    run_decoder()
