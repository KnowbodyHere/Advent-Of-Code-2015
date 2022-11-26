import hashlib

def MD5(data):
    return hashlib.md5(data.encode()).hexdigest()

def check(test,length):
    return (True if test[:length] == "0"*length else False)

def main():
    data = <Input You Data>

    found5 = False
    found6 = False

    answer = 0
    while True:
        answer += 1
        test = MD5(data+str(answer))
        if check(test,5) and not found5:
            print("Task 1: code = {}".format(answer))
            found5 = True


        if check(test,6) and not found6:
            print("Task 2: code = {}".format(answer))
            found6 = True

        if found5 and found6:
            break



if __name__ == "__main__":
    main()
