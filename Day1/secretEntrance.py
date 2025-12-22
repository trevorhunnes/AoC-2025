def main():
    START_LOCATION = 50
    with open("./sequence.txt", "r") as file:
        sequence = file.readlines()

    print(get_code(sequence, START_LOCATION))


def get_code(sequence, start):
    count = 0
    location = start
    for code in sequence:
        # print(f"count : {count}")
        direction = code[0]
        distance = int(code[1:])

        if direction == "L":
            if location == 0:
                count -= 1
            location -= distance

        elif direction == "R":
            location += distance

        if location > 100:
            while location > 100:
                # print(location)
                count += 1
                location = location - 100

        elif location < 0:
            while location < 0:
                # print(location)
                count += 1
                location = 100 + location

        if location == 100:
            location = 0

        if location == 0:
            count += 1

    return count


main()
