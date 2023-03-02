N = int(input())
seat = input()
result = ['*']

i = 0
while i < N:
    if seat[i] == 'S':
        result.append('S')
        result.append('*')
        i += 1
    elif seat[i] == 'L' and seat[i+1] == 'L':
        result.append('L')
        result.append('L')
        result.append('*')
        i += 2

cnt = 0
for i in range(1, len(result)):
    if result[i] == 'S' or result[i] == 'L':
        if result[i-1] == '*':
            cnt += 1
            result[i-1] = '/'
        elif result[i+1] == '*':
            cnt += 1
            result[i+1] = '/'

print(cnt)