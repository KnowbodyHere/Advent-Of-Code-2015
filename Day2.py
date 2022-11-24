def get_data():
    data = []
    with open("Day2.txt","r") as file:
        for line in file:
            line = line.strip("\n").split("x")
            for x in range(len(line)):
                line[x] = int(line[x])
            line.sort()
            data.append(line)
    return data


def find_slack_area(data):
    return 3*data[0]*data[1]+2*data[2]*(data[0]+data[1])

def find_ribbon_area(data):
    return 2*(data[0]+data[1])+data[0]*data[1]*data[2]


def main():
    data = get_data()
    slack_area = 0
    ribbon_area = 0
    for x in range(len(data)):
        slack_area += find_slack_area(data[x])
        ribbon_area += find_ribbon_area(data[x])


    print("Task 1: Total Slack Area needed: {}\nTask 2: Total Ribbon Area needed: {}".format(slack_area,ribbon_area))



if __name__ == "__main__":
    main()
