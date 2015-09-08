#!/usr/bin/env python
#Author: LTW
#a program to encrypt and decyrption


import string
import random
import sqlite3
import os


numberstaken = []
lettersandnumber = []
b = 5300
letterrepresentations = []


def writefile():
	with open('encryption1.txt', 'w') as f:
		for word in letterrepresentations:
			words = str(word + "\n")
			f.write(words)


def createrep():
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
	position = 0
	i = list(string.ascii_letters[position])
	while i != list(findnumber):
		i = list(string.ascii_letters[position])
		position = position + 1
	position = position * 100
	randomsequence = random.randint(position, (position+100))
	while randomsequence > 5200:
		randomsequence = random.randint(position, (position+100))
	return(int(randomsequence))

def numbertoletters(number):
	numberactual = int((number/100)-1)
	return(list(string.ascii_letters[numberactual]))

def importreps():
	with open("encryption1.txt", 'r') as f:
		for char in f:
			letterrepresentations.append(char[:-2])
		print(len(letterrepresentations))

def encryptinput(message):
	listoverallmessage = []
	overallmessage = str("")
	for char in list(message):
		if char not in string.ascii_letters:
			listoverallmessage.append(char)
			listoverallmessage.append(",")
		else:
			listoverallmessage.append(letterrepresentations[letterstonumbers(char)])
			listoverallmessage.append(",")
	for i in listoverallmessage:
		overallmessage += str(i)
	return(overallmessage)

def decryptinput(word):
	if word == "None":
		pass
	elif word == " ":
		pass
	else:
		position = 0
		while word != letterrepresentations[position]:
			position = position + 1
		return (numbertoletters(position))


def overalldecryption(words):
	message = []
	overallmessage = ""
	splitmessage = words.split(',')
	for char in splitmessage:
		message.append(decryptinput(char))
	for letter in message:
		try:
			overallmessage += str(letter[0])
		except:
			overallmessage += str(" ")
	return overallmessage


def encrypt(demand):
	for i in string.ascii_letters:
		numberletter = random.randint(1, 10000)
		if numberletter in numberstaken:
			numberletter = random.randint(1, 10000)
			numberstaken.append(numberstaken)
			n = numberletter
			lettersandnumber.append((i, n))


if __name__ == "__main__":
	print("Welcome to LWEM, here to ensure your message reach's its destination securely.")
	importreps()
	print('''Would you like to encrypt or decrypt? 
		(A) encrypt
		(B) decrypt
		''')
	answer = input()
	if answer == 'a' or answer == 'A':
		print("Please enter something to encrypt")
		answer2 = input()
		print("Here is your encryption:")
		print(encryptinput(answer2))

	else:
		print("Please enter something to decrypt")
		answer2 = input()
		print('''
			Here is what the message reads:
			''')
		print(overalldecryption(answer2[:-1]))
		print('''''')

