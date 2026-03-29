n = int(input())
switches = list(map(int, input().split()))

m = int(input())
students = []
for _ in range(m):
    s, num = map(int, input().split())
    students.append((s, num))

def toggle(num):
    if num == 1:
        return 0
    else:
        return 1

def boy(switch_num, switches):
    for i in range(1, len(switches) + 1):
        if i % switch_num == 0:
            switches[i-1] = toggle(switches[i-1])
    
def girl(switch_num, switches):
    l, r = switch_num-1, switch_num-1
    while l - 1 >= 0 and r + 1 <= len(switches)-1 and switches[l - 1] == switches[r + 1]:
        l -= 1
        r += 1
    for i in range(l, r + 1):
        switches[i] = toggle(switches[i])

for sex, num in students:
    if sex == 1:
        boy(num, switches)
    else:
        girl(num, switches)

for i in range(n // 20):
    print(*switches[i*20:i*20+20])
print(*switches[n // 20 * 20:])