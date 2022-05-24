import time

def input_pnames(n_pl):
    print(">>>> Players")
    if n_pl == 1:
        p1 = input("Type player name (player 1): ")
        p2 = "Computer"
    else:
        p1 = input("Playre 1 name : ")
        p2 = input("Playre 2 name : ")
    print("Saving player names (thanks for patience) ...")
    time.sleep(1.5)
    print(f">>> Player {p1} and {p2} are saved successfully.") 
    return(p1, p2)