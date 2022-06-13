# Author: Victoria Wiegand
# Sources: Danial Bekhit, https://github.com/lindseyyu/evilhangman/blob/master/hangman.py,
#   https://stackoverflow.com/questions/1228299/changing-one-character-in-a-string

class Hangman:
  	# set up dictionary into list
    words = []
    with open('dictionary.txt', 'r') as file:
        for line in file:
            info = line
            words.append(str.strip(info))

    def __init__(self):
        pass

    def __str__(self):
        pass

    def play(self):
        # set up game variable
        letters_guessed = []

        # prompt for word length and input validation
        word_size = (input("How long would you like the word to be? "))
        word_size = int(self.int_validation(word_size))
        words_remaining = self.guessable_words(word_size)

        # prompt for number of guesses and input validation
        num_guess = input("How many guesses would you like? ")
        num_guess = int(self.int_validation(num_guess))

        # prompt for words_remaining view and input validation
        guess_view = str(input("Would you like to see remaining guesses? yes or no "))
        while not(guess_view == 'yes' or guess_view == 'no'):
            guess_view = input("Please enter a valid input, yes or no: ")

        # display game parameters
        print("Length of Word: ", word_size)
        print("Number of Guesses Left:", num_guess)
        print("\n")

        # set up representation
        representation = "_" * word_size
        representation = list(representation)

        # start of game
        win = False
        winner = ""
        while win == False:
            # check number of guesses
            if num_guess == 0:
                win = True
                winner = "computer"
            elif "_" not in representation:
                win = True
                winner = "player"
            # user starts entering letters
            else:
                # letter input validation
                letter = input("Please Guess a Letter: ")
                while not(letter.isalpha() and len(letter) == 1):
                    letter = input("Please enter a valid input: ")
                while letter in letters_guessed:
                    letter = input("You have already guessed this letter. Please enter another one: ")
                letters_guessed.append(letter)

                # create word families
                keys, words_remaining = self.word_families(words_remaining, letter)

                # print representations
                keys_list = []
                keys_list[:0] = keys
                for i in range(len(keys_list)):
                    if keys_list[i] == letter:
                        representation[i] = letter
                print("".join(representation))

                # decrement guesses
                if not(representation.__contains__(letter)):
                    num_guess -= 1


                # display guesses left remaining guesses
                print("Letters Guessed: ", letters_guessed)
                print("Number of Guesses Left: ", num_guess)
                if guess_view == 'yes':
                    print("Remaining Guesses: ", words_remaining)

        # game results
        if winner == "computer":
            print("Sorry, you lost.")
        else:
            print("Congratulations, you guessed the word, " + words_remaining[0] + '!')

    def guessable_words(self, size):
        ' Returns list of guessable words of the size specified by the player '
        sized_words = []
        for i in self.words:
            if len(i) == int(size):
                sized_words.append(i)
        return sized_words

    def int_validation(self, string):
        ' Prompts the user for a string that is a positive integer and returns that string if valid '

        while string.isnumeric() == False or string == "0":
            string = input("Please enter an integer greater than 0: ")
        return string

    def word_families(self, list, guess):
        ' Returns the largest word family for words_remaining along with the word representation'
        families = {}
        rep = [] # show word dashes
        sort = [] # to sort the families
        final_sorted = {}

        # create dictionary for letter sequence
        for word in list:
            families[word] = ""
            for letter in word:
                if letter != guess:
                    families[word] += "_"
                if letter == guess:
                    families[word] += guess

        # make list of letter sequences, not repeated
        for key in families:
            rep.append(families[key])
        for i in rep:
            if i not in sort:
                sort.append(i)

        # dictionary of representations as key and list of words as the value
        for item in sort:  # will make a dict with the representations as the key and a list of words for the value
            final_sorted[item] = []
            for key in families:
                if families[key] == item:
                    final_sorted[item] += [key]

        # dictionary of final_sorted except value is the number of words for a representation
        len_dict = {}
        for key in final_sorted:
            len_dict[key] = len(final_sorted[key])

        # find largest list of representations
        largest_key = 0
        for key in len_dict:
            if len_dict[key] > largest_key:
                largest_key = len_dict[key]
        # find representation of largest_key
        for key in final_sorted:
            if len(final_sorted[key]) == largest_key:
                largest_key = key

        # return the representation with the largest possible words and the list of those words
        return largest_key, final_sorted[largest_key]