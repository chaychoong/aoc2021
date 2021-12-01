def day1_solution(input):
    count = 0
    prev = input.pop(0)
    for item in input:
        if item > prev:
            count += 1
        prev = item

    return count

def day1_solution_p2(input):
    count = 0
    for i in range(3, len(input)):
        if input[i] > input[i-3]:
            count += 1

    return count
