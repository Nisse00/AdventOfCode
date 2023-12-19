#Values
values = {
    "red": 12,
    "green": 13,
    "blue": 14
}

total = 0

#Handling the input
with open("test.txt", "r", encoding="UTF-8") as file:
    lines = file.readlines()

for gameline in lines:
    ok = True
    id_, line = gameline.split(":")
    for event in line.split(";"):
        for balls in event.split(","):
            n,color = balls.split()
            if int(n) > values.get(color,0):
                ok = False;
    if ok:
        total += int(id_.split()[1])
print(total)