#%% 
import time
import random as rd
from getpass import getpass

from _01_akp import any_key_proceed
from _02_snp import set_n_players
from _03_in_pnames import input_pnames
from _04_set_init_params import set_init_params
from _05_set_tn2p import set_target_num_2p
from _06_set_tnc import set_target_by_computer
#from _07_gn import guess_num
from _08_nreq2 import calc_nguess_req_2p
from _09_nreqc import calc_nguess_req_computer
from _10_winner import get_winner
from _11_wc import welcome_note
from _12_close import game_close




#%%
welcome_note()

print("==========================================")
print(">>>> Alright.... Now setting the stage ...")
print("==========================================")
time.sleep(2)


print("------------------------------------------")
print(">>>> Setting number of players ...")
time.sleep(2)
n_pl = set_n_players()



print("------------------------------------------")
print(">>>> Setting player names ...")
time.sleep(2)
p_names = input_pnames(n_pl)
p1 = p_names[0]
p2 = p_names[1]

print("------------------------------------------")
print(">>>> Setting initial parameters ...")
time.sleep(2)
init_params = set_init_params()
n1 = init_params[0]
n2 = init_params[1]



print("------------------------------------------")
print(" >>> All set. The game starts now ....")
print("------------------------------------------")


if n_pl == 2:
    time.sleep(2)
    ps = p1
    pg = p2
    tmp_target = set_target_num_2p(ps, pg, n1, n2)
    count_2 = calc_nguess_req_2p(n1, n2, tmp_target, ps, pg)
    print("------------------------------------------")
    print(" >>> Time to switch role ....")
    print("------------------------------------------")
    time.sleep(2)
    ps = p2
    pg = p1
    tmp_target = set_target_num_2p(ps, pg, n1, n2)
    count_1 = calc_nguess_req_2p(n1, n2, tmp_target, ps, pg)

if n_pl == 1:
    time.sleep(2)
    ps = p2
    pg = p1
    tmp_target = set_target_by_computer(n1, n2)
    count_1 = calc_nguess_req_2p(n1, n2, tmp_target, ps, pg)
    print("------------------------------------------")
    print(" >>> Time to switch role ....")
    print("------------------------------------------")
    time.sleep(2)
    ps = p1
    pg = p2
    tmp_target = set_target_num_2p(ps, pg, n1, n2)
    count_2 = calc_nguess_req_computer(n1, n2, tmp_target, ps)


get_winner(p1, p2, count_1, count_2)
game_close()


