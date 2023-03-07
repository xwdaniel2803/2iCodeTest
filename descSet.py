def readList():
    while True:
        print('Enter a whitespace-separated list of 10 numbers:')
        nums = input()
        try:
            numList = nums.split()
            for i in range(len(numList)):
                numList[i] = int(numList[i])
        except:
            print('Please input numerical values only.')
            continue
        if len(numList) != 10:
            print('Please enter 10 numbers exactly.')
            continue
        break
    return numList
    
def removeDuplicates(numList):
    uniqueList = []
    duplicates = 0
    for num in numList:
        if num not in uniqueList:
            uniqueList.append(num)
        else:
            duplicates += 1
        if duplicates == 4:
            break
    return uniqueList

def binarySearch(numList, x, left, right):
    if left == right:
        if numList[left] > x:
            return left
        else:
            return left + 1
    if left > right:
        return left
    mid = (left + right) // 2
    if numList[mid] < x:
        return binarySearch(numList, x, mid + 1, right)
    elif numList[mid] > x:
        return binarySearch(numList, x, left, mid - 1)
    else:
        return mid

def binarySort(numList):
    for i in range(1, len(numList)):
        x = numList[i]
        j = binarySearch(numList, x, 0, i - 1)
        numList = numList[:j] + [x] + numList[j:i] + numList[i+1:]
    return numList

def main():
    numList = readList()
    numList = removeDuplicates(numList)
    numList = binarySort(numList)
    numList = numList[::-1]
    print(numList)

if __name__ == "__main__":
    main()