n = int(input())
res = {}

while True:
    word = input()
    if word == "":
        break
    if n <= 0:
        continue
    if word in res.keys():
        res[word] = res[word] + 1
    else:
        res[word] = 1
    n -= 1

print(len(res.keys()), end="\n")
for i in res.keys():
    print(res[i], end=" ")