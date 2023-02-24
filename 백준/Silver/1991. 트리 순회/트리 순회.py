import sys

def preorder(i):
    global result
    if i:
        result.append(i)
        preorder(left[i])
        preorder(right[i])

def inorder(i):
    global result
    if i:
        inorder(left[i])
        result.append(i)
        inorder(right[i])

def postorder(i):
    global result
    if i:
        postorder(left[i])
        postorder(right[i])
        result.append(i)


N = int(input())
parent = [0] * (N+1)
left = [0] * (N+1)
right = [0] * (N+1)

for n in range(N):
    p, l, r = sys.stdin.readline().split()
    p_num = ord(p) - 64

    if l != '.' and r != '.':
        l_num = ord(l) - 64
        r_num = ord(r) - 64

        left[p_num] += l_num
        parent[l_num] = p_num
        right[p_num] += r_num
        parent[r_num] = p_num
    elif l == '.' and r == '.':
        pass
    elif l == '.':
        r_num = ord(r) - 64
        right[p_num] += r_num
        parent[r_num] = p_num
    elif r == '.':
        l_num = ord(l) - 64
        left[p_num] += l_num
        parent[l_num] = p_num


result = []
preorder(1)
for i in result:
    print(chr(i + 64), end='')
print()

result = []
inorder(1)
for i in result:
    print(chr(i + 64), end='')
print()


result = []
postorder(1)
for i in result:
    print(chr(i + 64), end='')
print()