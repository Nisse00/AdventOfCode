from isort import file


with open("input.txt", "r", encoding="UTF-8") as file:
    lines = file.readlines()

myMap = []
total = 0

word_to_digit = {
    "zero": '0',
    "one": '1',
    "two": '2',
    "three": '3',
    "four": '4',
    "five": '5',
    "six": '6',
    "seven": '7',
    "eight": '8',
    "nine": '9',
}

for line in lines:
    temp = []
    tempChar = ""
    for index, char in enumerate(line):
        tempChar = ""
        if char.isdigit():
            temp.append(char)
        else:
            should_break = False
            for i in range (index,len(line)):
                if not line[i].isdigit():
                    tempChar += line[i]
                    for key, value in word_to_digit.items():
                        if tempChar == key:
                            should_break = True
                            print(tempChar)
                            temp.append(value)
                            break
                    if(should_break):
                        break

    myMap.append(int(temp[0])*10 + int(temp[len(temp)-1]))

for nbr in myMap:
    total += nbr

print(total)


