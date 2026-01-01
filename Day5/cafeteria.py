def main():
    with open("./database.txt", "r") as file:
        database = file.read()

    ranges, ingredient_ids = split_database(database)
    print(get_count(ranges, ingredient_ids))


def split_database(database):
    database = database.split("\n\n")
    ranges = database[0].split("\n")
    ingredient_ids = database[1].split("\n")
    return ranges, ingredient_ids


def get_ranges(ranges):
    range_set = set()
    ranges = [c.split("-") for c in ranges]
    for x in ranges:
        for i in range(int(x[0]), int(x[1]) + 1):
            range_set.add(i)

    return range_set


def get_count(ranges, ingredient_ids):
    in_range = set()
    ranges = [c.split("-") for c in ranges]
    for x in ranges:
        for id in ingredient_ids[:-1]:
            if int(id) >= int(x[0]) and int(id) <= int(x[1]):
                print("made it")
                in_range.add(int(id))

    return len(in_range)


main()
