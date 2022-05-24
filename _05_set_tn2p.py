import time
from getpass import getpass

def set_target_num_2p(ps, pg, n1, n2):
    print(f"{ps}, set the target number in between {n1} and {n2}")
    print(f"{pg} will try to guess the number you set")
    print(f"Do not worry, {pg} will not see/know about it while you type")
    print(f"Do not include {n1} or {n2}")
    
    tmp_sts = 0
    while tmp_sts == 0:
        x = getpass("Target Number: ")
        try:
            x = int(x)
            tmp_sts = 1
            if not ((x > n1) and (x < n2) and x == int(x)):
                raise ValueError("Invalid input")
                print("Invalid input!")
                print(f"Input either not a number, "
                f"or number not a whole number in between {n1} and {n2}")
                print("Try again...")
                tmp_sts = 0
        except ValueError:
            print("Invalid input!")
            print(f"Input either not a number, "
            f"or number not a whole number in between {n1} and {n2}")
            print("Try again...")
            tmp_sts = 0
        
    print(f">>>> Nice job {ps}! Your number has been set.")
    time.sleep(2)
    return(x)