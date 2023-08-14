from random import choice

class tcol:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

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
        print(f'''\n Wordle is a single player game. 
              A player has to guess a 5 letter word.
              You have six attempts.
              Your progress guide "✔xx✔+"
              "{tcol.OKCYAN}{tcol.BOLD}A{tcol.ENDC}" = letter at that position was guesses correctly
              "{tcol.FAIL}{tcol.BOLD}A{tcol.ENDC}" = Letter is in the word but another position
              "{tcol.UNDERLINE}A{tcol.ENDC}" = Letter is not in the word. 
        ''')

    def check_word(self, guess):
        if self.hidden_word == guess:
            print("You've WON 🎉 🎊 🥳\nYou guessed the word correctly!\n") 
            return True
        else:
            result = ''
            for i, j in zip(guess, self.hidden_word):
                if i == j:
                    result += f'{tcol.OKCYAN}{tcol.BOLD}{i}{tcol.ENDC}'
                elif i in self.hidden_word:
                    result += f'{tcol.FAIL}{tcol.BOLD}{i}{tcol.ENDC}'
                else:
                    result += f'{tcol.UNDERLINE}{i}{tcol.ENDC}'
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
