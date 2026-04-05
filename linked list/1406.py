import sys
input = sys.stdin.readline

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

s = str(input().rstrip())
m = int(input())

head = ListNode(s[0])
cur_node = head
for i in range(1, len(s)):
    new_node = ListNode(s[i])
    cur_node.next = new_node
    cur_node = cur_node.next

def find_previous(target_node):
    curr = head
    prev = None
    while curr:
        if curr == target_node:
            return prev
        prev = curr
        curr = curr.next
    return None

for _ in range(m):
    inst = str(input().rstrip())
    if len(inst) > 1:
        p, ch = map(str, inst.split())
        new_node = ListNode(ch)
        new_node.next = cur_node.next
        cur_node.next = new_node
    if inst == 'L':
        curr = find_previous(cur_node)
        print(curr.val)
        if curr:
            cur_node = curr
        else:
            cur_node = head


ans = ''
while head:
    ans += head.val
    head = head.next
print(ans)