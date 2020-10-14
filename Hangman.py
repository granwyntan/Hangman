from random_words import RandomWords

library = RandomWords()

word = library.random_word()

print("Hangman")
print()

guesses = set()
noMoreVowels = False
chancesLeft = len(word)

while chancesLeft > 0:    
    wordIsFull = True
    for char in word: 
        if char in guesses:
                print(char, end=" ")       
        else: 
            print("_", end=" ")
            wordIsFull = False
    print()
    if wordIsFull == True:
        print("You Got it!")
        print("The word was:", word) 
        break
    print()
    guess = input("Guess a character: ")
    # print(guesses)
    if guess.isalpha() and len(guess) == 1:
        if guess in guesses:
            print("Character has been guessed before")
        guesses.add(guess)
        if guess not in word:
            print("Wrong")
            chancesLeft -= 1
            if noMoreVowels == False:
                if {'a', 'e', 'i', 'o', 'u'} in guesses or guesses == {'a', 'e', 'i', 'o', 'u'}:
                    print("\nNo more vowels\n")
                    noMoreVowels = True
            
            if chancesLeft > 1:
                print("You have", + chancesLeft, 'more guesses/chances left')
            elif chancesLeft == 1:
                print("You have", + chancesLeft, 'more guess/chance left')
            else:
                print("Try Harder Next Time!")
                print("The word was:", word)
            print()
        else:
            print()
    else:
        print("Invalid Input")
        print()
