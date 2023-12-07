with open(r"Advent_Of_Code_2023\day1_input.txt","r") as f:
     words = f.readlines()

num_list_2 = ["one","two","three","four","five","six","seven","eight","nine"]
words_to_num = {w : str(i) for i, w in enumerate(num_list_2,start=1)}
p1 = []
def first_part(s:str)->list:
    l = [y for y in s if y.isdigit()]
    num = int(l[0]+l[-1])
    return num

for x in words:
   p1.append(first_part(x))

print(f"Answer for the first part is: {sum(p1)}")


p2 = []
def second_part(s:str)->str:
        l = []
        for i in range(len(s)):
          if s[i].isdigit():
               l.append(s[i])
          for x in num_list_2:
               if s[i:].startswith(x):
                    l.append(words_to_num[x])
        return l

for x in words:
     p2.append(
          second_part(x))
     

# print(p2[0])
p2_ans = sum(
     list(
          map(
               lambda l : int(l[0]+l[-1]) , p2
          )
     )
)
print(f"answer for the second part is: {p2_ans}")