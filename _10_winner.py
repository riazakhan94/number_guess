import time

def get_winner(p1, p2, count_1, count_2):
    print("=========================================")
    print(">>>>>>>>>>>>>> Final Result <<<<<<<<<<<<<<")
    print("=========================================")
    print(">>>> Calculating Final Result ...")
    time.sleep(1)
    print("=========================================")
    print("=========================================")
    time.sleep(2)
    print(f">>>> {p1} took {count_1} guess(es)")
    time.sleep(2)
    print(f">>>> {p2} took {count_2} guess(es)")
    time.sleep(2)
    time.sleep(1)
    if count_1 < count_2:
        print("*****************************************")
        print(f">>>>>  Winner is : {p1}")
        time.sleep(2)
        print(f"***** CONGRATULATIONS {p1}!")
    if count_1 > count_2:
        print("*****************************************")
        print(f">>>>>  Winner is : {p2}")
        time.sleep(2)
        print(f"***** CONGRATULATIONS {p2}!")
    
    if count_1 == count_2:
        print("*****************************************")
        print(f">>>>>  It's a DRAW!!!")
        time.sleep(2)
        print(f"***** Nice competition {p1} and {p2}")
    
    time.sleep(2)
    return()