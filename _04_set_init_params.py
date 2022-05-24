
import time

def set_init_params():
    tmp_sts = 0
    while tmp_sts == 0:
        n1 = input("Lower number (whole number) : " )
        n2 = input(f"Upper number (whole number, bigger than {n1} by at least 10) : ")

        try:
            n1 = int(int(n1))
            n2 = int(int(n2))
            tmp_sts = 1
            if not (n2 - n1 >= 10):
                raise ValueError("Inputs are not valid, try again...")
                tmp_sts = 0
            
        except ValueError:
            print("Inputs are not valid, try again...")
            tmp_sts = 0
    
    print("Saving the numbers (thanks for patience) ...")
    time.sleep(1.5)
    print(f">>> {n1} and {n2} saved successfully.")
    return(n1, n2)