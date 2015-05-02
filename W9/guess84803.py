 # Name - Kakali Mahapatra
    # Student ID - 84803
    # Program for guessing game


def main():
    print('Welcome to the number guessing game')
    print('For each game, you have 4 chances to guess a secret number from 1 to 12.')
    print('')

    wins = 0
    losses = 0
    totalgames = 0

    while(True):
        user_input = input('Enter a number from 1 to 12. Enter X to exit:')
        print('')
        try:
            user_input = int(user_input)
        except ValueError:
            # String was passed probabaly X, check needs to be done
            if(user_input=='X' or 'x'):
                print('Here is your game summary:')
                print('Total games:             ' + str(totalgames))
                print('Total game wins:         ' + str(wins))
                print('Total game losses:       ' + str(losses))
                exit()
            else:
                print('Wrong input, Program existing ...')
                exit()

        # Import Random module to help generate random number
        import random
        random_number = random.randrange(1,13)

        totalgames = totalgames + 1
        trials = 1
        while(random_number!=user_input and trials<4):
            trials = trials + 1
            user_input = int(input('Not correct, try again:'))

        if(trials==4 and random_number!=user_input):
            losses = losses + 1
            print('Not correct. You have reached your fourth trials. The correct number is '
                  + str(random_number) + '.')
            print('Lets start a new secret number')
            print('')


        if(random_number==user_input):
            wins = wins + 1
            print('Congratulation, correct! Lets start a new secret number.')
            print('')



##if __name__ == "__main__":
main()
