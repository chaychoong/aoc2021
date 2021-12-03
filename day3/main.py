def day3_solution(input):
    bits_arr = [0]*len(input[0])

    for line in input:
        for i in range(len(line)):
            bits_arr[i] += int(line[i])

    mcb_arr = []
    lcb_arr = []

    for i in bits_arr:
        is_mcb = (2*i) > len(input)

        mcb_arr.append("1" if is_mcb else "0")
        lcb_arr.append("0" if is_mcb else "1")

    mcb_int = int("".join(mcb_arr), 2) # this ia python trick to convert a binary to an int
    lcb_int = int("".join(lcb_arr), 2)

    return mcb_int*lcb_int

def day3_solution_p2(input):
    input = list(set(input))

    mcb_inp = input[:] # makes a copy by value, without referencing the original

    for i in range(len(mcb_inp[0])):
        mcb = '1' if 2*sum([int(x[i]) for x in mcb_inp]) >= len(mcb_inp) else '0'

        mcb_inp = list(filter(lambda x : x[i] == mcb, mcb_inp))

        if len(mcb_inp) == 1:
            break

    mcb_int = int(mcb_inp[0], 2)

    lcb_inp = input[:]

    for i in range(len(lcb_inp[0])):
        lcb = '0' if 2*sum([int(x[i]) for x in lcb_inp]) >= len(lcb_inp) else '1'
        lcb_inp = list(filter(lambda x : x[i] == lcb, lcb_inp))
        if len(lcb_inp) == 1:
            break

    lcb_int = int(lcb_inp[0], 2)

    return mcb_int * lcb_int
