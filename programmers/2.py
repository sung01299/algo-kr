'''
오픈채팅방
Simulation
'''
from collections import defaultdict
def solution(record):
    uid_name = defaultdict(str)
    answer = []
    res = []
    for rec in record:
        msg = rec.split(' ')
        if len(msg) == 3:
            cmd, uid, name = msg[0], msg[1], msg[2]
            uid_name[uid] = name
        else:
            cmd, uid = msg[0], msg[1]
        if cmd == 'Enter':
            res.append((0, uid))
        elif cmd == 'Leave':
            res.append((1, uid))
        else:
            uid_name[uid] = name
            
    for msg in res:
        cmd, uid = msg
        if cmd == 0:
            answer.append(f'{uid_name[uid]}님이 들어왔습니다.')
        else:
            answer.append(f'{uid_name[uid]}님이 나갔습니다.')
    
    return answer