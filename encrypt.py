import string

alphabet = string.ascii_letters
punctuation = string.punctuation
encrypt = {" ":53}

i = 1
for letter in alphabet:
	encrypt[letter] = i 
	i = i + 1 
z = 54
for punc in punctuation:
	encrypt[punc] = z
	z = z + 1

def encrypt_message():
	message = "Talia rules" #raw_input("What message would you like to encrypt?")
	for i in range(len(message)):
		print encrypt[message[i]]

def decrypt_message():
	message = "1 12 9 1 53"  #int(raw_input("Decrypt a message."))
	for i in range(len(message)):
		if encrypt[key] == message[i]:
			print key



decrypt_message()