from moduls import *

def start():


    while True:
        print("\n========Guess Game========")
        print("1-play game")
        print("2-exit")
        try:
            sub = int(input("enter your choice:"))
            if sub == 1:
                print("\n========choice level========")
                print("1-easy")
                print("2-medium")
                print("3-hard")
                print("4-very hard")
                print("5-back to main menu")

                try:
                    level = int(input("enter your choice:"))
                    if level == 1:
                        play_game(3, 10, "easy")
                    elif level == 2:
                        play_game(3, 20, "medium")
                    elif level == 3:
                        play_game(4, 50, "hard")
                    elif level == 4:
                        play_game(5, 100, "very hard")
                        
                    elif level == 5:
                        continue
                    else:
                        print("invalid choice")
                except ValueError:
                    print("invalid input")
  
            elif sub == 2:
                print("good bye")
                break
            else:
                print("invalid choice")
        except ValueError:
            print("invalid input")
                  

if __name__ == "__main__":
    start()
