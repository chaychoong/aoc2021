import ast

def parse_input(file_name):
    output = []
    with open(file_name, "r") as file_reader:
        for line in file_reader:
            output.append(ast.literal_eval(line)) # without literal_eval, the lines will be read as strings

    return output
