def get_data():
    with open("Day3.txt","r") as file:
        return file.readline()


def checkHouse(pos, visited):
    if (pos[0],pos[1]) in visited:
        visited[pos[0],pos[1]] += 1
    else:
        visited[pos[0],pos[1]] = 1


def nextMove(pos, move):
    if move == '^':
        pos[1] += 1
    elif move == 'v':
        pos[1] -= 1
    elif move == '>':
        pos[0] += 1
    else:
        pos[0] -= 1
    return pos

  
def task1(data):
    pos = [0,0]
    visited = {}
    checkHouse(pos, visited)
    for move in data:
        pos = nextMove(pos, move)
        checkHouse(pos, visited)
    print("Task 1: Unique Houses Visited: {}".format(len(visited)))

    
def task2(data):
    santaPos = [0,0]
    roboPos = [0,0]
    visited = {}
    checkHouse(santaPos,visited)
    
    for x in range(len(data)):
        if x%2 != 0:
            roboPos = nextMove(roboPos,data[x])
            checkHouse(roboPos,visited)
        else:
            santaPos = nextMove(santaPos,data[x])
            checkHouse(santaPos,visited)
            
    print("Task 2: Unique Houses Visited With Robo Santa: {}".format(len(visited)))



def main():
    data = list(get_data())
    task1(data)
    task2(data)


if __name__ == "__main__":
    main()
