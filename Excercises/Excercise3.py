def bomber_man(n, grid):
    grid = [[i for i in j] for j in grid]
    timers = [[0 if i == "O" else "." for i in j] for j in grid]

    # INCREMENTING TIMERS
    for i in range(0, n):
        timers = [[(q + 1) if q != "." else q for q in p] for p in timers]

        # PLANTING BOMBS
        if i != 0:
            timers = [[0 if m == "." else m for m in p] for p in timers]

        # REMOVING BOMBS ADJACENT TO EXPLODING BOMBS
        for q in range(len(grid)):
            for p in range(len(grid[0])):
                if timers[q][p] == 3:
                    timers[q][p] = "."
                    if q - 1 >= 0 and timers[q - 1][p] != 3:
                        timers[q - 1][p] = "."
                    if q + 1 <= len(timers) - 1 and timers[q + 1][p] != 3:
                        timers[q + 1][p] = "."
                    if p - 1 >= 0 and timers[q][p - 1] != 3:
                        timers[q][p - 1] = "."
                    if p + 1 <= len(timers[0]) - 1 and timers[q][p + 1] != 3:
                        timers[q][p + 1] = "."

        # # PRINT RESULT
        # for q in timers:
        #     for p in q:
        #         print(p,end=" ")
        #     print("\n")
        # print("---------")

        # REMOVING BOMBS WITH TIMER 3 (EXPLODING THEM)
        timers = [["." if m == 3 else m for m in p] for p in timers]
    return [''.join([str(j) for j in i]) for i in timers]


if __name__ == '__main__':
    seconds = int(input())
    gridRows = []
    while True:
        row = input()
        if row == "":
            break
        gridRows.append(row)
    for i in bomber_man(seconds, gridRows):
        print(i, end="\n")
