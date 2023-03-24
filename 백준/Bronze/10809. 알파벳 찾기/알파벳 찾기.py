S = input()
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
result = [-1] * 26
for i in range(len(S)):
    for j in range(len(alphabet)):
        if S[i] == alphabet[j] and result[j] == -1:
            result[j] = i
print(*result)