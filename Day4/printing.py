def main():
    with open("./paper-grid.txt", "r") as file:
        grid = file.readlines()

    print(get_count(grid))


def get_count(grid):
    count = 0
    for x in range(0, len(grid)):
        # print(grid[x])
        for y in range(0, len(grid[x])):
            if grid[x][y] == "@":
                if is_accessable(grid, x, y):
                    # print(x, y)
                    count += 1

    return count


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
