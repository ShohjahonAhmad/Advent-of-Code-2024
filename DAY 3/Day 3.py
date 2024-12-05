import re 

with open ("Day 3.txt", "r") as f:
    memory = f.read()
    memory = memory.replace(" ", "")
def mul(data):
    pattern = re.compile(r'mul\((\d{1,3}),(\d{1,3})\)')

    matches = pattern.finditer(data)

    result = 0
    for match in matches:
        a = match.group(1)
        b = match.group(2)
        result += int(a) * int(b)
    return result
# part 1
print(mul(memory))
# part 2
clean_data = ""
i = 0
do = True
while i < len(memory):
    if do:
        if memory[i:i+5] == "don't":
            do = False
            i += 7
        else:
            clean_data += memory[i]
            i += 1
    else:
        if memory[i:i+4] == "do()":
            do = True
            i += 4
        else:
            i += 1
print(mul(clean_data))
    