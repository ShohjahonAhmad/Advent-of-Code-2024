reports = []

with open("Day 2.txt", 'r') as f:
    for line in f.readlines():
        x = [int(z) for z in line.split()]
        reports.append(x)
# part 1      
def is_safe(l):
    n = len(l)
    return (all(1 <= l[i+1]-l[i] <= 3 for i in range(n-1))) or (all(1 <= l[i]-l[i+1] <= 3 for i in range(n-1)))
safe_count = sum(map(is_safe, reports))
print(safe_count)      
       
# safe_count = 0
# for report in reports:
#     n = len(report)
#     safe_count += (all(1 <= report[i+1]-report[i] <= 3 for i in range(n-1))) or (all(1 <= report[i]-report[i+1] <= 3 for i in range(n-1)))
# print(safe_count)

# part 2
safe_count2 = 0
for report in reports:
    n = len(report)
    safe_count2 += is_safe(report) or any(is_safe(report[:i] + report[i+1:]) for i in range(n))
print(safe_count2)
    