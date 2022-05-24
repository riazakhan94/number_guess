
import time
from _07_gn import guess_num

def calc_nguess_req_2p(n1, n2, n_target, ps, pg):
    #print("Time for guessing!")
    print("-----------------------------------------")
    print(f"{pg}, guess the number {ps} has set as target.")
    # initial_guess:
    tmp_guess = guess_num(n1, n2)
    if tmp_guess == n_target:
        print(f"Congratulations {pg}!")
        time.sleep(2)
        print("You've guessed it right in your first attempt.")
        time.sleep(2)
        return(1)

    g_count = 1 #guess count

    while tmp_guess != n_target:
        print("-----------------------------------------")
        if(n_target > tmp_guess):
            print(f"{tmp_guess} too low. Try again ...")
            n1 = tmp_guess
            tmp_guess = guess_num(n1, n2)
            g_count = g_count + 1
        
        if(n_target < tmp_guess):
            print(f"{tmp_guess} too high. Try again ...")
            n2 = tmp_guess
            tmp_guess = guess_num(n1, n2)
            g_count = g_count + 1
        print(f"Number of guesses so far : {g_count}")
    time.sleep(2)
    print(f"Nice Job {ps}! {tmp_guess} was the number that {pg} set.")
    print("=========================================")
    print("=========================================")
    print(f"Number of guesses {pg} took : {g_count}")
    print("\n\n")
    return(g_count)