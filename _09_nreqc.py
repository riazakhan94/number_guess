import time
import random as rd


def calc_nguess_req_computer(n1, n2, n_target, ps):
    print()
    print(f"{ps}, computer will now guess the number set by you.")   
    time.sleep(2)
    tmp_guess = rd.randint(n1+1, n2-1)
    print(f"Computer's first guess is {tmp_guess}")
    time.sleep(2)
    if(n_target == tmp_guess):
        print("Bingo! The computer is a gunius! "
        f"Got {n_target} right on it's first attempt.")
        time.sleep(2)
        return(1)
    g_count = 1
    while tmp_guess != n_target:           
        if(tmp_guess < n_target):
            time.sleep(2)
            print(f"Looks like {tmp_guess} is too low")
            time.sleep(1)
            print(f"Number of guesses so far : {g_count}")
            time.sleep(1)
            g_count = g_count + 1
            print("-----------------------------------------")
            print("Computer re-thinking ...")            
            time.sleep(1)
            n1 = tmp_guess
            print(f"Guessing in between {n1} and {n2} ...")
            time.sleep(1)
            tmp_guess = rd.randint(n1+1, n2-1)
            print(f"Computer's next guess is : {tmp_guess}")
            time.sleep(2)

        if(tmp_guess > n_target):
            time.sleep(2)
            print(f"Looks like {tmp_guess} is too high")
            time.sleep(1)
            print(f"Number of guesses so far : {g_count}")
            time.sleep(1)
            g_count = g_count + 1
            print("-----------------------------------------")
            print("Computer re-thinking ...")
            time.sleep(2)
            n2 = tmp_guess
            print(f"Guessing in between {n1} and {n2} ...")
            time.sleep(1)
            tmp_guess = rd.randint(n1+1, n2-1)
            print(f"Computer's next guess is : {tmp_guess}")
            time.sleep(2)
        

    time.sleep(2)
    print("=========================================")
    print("=========================================")
    print(f"Number of guesses Computer took : {g_count}")
    time.sleep(2)
    print("\n\n")
    return(g_count)