def calculate(operator, operand1, operand2):
    x, y = int(operand1), int(operand2)
    if operator == "x" and y == 0:
        return 0
    if operator == "x":
        return x * y
    elif operator == "+":
        return x + y
    elif operator == "-":
        return x - y
    elif operator == "/":
        return x / y
    
def compute_lines_in_file():
    start_index = len("calc ")
    total = 0
    with open("/Users/kchima/Documents/Corndel/step_2.txt") as file_to_process:
        for line in file_to_process:
            operator, x, y = line[start_index:].split()
            result = calculate(operator, x, y)
            total += result
    return total

def process_goto_file():
    with open("/Users/kchima/Documents/Corndel/step_3.txt") as goto_file:
        lines = goto_file.readlines()
    statements = []
    index, goto_index = 0, len("goto ")
    while True:
        line = lines[index]
        print(statements, line)
        words = line[goto_index:].split()
        if len(words) == 1:
            statement = int(words[0])
        elif "calc " in words:
            statement = int(calculate(words[1], words[2], words[3]))
        print(f"current value={statement}")
        if statement in statements:
            return (line, index+1)
        else:
            statements.append(statement)
            index = statement - 1


if __name__ == "__main__":
    print(process_goto_file())