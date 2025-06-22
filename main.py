import os
import subprocess
import base64
import zlib
import binascii
import pyperclip
import codecs
import html

# Current version (used by update.py if needed)
CURRENT_VERSION = "v1.0-release"

try:
    import pyfiglet
    print(pyfiglet.figlet_format("UniDecoder"))
except ImportError:
    print("[!] pyfiglet not installed, banner skipped.")

AUTOUPDATE_FILE = ".autoupdate"
UPDATE_SCRIPT = "update.py"

def auto_update_check():
    if os.path.exists(AUTOUPDATE_FILE):
        with open(AUTOUPDATE_FILE, "r") as f:
            enabled = f.read().strip().lower()
        if enabled == "true":
            print("[*] Auto-update is ON, checking for updates...")
            try:
                subprocess.run(["python", UPDATE_SCRIPT], check=True)
                print("[*] Update check complete.")
            except subprocess.CalledProcessError as e:
                print(f"[!] Auto-update failed: {e}")
            except Exception as e:
                print(f"[!] Unexpected error during auto-update: {e}")
        else:
            print("[*] Auto-update is OFF, skipping update check.")
    else:
        print("[*] Auto-update setting not found, skipping update check.")

auto_update_check()

# Morse code dictionary (uppercase keys, lowercase output)
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

REVERSE_MORSE_DICT = {v: k for k, v in MORSE_CODE_DICT.items()}

def morse_to_text(morse_code):
    morse_code += ' '
    decipher = ''
    citext = ''
    space_count = 0
    for letter in morse_code:
        if letter != ' ':
            citext += letter
            space_count = 0
        else:
            space_count += 1
            if citext != '':
                decipher += REVERSE_MORSE_DICT.get(citext, '')
                citext = ''
            if space_count == 2:
                decipher += ' '
    return decipher.lower()

def text_to_morse(text):
    text = text.upper()
    return ' '.join(MORSE_CODE_DICT.get(letter, '') for letter in text).strip()

# Encoding/decoding functions
def base64_to_bytes(data): return base64.b64decode(data)
def bytes_to_base64(data): return base64.b64encode(data).decode()
def zlib_decompress(data): return zlib.decompress(data)
def zlib_compress(data): return zlib.compress(data)
def hex_to_bytes(data): return binascii.unhexlify(data)
def bytes_to_hex(data): return binascii.hexlify(data).decode()
def text_to_bytes(text): return text.encode('utf-8')
def bytes_to_text(data): return data.decode('utf-8', errors='ignore')
def encode_rot13(data): return codecs.encode(data, 'rot_13')
def decode_rot13(data): return codecs.decode(data, 'rot_13')
def encode_base32(data): return base64.b32encode(data.encode()).decode()
def decode_base32(data): return base64.b32decode(data.encode()).decode()
def encode_html_entities(data): return html.escape(data)
def decode_html_entities(data): return html.unescape(data)

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
    while True:
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
        print("14) Text -> ROT13")
        print("15) ROT13 -> Text")
        print("16) Text -> Base32")
        print("17) Base32 -> Text")
        print("18) Text -> HTML Entities")
        print("19) HTML Entities -> Text")
        print("20) Exit")

        choice = input("Enter choice number: ").strip()
        if choice == '20':
            print("Exiting... Bye Bye! ✌️")
            break

        raw_input_data = multiline_input("Paste your input (end with blank line):")
        try:
            if choice == '1': result = bytes_to_text(zlib_decompress(base64_to_bytes(raw_input_data)))
            elif choice == '2': result = base64_to_bytes(raw_input_data).decode('utf-8', errors='ignore')
            elif choice == '3': result = bytes_to_text(zlib_decompress(raw_input_data.encode()))
            elif choice == '4': result = bytes_to_text(zlib_decompress(base64_to_bytes(raw_input_data)))
            elif choice == '5': result = bytes_to_text(zlib_decompress(raw_input_data.encode()))
            elif choice == '6': result = raw_input_data
            elif choice == '7': result = base64_to_bytes(raw_input_data).decode('utf-8', errors='ignore')
            elif choice == '8': result = bytes_to_text(hex_to_bytes(raw_input_data))
            elif choice == '9': result = bytes_to_text(zlib_decompress(hex_to_bytes(raw_input_data)))
            elif choice == '10': result = bytes_to_text(zlib_decompress(base64_to_bytes(hex_to_bytes(raw_input_data).decode())))
            elif choice == '11': result = base64_to_bytes(hex_to_bytes(raw_input_data).decode()).decode('utf-8', errors='ignore')
            elif choice == '12': result = text_to_morse(raw_input_data)
            elif choice == '13': result = morse_to_text(raw_input_data)
            elif choice == '14': result = encode_rot13(raw_input_data)
            elif choice == '15': result = decode_rot13(raw_input_data)
            elif choice == '16': result = encode_base32(raw_input_data)
            elif choice == '17': result = decode_base32(raw_input_data)
            elif choice == '18': result = encode_html_entities(raw_input_data)
            elif choice == '19': result = decode_html_entities(raw_input_data)
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

        cont = input("\nWhat do you want to do now? [M]enu / [E]xit: ").strip().lower()
        if cont == 'e':
            print("Exiting... Catch you later! 👋")
            break

if __name__ == "__main__":
    run_decoder()
