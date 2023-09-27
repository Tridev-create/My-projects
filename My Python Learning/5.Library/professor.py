import random
import sys


def main():



    level = get_level()
    Count = 1
    Attempt = 0
    Score = 10

    while Count < 10:
        x, y, Result = generate_integer(level)
        while True:
            try:
                for i in range(3):
                    Conclusion = int(input(f"{x} + {y} = "))
                    if Conclusion == Result:
                        break
                    else:
                        pass
                        #print('EEE')
                        Attempt += 1
                        #print(Attempt)
                        if Attempt  == 3:
                            print(f"{x} + {y} = {Result}")
                            Score -= 1
                            Count += 1
                            Attempt = 0
                            break
                        break


            except ValueError:
                print('EEE')
                pass

            else:
                if Conclusion == Result:
                    #print('Count: ', Count)
                    Count += 1
                    Attempt = 0
                    if Count == 3:
                        print(f'Score: {Score}')
                    break

                else:
                    Attempt += 1
                    print('EEE')


                if Attempt == 3:
                    print(f"{x} + {y} = {Result}")
                    generate_integer(level)
                    Score -= 1
                    Count += 1
                    Attempt = 0
                    break

    print(f'Score: {Score}')


                #print(f"{x} + {y} = {Result}")
                #generate_integer(level)
                #Score += 1
                #if Score == 10:
                    #print(f'Score: {Score}')
                    #break
        #print(Result)
        #generate_integer()
        #print(x,y)

def get_level():
    while True:
        try:
            Lv = int(input('Level:'))
            if Lv > 3:
                raise ValueError('wrong')
        except ValueError as Lv: # This scope will automatically running when the program occured by error
            if str(Lv) == '-':
                pass
                int(Lv)
            else:
                pass
        else:
            if Lv < 4 and Lv > 0:
                return Lv
                break

def generate_integer(level):
    match level:
        case 1:

            x = random.randint(0, 9)
            y = random.randint(0, 9)
        case 2:
            x = random.randint(10, 99)
            y = random.randint(10, 99)
        case 3:
            x = random.randint(100, 999)
            y = random.randint(100, 999)
        case _:
            raise ValueError

    Result = x + y
    return x , y , Result


if __name__ == "__main__":
    main()