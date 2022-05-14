import sys

def show_help():
	print("This program encrypts a plain text by using the Caesar cipher.")
	print("The program needs to be called with two arguments:")
	print("Argument 1: The plain text")
	print("Argument 2: The number of places to shift (in the range 0 to 25)")
	print("Example: python3 caesar.py \"this is the plain text\" 3")

if len(sys.argv) != 3:
	show_help()
	exit()

shift_no = sys.argv[2]
if not shift_no.isdecimal() or (int(shift_no) < 0 or int(shift_no) > 25):
	print("You need to enter a number between 0 and 25!")
	exit()
shift_no = int(shift_no)

plain_text = sys.argv[1].lower()

cipher_text = ""

alphabet = "abcdefghijklmnopqrstuvwxyz"

for plain_char in plain_text:
	if plain_char in alphabet:
		plain_char_index = alphabet.find(plain_char)
		encrypted_char_index = (plain_char_index + shift_no) % 26
		encrypted_char = alphabet[encrypted_char_index]
		cipher_text += encrypted_char
	else:
		cipher_text += plain_char

print("The encrypted sentence is: " + cipher_text)