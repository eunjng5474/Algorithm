def solution(commands):
    answer = []
    arr = [["EMPTY"] * 51 for _ in range(51)]
    merged = [[(i, j) for j in range(51)] for i in range(51)]
    
    for command in commands:
        com = command.split()
        if com[0] == "UPDATE":
            if len(com) == 4:
                r, c = map(int, com[1:3])
                x, y = merged[r][c]
                arr[x][y] = com[3]
            else:
                for i in range(1, 51):
                    for j in range(1, 51):
                        if arr[i][j] == com[1]:
                            arr[i][j] = com[2]
    
        elif com[0] == "MERGE":
            r1, c1, r2, c2 = map(int, com[1:])
            x1, y1 = merged[r1][c1]
            x2, y2 = merged[r2][c2]
            
            # (r1,c1)이 병합된 셀이 빈 값이면 (r2,c2) 병합 셀의 값 저장
            if arr[x1][y1] == "EMPTY":
                arr[x1][y1] = arr[x2][y2]
                
            for i in range(1, 51):
                for j in range(1, 51):
                    # merged에 저장된 값이 (r2,c2)가 병합되어 있는 셀(x2,y2)이면 모두 (r1,c1)이 병합된 셀(x1,y1)으로 변경
                    if merged[i][j] == (x2, y2):
                        merged[i][j] = (x1, y1)
        
        elif com[0] == "UNMERGE":
            r, c = map(int, com[1:3])
            x, y = merged[r][c]
            tmp = arr[x][y]
            
            for i in range(1, 51):
                for j in range(1, 51):
                    # (r,c)가 병합된 (x,y)와 병합되어 있는 셀이면
                    # arr는 EMPTY로, merged에는 다시 본인으로 바꾸기
                    if merged[i][j] == (x, y):
                        arr[i][j] = "EMPTY"
                        merged[i][j] = (i, j)
            arr[r][c] = tmp

        else:
            r, c = map(int, com[1:3])
            x, y = merged[r][c]
            answer.append(arr[x][y])
        
    return answer