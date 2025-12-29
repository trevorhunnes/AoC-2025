def main():
    with open("./paper-grid.txt", "r") as file:
        grid = file.readlines()

    count = 0
    last_count = 0
    removed = []
    while True:
        last_count, removed = get_count(grid)
        if last_count == 0:
            break
        count += last_count
        for c in removed:
            my_string = grid[c[0]]
            index = [c[1]]
            grid[c[0]] = my_string[: index[0]] + "." + my_string[index[0] + 1 :]

    print(count)


def get_count(grid):
    count = 0
    removed = []
    for x in range(0, len(grid)):
        # print(grid[x])
        for y in range(0, len(grid[x])):
            if grid[x][y] == "@":
                if is_accessable(grid, x, y):
                    removed.append([x, y])
                    count += 1

    return count, removed


def is_accessable(grid, x, y):
    count = 0

    try:
        if x != 0 and grid[x - 1][y - 1] == "@":
            count += 1
    except IndexError:
        pass
    try:
        if x != 0 and grid[x - 1][y] == "@":
            count += 1
    except IndexError:
        pass
    try:
        if x != 0 and grid[x - 1][y + 1] == "@":
            count += 1
    except IndexError:
        pass
    try:
        if y != 0 and grid[x][y - 1] == "@":
            count += 1
    except IndexError:
        pass
    try:
        if grid[x][y + 1] == "@":
            count += 1
    except IndexError:
        pass
    try:
        if y != 0 and grid[x + 1][y - 1] == "@":
            count += 1
    except IndexError:
        pass
    try:
        if grid[x + 1][y] == "@":
            count += 1
    except IndexError:
        pass
    try:
        if grid[x + 1][y + 1] == "@":
            count += 1
    except IndexError:
        pass

    if count < 4:
        return True
    else:
        return False


main()
