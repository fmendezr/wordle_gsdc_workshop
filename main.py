from random import choice

class Game:
    def __init__(self) -> None:
        self.words = ['about', 'alert', 'argue', 
                    'beach', 'brain', 'carry', 'claim', 'cream',
                    'brand', 'class', 'dance', 'dated',	'dealt',
                    'debut', 'entry', 'risky', 'worth', 'stuff',
                    ]                       
        self.hidden_word = choice(self.words)
        self.attempt = 6

        self.game_loop()

    def give_instructions(self):
        print('''\n Wordle is a single player game. 
              A player has to guess a 5 letter word.
              You have six attempts.
              Your progress guide "✔xx✔+"
              "✔" = letter at that position was guesses correctly
              "+" = Letter is in the word but another position
              "x" = Letter is not in the word. 
        ''')

    def check_word(self, guess):
        if self.hidden_word == guess:
            print("You've WON 🎉 🎊 🥳\nYou guessed the word correctly!\n") 
            return True
        else:
            result = ''
            for i, j in zip(guess, self.hidden_word):
                if i == j:
                    result += '✔'
                elif i in self.hidden_word:
                    result += '+'
                else:
                    result += 'x'
            print(result)
            return False
            
    def game_loop(self):
        self.give_instructions()
        while self.attempt > 0:
            guess = str(input("\nGuess the word: ")).lower()
            if self.check_word(guess=guess):
                break
            else:
                self.attempt  -= 1
                print(f'You have {self.attempt} attempts left.')
        else:
            print(f'\nSorry, you lost!\nThe word was {self.hidden_word}')

Game()