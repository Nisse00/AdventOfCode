from isort import file


with open("input.txt", "r", encoding="UTF-8") as file:
    lines = file.readlines()

myMap = []
total = 0



for line in lines:
    temp = []
    for char in line:
        if char.isdigit():
            temp.append(char)
    myMap.append(int(temp[0])*10 + int(temp[len(temp)-1]))

for nbr in myMap:
    total += nbr

print(total)


