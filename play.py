from random import randint
import urllib2

def hangman_game():
	# choose word that the user will guess
	word_list = urllib2.urlopen('http://brittanyalee.com/sample_files/wordlist.txt')
	words = word_list.readlines()
	number = randint(0,19)
	play_word = words[number].strip()
	word_length = len(play_word)

	# set the number of tries the user has
	tries = 7

	print
	print 'Welcome to Hangman created by Brittany'
	print 'Try to guess this sports related word:'
	print

	answer = ['_ '] * word_length
	print ''.join(answer)

	# loop while the user still has tries left
	while tries > 0:
		guess_letter = raw_input('Guess a letter: ')

		# loop through each letter in the play word
		for i in range(0,word_length):
			# check if the user guessed a letter in the play word
			if play_word[i] == guess_letter:
				answer[i] = guess_letter + ' '  

		print ''.join(answer)

		# check if the user has a guess for the word
		guess = raw_input('Do you know the word? (y/n) ')
		if guess == 'y':
			guess_word = raw_input('What is your guess? ')
			if guess_word == play_word:
				# if the user guessed correctly, they won
				print 'You won!'
				break
			else:
				# if the user guessed incorrectly, they lose a try
				'Not quite, but keep trying!'
				tries-=1
		else:
			# if the user does not guess the word, they lose a try
			tries-=1

	# if the user is all out of guesses they lose the game
	if tries <= 0:
		print 'Out of guesses :('
		print 'The word was ' + play_word

	# ask the user if they want to play again
	play_again = raw_input('Do you want to play again? (y/n) ')
	if play_again == 'y':
		hangman_game()

hangman_game()


