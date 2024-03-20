def solution(record):
    answer = []
    name = dict()
    for r in record:
        lst = list(r.split())
        if len(lst) == 3:
            name[lst[1]] = lst[2]
    
    for r in record:
        lst = list(r.split())
        if lst[0] == "Enter":
            answer.append(name[lst[1]]+"님이 들어왔습니다.")
        elif lst[0] == "Leave":
            answer.append(name[lst[1]]+"님이 나갔습니다.")
    
    return answer