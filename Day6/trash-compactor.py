def main():
    with open("./input.txt", "r") as file:
        input = file.readlines()

    clean_input = cleanInputs(input)
    print(len(clean_input))
    total = calcTotals(clean_input)
    print(total)


def cleanInputs(input):

    clean_input = []

    for x in range(0, len(input)):
        clean_input.append(input[x].split())
        if x < (len(input) - 1):
            for y in clean_input[x]:
                y = int(y)

    for y in clean_input[len(input) - 1]:
        y.strip()

    return clean_input


def calcTotals(input):
    total = 0
    for x in range(0, len(input[0])):
        result = 0
        if input[-1][x] == "*":
            result = (
                int(input[0][x])
                * int(input[1][x])
                * int(input[2][x])
                * int(input[3][x])
            )

        if input[-1][x] == "+":
            result = (
                int(input[0][x])
                + int(input[1][x])
                + int(input[2][x])
                + int(input[3][x])
            )

        total += int(result)

    return total


main()
