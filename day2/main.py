def day2_solution(input):
    horizontal_pos = 0
    depth = 0
    for item in input:
        (direction, value) = item.split()
        value = int(value)

        match direction:
            case "forward":
                horizontal_pos += value
            case "down":
                depth += value
            case "up":
                depth -= value

    return horizontal_pos * depth

def day2_solution_p2(input):
    horizontal_pos = 0
    depth = 0
    aim = 0

    for item in input:
        (direction, value) = item.split()
        value = int(value)

        match direction:
            case "forward":
                horizontal_pos += value
                depth += aim * value
            case "down":
                aim += value
            case "up":
                aim -= value

    return horizontal_pos * depth
