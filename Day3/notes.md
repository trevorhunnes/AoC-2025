# Lobby Puzzle

## Problems
- I need to make the largest number possible from left to right, not find the two largest numbers

>[!TIP] TODO:
> - [x] Get a function running that can extract the largest possible number from a string of numbers from left to right
> - [x] Write a function to go through each string of numbers and add the largest numbers together from each string
> - [x] Read file of strings into a list for each new line, and run that list through the adding function to get the total

---
>[!NOTE]
> The biggest number will always be first, unless the last number in the sequence is the biggest.
> In that case, the second biggest number will be first.

### Storing three numbers instead of two
- save 3 numbers
    - 88765432191
    - 8: 08
    - 8: 88
    - 7: 88
    - 6: 88
    - 5: 88
    - 4: 88
    - 3: 88
    - 2: 88
    - 1: 88
    - 9: 89
    - 1: 91

## Part Two
- Now I need to solve for twelve numbers instead of two.
    - The first number cannot be less than twelve numbers away from the end
    - each number after that can be one number closer
    - if the largest number starts in the 12 from last position, the largest number is the last 12 numbers
