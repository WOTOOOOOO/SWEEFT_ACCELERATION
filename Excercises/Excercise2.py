def bigger_Is_greater(w):
    if len(w) <= 1:
        return "no answer"
    res = ""
    #
    for i in range(len(w) - 1):
        if ord(w[len(w) - 2 - i]) < ord(w[len(w) - 1 - i]):
            mindif = 10000
            index = len(w) - 1 - i
            # find the element that needs to be swapped
            for j in range(len(w) - 1 - i, len(w)):
                if 0 < (ord(w[j]) - ord(w[len(w) - 2 - i])) < mindif:
                    mindif = ord(w[j]) - ord(w[len(w) - 2 - i])
                    index = j
            # here we swap the two characters and sort the last portion of the string (from the first index of the swap
            # to the end)
            res = w[:len(w) - 2 - i] + w[index]
            res += ''.join(sorted([char for char in (w[len(w) - 1 - i:index] + w[len(w) - 2 - i] + w[index + 1:])]))

            break
    return "no answer" if res == "" else res


if __name__ == '__main__':
    T = int(input())
    results = []
    while T > 0:
        results.append(bigger_Is_greater(input()))
        T -= 1
    for i in results:
        print(i, end="\n")
