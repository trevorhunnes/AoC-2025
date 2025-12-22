def main():
    with open("./idRanges.txt", "r") as file:
        ranges = file.read()

    ids = ranges.split(",")
    print(find_invalid_ids(ids))


def repeats(id):
    double_id = id + id
    return id in double_id[1:-1]


def check_range(x, y):
    x = int(x)
    y = int(y)
    total = 0
    for i in range(x, y + 1):
        if repeats(str(i)):
            total += i

    return total


def find_invalid_ids(ids):
    total = 0
    for id in ids:
        ranges = id.split("-")
        x = ranges[0]
        y = ranges[1]
        total += check_range(x, y)

    return total


main()
