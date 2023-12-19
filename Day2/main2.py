total = 0
#Handling the input
with open("input.txt", "r", encoding="UTF-8") as file:
    lines = file.readlines()

for gameline in lines:
    id_, line = gameline.split(":")
    tempMax = {"red": 0, "green": 0, "blue": 0}
    for event in line.split(";"):
        for balls in event.split(","):
            n,color = balls.split()
            if int(n) > tempMax.get(color,0):
                tempMax.update({color:int(n)})
    tempTotal = 1
    for key,value in tempMax.items():
        tempTotal *= value
    total += tempTotal
print(total)
