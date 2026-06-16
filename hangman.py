import random
name=input("Enter Your Name: ")
print(f"\nWelcome To Hangman Game,{name}!\n")
fruits=["apple","orange","mango","banana","watermelon","strawberry","grape","kiwi","Cherry"]
tech=["Smartphone","Laptop","Keyboard","Mouse","Scanner","Camera"]
word=fruits+tech
word=random.choice(word)
guessed = ["_"] * len(word)
print(" ".join(guessed))
attempts=6
while attempts>0 and "_" in guessed:
    guess=input("Guess a letter: ")
    if guess in word:
        print("Great! Correct Guess ")
        for i in range(len(word)):
            if word[i]==guess:
                guessed[i]=guess
    else:
        print("Wrong Guess! Try Again")
        attempts-=1
        print("Attempts Left :" ,attempts)
    print("".join(guessed))
if "_" not in guessed:
    print(f"\nCongratulations {name},YOU WON")
else:
    print(f"\nGame Over {name},the word was : " ,word)
print("\nThanks For Playing",name)

 
    