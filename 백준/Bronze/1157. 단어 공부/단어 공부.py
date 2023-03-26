alphabet = {'a': 0, 'b':0, 'c':0, 'd':0, 'e':0, 'f':0, 'g':0, 'h':0, 'i':0, 'j':0, 'k':0, 'l':0,
'm':0, 'n':0, 'o':0, 'p':0, 'q':0, 'r':0, 's':0, 't':0, 'u':0, 'v':0, 'w':0, 'x':0, 'y':0, 'z':0}
word_inp = input()
word = word_inp.lower()
for w in word:
    for a in alphabet:
        if w == a:
            alphabet[a] += 1

result = sorted(alphabet.items(), key=lambda x:x[1], reverse=True)
if result[0][1] == result[1][1]:
    print('?')
else:
    print(str(result[0][0].upper()))