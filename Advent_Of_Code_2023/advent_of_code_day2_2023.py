import numpy as np

with open(r"Advent_Of_Code_2023\day2_input.txt","r") as f:
    games = f.readlines()

target_combo = (14,13,12)

game_dict = {
    x.split(":")[0] : [",".join([_ for _  in y.strip().split(", ")])    for y in x.split(":")[1].split(";")] for x in games}


# Determine which games would have been possible if the bag had been loaded with only 
# 12 red cubes, 13 green cubes, and 14 blue cubes. What is the sum of the IDs of those games?

def sorting_bgr(s:str)->str:
    return ",".join(sorted(s.split(","),key=lambda x:x.split(" ")[1]))

def padding_bgr(s:str)->str:
    s1 = ""
    colors = set(["blue","green","red"])
    col_from_text = set(
        map(
        lambda x : x[1] , list(map(lambda x : x.split(" "),s.split(","))) ) )

    padding_colors = (colors - col_from_text) # remaining colors to be padded if not then pass
    # print(padding_colors)
    if padding_colors == set():
        return s
    else:
        for x in padding_colors:
            s = s +","+f"0 {x}"
        return s

def extract_bgr_coeff(s:str)->(int,int,int):
    return tuple([int(y.split(" ")[0]) for y in s.split(",")])


def target_comparison(g:tuple)->int:
    return int(
        any(x > y for x, y in zip(g, target_combo)))


game_dict_2 = {
    k:list(map(lambda x: sorting_bgr(padding_bgr(x)),v)) for k,v in game_dict.items()}

game_dict_3 = {k:list(map(lambda x:extract_bgr_coeff(x),v)) for k,v in game_dict_2.items()}

game_dict_4 = {
    k : list(map(lambda x : target_comparison(x),v)) for k, v in game_dict_3.items()}
game_dict_4 = {
    k : sum(v) for k,v in game_dict_4.items()
}

required_games = dict(
    filter(
        lambda x : x[1]==0, game_dict_4.items()
    )
).keys()

p1_ans = sum([int(y.split(" ")[1]) for y in required_games])

print(f"Answer for the first part is {p1_ans}")


d1 = {
    k : np.product([max(np.array(v)[:,0]),max(np.array(v)[:,1]),max(np.array(v)[:,2])][::-1])   for k,v in game_dict_3.items()
}

print(f"Answer for the second part is: {sum(d1.values())}")