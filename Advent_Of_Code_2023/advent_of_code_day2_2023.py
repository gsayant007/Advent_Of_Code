with open(r"Advent_Of_Code_2023\day2_input.txt","r") as f:
    games = f.readlines()

target_combo = (14,13,12)

game_dict = {
    x.split(":")[0] : [",".join([_ for _  in y.strip().split(", ")])    for y in x.split(":")[1].split(";")] for x in games}

print(game_dict)