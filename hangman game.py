import random

words = ["banana", "apple", "man", "girl"]
word = random.choice(words)
lives = 6
display = ["_"] * len(word)

while lives > 0 and "_" in display:
    print("Word:", " ".join(display))
    guess = input("Enter a letter: ").lower()

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                display[i] = guess
        print(" Correct guess!")
    else:
        lives -= 1
        print(" Wrong guess! Lives left:", lives)

if "_" not in display:
    print(" You win! The word was:", word)
else:
    print(" You lose! The word was:", word)
