from random import randint

def sports_words():
	return ['athletics', 'baseball', 'basketball', 'bowling', 'cycling', 'football', 'golf', 'gymnastics', 'handball', 'hockey', 'jogging', 'polo', 'rugby', 'skiing', 'soccer', 'softball', 'squash', 'swimming', 'tennis', 'volleyball']

def hangman_game():
	# choose word that the user will guess

	# set the number of tries the user has

	print
	print 'Welcome to Hangman created by <NAME>'
	print 'Try to guess this sports related word:'
	print

	answer = ['_ '] * word_length
	print ''.join(answer)

	# loop while the user still has tries left
	
		guess_letter = raw_input('Guess a letter: ')

		# loop through each letter in the play word
		
			# check if the user guessed a letter in the play word
			

		print ''.join(answer)

		# check if the user has a guess for the word
		guess = raw_input('Do you know the word? (y/n) ')
		
			guess_word = raw_input('What is your guess? ')
			
				# if the user guessed correctly, they won
				
				break
			else:
				# if the user guessed incorrectly, they lose a try
				
		else:
			# if the user does not guess the word, they lose a try
			

	# if the user is all out of guesses they lose the game
	

	# ask the user if they want to play again
	

hangman_game()


