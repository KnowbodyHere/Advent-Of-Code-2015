def get_data():
    data = {}
    with open("Day7.txt","r") as file:
        for line in file:
            wire = line.rstrip().split(" -> ")
            data[wire[-1]] = wire[0].split()
    return data


def solve(node,data,solved):


    if node.isnumeric():
        return int(node)

    if node not in solved:

        operation = data[node]

        if len(operation) == 1:
            n = solve(operation[0],data,solved)

        else:
            op = operation[-2]
            if op == "AND":
              n = solve(operation[0],data,solved) & solve(operation[2],data,solved)
            elif op == "OR":
              n = solve(operation[0],data,solved) | solve(operation[2],data,solved)
            elif op == "NOT":
              n = ~solve(operation[1],data,solved) & 65535
            elif op == "RSHIFT":
              n = solve(operation[0],data,solved) >> solve(operation[2],data,solved)
            elif op == "LSHIFT":
              n = solve(operation[0],data,solved) << solve(operation[2],data,solved) & 65535

        solved[node] = n

    return solved[node]

def main():
    data = get_data()
    solved = {}
    a = solve("a",data,solved)

    data['b'] = [str(a)]
    solved = {}
    new_a = solve("a",data,solved)

    print("Task 1: a = {}\nTask2: new a = {}".format(a,new_a))


if __name__ == "__main__":
    main()
