from random import randint 

def generate_number(valeu):
    number = randint(1,valeu)
    return number

def check_valeu(sub , valeu):
    if sub > 0 and sub <= valeu:
        return True
    else:
        return False
    
def play_one_game(count, valeu,level):

    
    print("welcome to the game level:", level)
    print("you have", count, "attempts to guess the number between 1 and", valeu)
        
        
    random_number = generate_number(valeu)
    won = False
    while  count > 0:

        
        try:
            submitted_number = int(input("entree you number:"))
            if check_valeu(submitted_number, valeu):

                if submitted_number == random_number:
                    print("wooow bro you win.")
                    won = True
                    break
                    
                    
                elif submitted_number < random_number:
                    print("your number is less than the random number")
                    count -= 1
                    print("mo7awalat ba9yn :", count)
                elif submitted_number > random_number:
                    print("your number is greater than the random number")
                    count -= 1
                    print("mo7awalat ba9yn :", count)
                   
            else:
                print("invalid number (must be between 1 and", valeu, ")")
                count -= 1
                print("mo7awalat ba9yn :", count)
        except ValueError:
                count -= 1
                print("invalid input")
                print("mo7awalat ba9yn :", count)
            

    if not won:
        print("game over")
        
                
    print("the number is:", random_number)
    
    return won

def play_game(count, valeu, level):


    while True:
        play_one_game(count, valeu, level)

        sub = input("do you want to play again? (y/n): ").strip().lower()
        if sub == "y":
            continue
        elif sub == "n":
            return 
        else:
            print("invalid choice (type y or n)")
