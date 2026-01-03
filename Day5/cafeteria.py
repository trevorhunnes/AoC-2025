clean_ranges: list[list[int]] = []


def main():
    with open("./database.txt", "r") as file:
        database = file.read()

    int_ranges: list[list[int]] = []
    ranges: list[str] = []
    ingredient_ids: list[str] = []

    ranges, ingredient_ids = split_database(database)
    for x in ranges:
        split_ranges: list[int] = list(map(lambda y: int(y), x.split("-")))
        int_ranges.append(split_ranges)
    for c in sorted(int_ranges, key=lambda x: x[0]):
        add_range(c)
    print(get_count(clean_ranges))


def add_range(input_range: list[int]) -> None:
    global clean_ranges
    i: int = 0
    if clean_ranges == []:
        clean_ranges.append(input_range)
    else:
        for clean_range in clean_ranges:
            i += 1
            if input_range[0] >= clean_range[0] and input_range[0] <= clean_range[1]:
                if input_range[1] <= clean_range[1]:
                    break
                else:
                    clean_range[1] = input_range[1]
                    break
            elif input_range[1] >= clean_range[0] and input_range[1] <= clean_range[1]:
                clean_range[1] = input_range[1]
            elif input_range[0] < clean_range[0] and input_range[1] > clean_range[1]:
                clean_range[0] = input_range[0]
                clean_range[1] = input_range[1]
            elif i == len(clean_ranges):
                clean_ranges.append(input_range)


def split_database(database: list[str]) -> tuple(list[str], list[str]):
    database = database.split("\n\n")
    ranges = database[0].split("\n")
    ingredient_ids = database[1].split("\n")
    return ranges, ingredient_ids


def optomize_ranges(ranges):
    optomized_ranges = []
    ranges = [c.spliy("-") for c in ranges]
    ranges = [(int(item[0]), int(item[1])) for item in ranges]


def get_count(ranges):
    in_range = set()
    count = 0
    for x in ranges:
        count += (int(x[1]) - int(x[0])) + 1

    return count


main()
