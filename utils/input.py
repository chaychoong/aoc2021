import ast

def parse_input(file_name):
    output = []
    with open(file_name, "r") as file_reader:
        for line in file_reader:
            try:
                parsed_line = ast.literal_eval(line) # without literal_eval, the lines will be read as strings
            except:
                parsed_line = line.rstrip("\n")

            output.append(parsed_line)

    return output

import ast

def parse_input_lambda(file_name, lambda_inp):
    output = []
    with open(file_name, "r") as file_reader:
        for line in file_reader:
            parsed_line = lambda_inp(line.rstrip("\n"))

            output.append(parsed_line)

    return output
