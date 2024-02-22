# Question 1:
def printIsocel(n):
    stars = ''
    for num in range(1, 2*n):
        if (num <= n):
            stars += '*'
            print(stars)
        else:
            stars = stars[0:len(stars)-1]
            print(stars)

printIsocel(6)
# ------------------------------------------------------------------------------------------

# Question 2:
def printEvensInBetween():
    if (n2 <= n1):
        print("first number can't be bigger than the second")
    else:
        for num in range(n1, n2+1):
            if (num % 2 == 0):
                print(num, end=' ')

n1 = int(input('enter first number: '))
n2 = int(input('enter second number: '))

printEvensInBetween()
# ------------------------------------------------------------------------------------------

# Question 3:

# for loop:
def reverseString(string):
    reversed = ''
    for ltr in string:
        reversed = ltr + reversed
    return reversed

# Recursive:
def reverseWithRecursion(string):
    if (len(string) == 0):
        return string
    else:
        return string[len(string)-1:] + reverseString(string[:len(string)-1])

print(reverseString('Hello World1'), reverseWithRecursion('Hello World2'))
# ------------------------------------------------------------------------------------------

# Question 4:
def filterEvens():
    evenNums = []
    for num in lst:
        if (num % 2 == 0):
            evenNums.append(num)
    print(evenNums)

lst = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
    elem = int(input())
    lst.append(elem)

filterEvens()
#------------------------------------------------------------------------------------------

# Question 5:
def validateIPv4(s):
    octets = s.split('.')
    
    if len(octets) < 4:
        return 'IP invalid: missing octet(s)'
    elif len(octets) > 4:
        return 'IP invalid: extra octet(s)'

    for octet_str in octets:
        if(octet_str == ''):
            return 'IP invalid: consecutive periods'

        octet = int(octet_str)

        if (octet < 0):
            return 'IP invalid: negative number'
        elif (octet > 255):
            return 'IP invalid: octet value too big'
        elif (octet_str[0] == '0' and len(octet_str) > 1):
            return 'IP invalid: leading zero in octet'

    return 'IP Valid'

s = input('Enter the IP address you wish to validate: ')

print(validateIPv4(s))
#----------------------------------------------------------------------------------------------