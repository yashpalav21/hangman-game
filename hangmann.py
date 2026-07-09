import random
words = ("apple", "banana", "cherry", "lemon", "mango")
#dictionary
hangman_art = {0: ("   "
                   "   ",
                   "   "),
               1: (" o ",
                   "   ",
                   "   "),
               2: (" o ",
                   " |  ",
                   "   "),
               3: (" o ",
                   "/| ",
                   "   "),
               4: (" o ",
                   "/|\\",
                   "   "),
               5: (" o ",
                   "/|\\",
                   "/  "),
               6: (" o ",
                   "/|\\",
                   "/ \\")}
def display_man(wrong_guesses):
    print("+++++++++++++")
    for line in hangman_art[wrong_guesses]:
        print(line)
    print("+++++++++++++")
def display_hint(hint):
    print(" ".join(hint))


def display_word(answer):
    pass

def main():
   answer = random.choice(words)
   hint = "_" * len(answer)
   wrong_guesses = 0
   guessed_letters = set()
   is_running = True


   while is_running:
         display_man(wrong_guesses)
         display_hint(hint)
         display_word(answer)
         guess = input("guess a letter: ").lower()
         answer == guess
         break

         if len(guess) != 1 or not guess.isalpha():
             print("Please enter a single letter.")
             continue
         
         if guess in answer:
           for i in range(len(answer)):
             if answer[i] == guess:
               hint[i] = guess
               break
if __name__ == "__main__":
    main()