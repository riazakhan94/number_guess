import time
import random as rd


def set_target_by_computer(n1, n2):
    print("Computer is setting the target number ...")
    time.sleep(2)
    x = rd.randint(n1 + 1, n2 - 1)
    print(">>>> Target set by computer successfully.")
    return(x)
  