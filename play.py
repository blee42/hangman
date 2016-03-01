from random import randint

def hangman_game():
	word_list = open('wordlist.txt', 'r')
	words = word_list.readlines()
	number = randint(0,19)

	tries = 7

	print
	print 'Welcome to Hangman created by Brittany'
	print 'Try to guess this sports related word:'
	print

	play_word = words[number].strip()
	word_length = len(play_word)

	answer = ['_ '] * word_length
	print ''.join(answer)

	while tries > 0:
		guess_letter = raw_input('Guess a letter: ')

		for i in range(0,word_length):
			if play_word[i] == guess_letter:
				answer[i] = guess_letter + ' '  

		print ''.join(answer)

		guess = raw_input('Do you know the word? (y/n) ')
		if guess == 'y':
			guess_word = raw_input('What is your guess? ')
			if guess_word == play_word:
				print 'You won!'
				break
			else:
				'Not quite, but keep trying!'
				tries-=1
		else:
			tries-=1

	if tries <= 0:
		print 'Out of guesses :('
		print 'The word was ' + play_word

	play_again = raw_input('Do you want to play again? (y/n)')
	if play_again == 'y':
		hangman_game()

hangman_game()


