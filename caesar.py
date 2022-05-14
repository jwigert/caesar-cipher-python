shift_no = input("Please enter the number of places to shift: ")
while True:
	if not shift_no.isdecimal() or (int(shift_no) < 0 or int(shift_no) > 25):
		print("You need to enter a number between 0 and 25!")
		shift_no = input("Please enter the number of places to shift: ")
	else:
		shift_no = int(shift_no)
		break

plain_text = input("Please enter a sentence: ").lower()

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