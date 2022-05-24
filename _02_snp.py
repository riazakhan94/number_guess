import time

def set_n_players():
    tmp_sts = 0
    while tmp_sts == 0:
        n_pl = input("Input the number of players (1 or 2) : ")
        try:
            n_pl = int(n_pl)
            tmp_sts = 1
            if not ((n_pl == 1) | (n_pl == 2)):
                raise ValueError("Not a valid input, try again...")
                tmp_sts = 0
        except ValueError:
            print("Not a valid input, try again...")
            tmp_sts = 0
    
    print("Saving number of palyers (thanks for patience) ...")
    time.sleep(1)
    print(">>> Number of players saved successfully.") 
    return(n_pl)