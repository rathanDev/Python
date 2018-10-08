
def sum(x, y):
    return x + y


def main():
    res = sum(2, 3)
    print('res => ', res)

main()






def recursiveSum(currentNum, accu):

    if currentNum == 11:
        return accu

    return recursiveSum(currentNum + 1, accu + currentNum)

def main():

    sum = recursiveSum(1, 0)
    print ('sum', sum)

# main()