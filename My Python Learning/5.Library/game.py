import sys
def main():

    ans = manage_ans()

    guess = manage_guess()

    match ans:
        case 22:
            print('Too large!')
        case 5:
            print('Too small!')
    match guess:
        case 4:
            print('Just right!')
            sys.exit()

def manage_ans():
    while True:
        try:
            ans = int(input('Level:'))
            if ans < 0:
                raise ValueError('wrong')
        except ValueError as ans: # This scope will automatically running when the program occured by error
            if str(ans) == '-':
                pass
                int(ans)
            else:
                pass
        else:
            if ans > 0:
                return ans
                break

def manage_guess():
    while True:
        try:
            guess = int(input('Guess:'))
            if guess < 0:
                raise ValueError('wrong')
        except ValueError as guess:
            if str(guess) == '-':
                pass
                int(guess)
            else:
                pass
        else:
            if guess > 0:
                return guess
                break

main()
