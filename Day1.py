##Day 1
def get_data():
    with open("Day1.txt","r") as file:
        return file.readline()

def find_floor(f,d):
    pos = 0
    basement_found = False
    
    for x in range(len(d)):
        if d[x] == "(":
            f += 1
        elif d[x] == ")":
            f -= 1

        pos += 1
        if f == -1 and not basement_found:
            basement_found = True
            print("Task 2: Reached basement at position: {}".format(pos))

    print("Task 1: Floor located at {}".format(f))

def main():
    data = list(get_data())

    floor = 0
    find_floor(floor,data)
    

if __name__ == "__main__":
    main()
