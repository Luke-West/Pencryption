#17/05/2015
#Author: LTW
#A program to encrypt and decrypt input data.

import string
import random
import os

numberstaken = []
lettersandnumber = []
letterrepresentations = []

def writefile():
	'''If there is already a file with encrypted reps in, leave this
	function alone. Otherwise, put it in the program under create reps 
	and remove it as soon as you have the encryption.txt file.'''
	with open('encryption1.txt', 'w') as f:
		for word in letterrepresentations:
			words = str(word + "\n")
			f.write(words)

def createrep():
	'''Use this in conjunction with write file if there is not encrypted .txt file
	This will create 100 representations for each ascii letter. It should be deleted from
	the program as soon as there is an encryption file otherwise the program will get confused'''

	for letter in string.ascii_letters:
		representations = []
		numberofreps = 0
		while numberofreps < 100:
			letters = list(string.ascii_letters)
			wordlength = random.randint(7, 25)
			currentwordlength = 0
			word = ""
			while currentwordlength < wordlength:
				randomletter = random.randint(1,50)
				word += letters[randomletter]
				currentwordlength = currentwordlength + 1
			if word not in letterrepresentations:
				representations.append(word)
				numberofreps = numberofreps + 1
				letterrepresentations.append(word)


def letterstonumbers(findnumber):
	'''This converts decrypted text to a number which can then be used to encrypt the text data'''
	position = 0
	i = list(string.ascii_letters[position])
	position = string.ascii_letters.find(findnumber) + 1
	position = position * 100
	randomsequence = random.randint(position, (position+100))
	while randomsequence > 5200:
		randomsequence = random.randint(position, (position+100))
	return(int(randomsequence))

def numbertoletters(number):
	'''This is used to find the letter given to the representation'''
	numberactual = int((number/100)-1)
	return(list(string.ascii_letters[numberactual]))

def importreps():
	'''This is used to import the encryption data and should remain in the program at all times'''
	with open("encryption1.txt", 'r') as f:
		for char in f:
			letterrepresentations.append(char[:-1])
			
def encryptinput(message):
	'''Used to convert the data into an encrypted format. This calls severl other functions and procedures in
	order to execute properly'''
	listoverallmessage = []
	overallmessage = str("")
	for char in list(message):
		if char not in string.ascii_letters:
			listoverallmessage.append(char)
			listoverallmessage.append("$^&")
		else:
			listoverallmessage.append(letterrepresentations[letterstonumbers(char)])
			listoverallmessage.append("$^&")
	for i in listoverallmessage:
		overallmessage += str(i)
	return(overallmessage)

def decryptinput(word):
	'''Used to return the letter equivelent to the partly decrypted data'''
	if word == "None":
		pass
	elif word in list(string.punctuation) or word in list(string.digits) or word in list(string.whitespace):
		return word
	else:
		position = 0
		while word != letterrepresentations[position]:
			position = position + 1
		return (numbertoletters(position))

def overalldecryption(sequence):
	'''Part of the decryption process'''
	message = []
	overallmessage = ""
	splitmessage = sequence.split('$^&')
	for char in splitmessage:
		message.append(decryptinput(char))
	for letter in message:
		try:
			overallmessage += str(letter[0])
		except:
			overallmessage += str(" ")
	return overallmessage

if __name__ == "__main__":
	if not os.path.exists('encryption1.txt'):
	   createrep()
	   writefile()
	print("Welcome to LWEM. Ensuring your message reach's its destination securely.")
	importreps()
	print('''
		Would you like to encrypt or decrypt? 

		(A) encrypt

		(B) decrypt
		''')
	answer = input()
	if answer == 'a' or answer == 'A':
		print("Please enter something to encrypt")
		answer2 = input()
		print("Here is your encryption:")
		print(encryptinput(answer2))

	elif answer == 'b' or answer == 'B':
		print("Please enter something to decrypt")
		answer2 = input()
		print('''
			Here is what the message reads:
			''')
		print(overalldecryption(answer2[:-3]))
		print('''''')

	else:
		print("Please try again.")

