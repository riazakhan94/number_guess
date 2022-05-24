
def guess_num(n_low, n_high):    
    tmp_sts = 0
    while tmp_sts == 0:
        n_pred = input(f"Guess (whole number in between {n_low} and {n_high}): ")
        try:
            n_pred = int(n_pred)
            tmp_sts = 1
            if not ((n_pred > n_low) & (n_pred < n_high)):
                raise ValueError("Not a valid input, try again...")
                tmp_sts = 0
            
        except ValueError:
            print("Not a valid input, try again...")
            tmp_sts = 0
    return(n_pred)