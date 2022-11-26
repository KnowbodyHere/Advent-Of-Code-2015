def get_data():
    data = []
    with open("Day6.txt","r") as file:
        for line in file:
            line = line.strip("\n").strip("turn ").split(" ")
            line.pop(2)
            line[1] = line[1].split(",")
            line[1] = [int(line[1][0]),int(line[1][1])]
            line[2] = line[2].split(",")
            line[2] = [int(line[2][0]), int(line[2][1])]
            data.append(line)
    return data




def create_table():
    table = []
    for row in range(1000):
        line = []
        for col in range(1000):
            line.append(False)
        table.append(line)
    return table


def do_step(com,table):
    Function = com[0]
    From = com[1]
    To = com[2]


    if Function == "on":
        for x in range(From[0],To[0]+1):
            for y in range(From[1],To[1]+1):
                table[x][y] = True

    elif Function == "off":
        for x in range(From[0],To[0]+1):
            for y in range(From[1],To[1]+1):
                table[x][y] = False

    else:
        for x in range(From[0],To[0]+1):
            for y in range(From[1],To[1]+1):
                table[x][y] = not table[x][y]
    return table

def count_table(table):
    count = 0
    for x in range(len(table)):
        for y in range(len(table[x])):
            if table[x][y]:
                count += 1
    return count

def task1(data):
    table = create_table()

    for command in data:
        table = do_step(command,table)

    print("Task 1: Total Lights On = {}".format(count_table(table)))




def create_bright_table():
    table = []
    for row in range(1000):
        line = []
        for col in range(1000):
            line.append(0)
        table.append(line)
    return table

def do_bright_step(com,table):
    Function = com[0]
    From = com[1]
    To = com[2]

    if Function == "on":
        for x in range(From[0], To[0] + 1):
            for y in range(From[1], To[1] + 1):
                table[x][y] += 1

    elif Function == "off":
        for x in range(From[0], To[0] + 1):
            for y in range(From[1], To[1] + 1):
                table[x][y] -= 1
                if table[x][y] < 0:
                    table[x][y] = 0

    else:
        for x in range(From[0], To[0] + 1):
            for y in range(From[1], To[1] + 1):
                table[x][y] += 2
    return table

def count_bright_table(table):
    count = 0
    for x in range(len(table)):
        for y in range(len(table)):
            count += table[x][y]
    return count

def task2(data):
    table = create_bright_table()
    for command in data:
        table = do_bright_step(command,table)
    print("Task 2: Total Brightness = {}".format(count_bright_table(table)))



def main():
    data = get_data()
    task1(data)
    task2(data)

if __name__ == "__main__":
    main()
