
def displayMenu():
    return "The Menu\n1) Count Digits\n2) Find Max\n3) Count Tags\n4) Count Normalized Columns\n5) Recursive Binary Search\n6) Recursive Binary Search on 2d Matrix\n7) Exit"


def main():
    print(displayMenu())
    choice = int(input("choose your desired function to run: "))
    while choice < 7:
        if (choice == 1):
            number = int(input('choose an integer: '))
            print(countDigits(number))
        elif (choice == 2):
            lst = []
            lst_length = int(
                input('choose the size of the list you wish to search for its max val: '))
            for _ in range(lst_length):
                n = int(input('add int: '))
                lst.append(n)
            print(findMax(lst))
        elif (choice == 3):
            markup = ''
            tag = 'li'
            print(countTags(markup, tag))
        elif (choice == 4):
            matrix = [
                [-1.2649110640673518, 5.123451, 43],
                [-0.6324555320336759, 5.13123123, 4334],
                [0.0, 6.1543453, 125879],
                [0.6324555320336759, 0.1231235709, 123544],
                [1.2649110640673518, 9.1543524234, 55676]
            ]
            print(countNormalizedCols(matrix))
        elif (choice == 5):
            lst2 = []
            n = int(input('please enter the list length: '))
            for _ in range(n):
                num = int(
                    input('enter desired integers in ascending order: '))
                lst2.append(num)
            target = int(input('choose target to search for: '))
            print(binarySearch(lst2, 0, len(lst2)-1, target))
        elif (choice == 6):
            bs_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
            target = 5
            print(binarySearchInMatrix(bs_matrix, 0, len(bs_matrix)-1, target))
        else:
            print("Invalid choice")

        print(displayMenu())
        choice = int(input("Enter your choice: "))

    exit()

# &  Question 1:
# &--------------


def countDigits(num):
    if(num<0): return countDigits(-num)
    if (num < 10):
        return 1
    return 1 + countDigits(num//10)

# ^  Question 2:
# ^--------------

def findMax(lst):
    if len(lst) == 0:
        return 'list is empty'
    elif len(lst) == 1:
        return lst[0]
    else:
        sliced_list_max = findMax(lst[1:])
        if lst[0] > sliced_list_max:
            return lst[0]
        else:
            return sliced_list_max

# ?  Question 3:
# ?--------------


def countTags(markup, tag, count=0):
    if len(markup) == 0:
        return count
    close_tag = f"</{tag}>"
    close_tag_idx = markup.find(close_tag)
    if (close_tag_idx == -1):
        return count
    else:
        count += 1
        return countTags(markup[close_tag_idx+1:], tag, count)


# *  Question 4:
# *--------------

def calcMean(lst):
    X_bar = len(lst)
    if (X_bar != 0):
        total = sum(lst)
        mean = total/X_bar
        return mean


def calcStd(lst):
    mean = calcMean(lst)
    X_bar = len(lst)
    diff = 0
    for x in lst:
        diff += (x - mean)**2
    variance = diff/(X_bar-1)
    return variance**0.5


def isNormalized(lst):
    if (calcMean(lst) == 0 and calcStd(lst) == 1):
        return True
    return False


def countNormalizedCols(matrix, col=0, count=0):
    if (col >= len(matrix[0])):
        return count
    temp_col = []
    for row in matrix:
        temp_col.append(row[col])
    if isNormalized(temp_col):
        count += 1
    return countNormalizedCols(matrix, col+1, count)

#!  Question 5:
#!--------------


def binarySearch(lst, low, high, target):

    while (low <= high):
        mid = (low+high) // 2
        if (lst[mid] == target):
            return mid
        elif (lst[mid] > target):
            return binarySearch(lst, low, mid-1, target)
        else:
            return binarySearch(lst, mid+1, high, target)
    return -1


# ~  Question 6:
# ~--------------

def binarySearchInMatrix(matrix, low, high, target):

    while (low <= high):
        mid = (low + high) // 2
        sublist = matrix[mid]

        if target in sublist:
            col = binarySearch(sublist, 0, len(sublist)-1, target)
            return f"The element is at row: {mid} , column: {col}"
        else:
            if sublist[0] > target:
                return binarySearchInMatrix(matrix, low, mid-1, target)
            elif sublist[-1] < target:
                return binarySearchInMatrix(matrix, mid+1, high, target)

    return 'target not found'


def exit():
    print('exited')


main()
