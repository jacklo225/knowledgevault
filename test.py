def mergeSort(l):
    n = len(l)
    if n == 1:
        return l
    elif n == 2:
        return l if l[0] <= l[1] else [l[1], l[0]]

    mid = n // 2

    leftSorted = mergeSort(l[:mid])
    rightSorted = mergeSort(l[mid:])

    leftPointer = 0
    rightPointer = 0
    newPointer = 0

    new = [0] * n

    while leftPointer < len(leftSorted) and rightPointer < len(rightSorted):
        if leftSorted[leftPointer] <= rightSorted[rightPointer]:
            new[newPointer] = leftSorted[leftPointer]
            leftPointer += 1
        else:
            new[newPointer] = rightSorted[rightPointer]
            rightPointer += 1
        newPointer += 1

    while leftPointer < len(leftSorted):
        new[newPointer] = leftSorted[leftPointer]
        leftPointer += 1
        newPointer += 1

    while rightPointer < len(rightSorted):
        new[newPointer] = rightSorted[rightPointer]
        rightPointer += 1
        newPointer += 1

    return new

def quickSort(l):
    n = len(l)
    if n == 0: return l
    elif n == 1: return l
    elif n == 2: return l if l[0] <= l[1] else [l[1], l[0]]

    #optimization
    x = 0
    y = n//2
    z = n-1

    if l[x] > l[y]:
        l[x], l[y] = l[y], l[x]
    if l[x] > l[z]:
        l[x], l[z] = l[z], l[x]
    if l[y] > l[z]:
        l[y], l[z] = l[z], l[y]

    l[y], l[z] = l[z], l[y] #pointer goes to end


    pivotPointer = n-1

    smallerPointer = pivotPointer - 1
    largerPointer = 0

    while(smallerPointer > largerPointer):
        if l[smallerPointer] < l[pivotPointer] and l[largerPointer] > l[pivotPointer]:
            temp = l[smallerPointer]
            l[smallerPointer] = l[largerPointer]
            l[largerPointer] = temp
            smallerPointer -= 1
            largerPointer += 1
        elif l[smallerPointer] < l[pivotPointer]:
            largerPointer += 1
        elif l[largerPointer] > l[pivotPointer]:
            smallerPointer -= 1
        else:
            smallerPointer -= 1
            largerPointer += 1


    splitIndex = 0
    while(l[splitIndex] <= l[pivotPointer] and splitIndex < pivotPointer):
        splitIndex += 1

    left = quickSort(l[:splitIndex])
    right = quickSort(l[splitIndex:pivotPointer])

    return left + [l[pivotPointer]] + right

# from numpy import cbrt

def cubed(n):
    out = []

    map = {}

    for c in range(1, n):
        for d in range(1, n):
            sum = c ** 3 + d ** 3
            if not sum in map:
                map[sum] = []
            map[sum].append((c, d))

    for sum in map:
        pairs = map[sum]
        for a, b in pairs:
            for c, d in pairs:
                out.append((a, b, c, d))

    return out

# print(cubed(1000))

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1: ListNode, list2: ListNode) -> ListNode:
    if list1 == None: return list2
    if list2 == None: return list1

    new = ListNode()
    start = new

    while(list1 and list2):
        if list1.val < list2.val:
            new.next = list1
            list1 = list1.next
        else:
            new.next = list2
            list2 = list2.next
        new=new.next

    if list1:
        new.next = list1
    else:
        new.next = list2

    return start.next
