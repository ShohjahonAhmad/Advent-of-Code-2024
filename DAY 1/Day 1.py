from collections import Counter

left, right = [], []

with open("Day1.txt", 'r') as f:
    for line in f.readlines():
        x, y = (int(z) for z in line.split())
        left.append(x)
        right.append(y)
left.sort()
right.sort()
        
print(left)
print(right)

n = len(right)
# part 1
print(sum(abs(left[i] - right[i]) for i in range(n)))

c = Counter(right)
# part 2
print(sum(c[left[i]] * left[i] for i in range(n)))