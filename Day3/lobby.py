def main():
    with open("./batteryBanks.txt", "r") as file:
        banks = file.readlines()

    # banks = [
    #     "987654321111111",
    #     "811111111111119",
    #     "234234234234278",
    #     "818181911112111",
    # ]
    print(total_joltage(banks))


def get_jolts(joltages):
    joltages = joltages.replace("\n", "")
    jolts = [0] * 12
    position = 0
    for i in range(0, 12):
        position, jolts[i] = get_next_biggest(position, joltages, i)

    total = "".join(jolts)
    return int(total)


def total_joltage(banks):
    total = 0
    for bank in banks:
        # print(get_jolts(bank))
        total += get_jolts(bank)

    return total


def get_next_biggest(pointer, joltages, i):
    largest = 0
    count = pointer
    if i < 11:
        for c in joltages[pointer : -(11 - i)]:
            if int(c) > largest:
                largest = int(c)
                pointer = count

            count += 1

    else:
        for c in joltages[pointer:]:
            if int(c) > largest:
                largest = int(c)
                pointer = count

            count += 1
    pointer += 1
    return pointer, str(largest)


main()
