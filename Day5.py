def get_data():
    data = []
    with open("Day5.txt","r") as file:
        for line in file:
            data.append(line.strip("\n"))
    return data


  
def vowel3(string):
    vowel = ["a","e","i","o","u"]
    vowelCount = 0

    for x in range(len(string)):
        if string[x] in vowel:
            vowelCount += 1

        if vowelCount >= 3:
            return True

def doubleLetter(string):
    for x in range(len(string)-1):
        if string[x] == string[x+1]:
            return True
    return False

def notContaining(string):
    return sum(map(string.count, ['ab', 'cd', 'pq', 'xy'])) == 0

def task1(data):
    nicestrings = 0
    for string in data:
        if vowel3(string) and doubleLetter(string) and notContaining(string):
            nicestrings += 1
    print("Task 1: Nice strings = {}".format(nicestrings))


    
def repeats(string):
    for x in range(len(string)-2):
        if string[x] == string[x+2]:
            return True
    return False

def doubleTwice(string):
    for x in range(len(string)-3):
        double = string[x] + string[x+1]

        for y in range(x+2,len(string)-1):
            check = string[y]+string[y+1]
            if check == double:
                return True
    return False

def task2(data):
    niceStrings = 0
    for string in data:
        if repeats(string) and doubleTwice(string):
            niceStrings += 1
    print("Task 2: New system nice strings = {}".format(niceStrings))


    
def main():
    data = get_data()
    
    task1(data)
    task2(data)

if __name__ == "__main__":
    main()
