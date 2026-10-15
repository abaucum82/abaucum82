from itertools import combinations

#find all valid sets based on digits
def digitFinder(initRange,sumGoal,digits):
    for i in combinations(initRange,digits):
        if sum(i) == sumGoal:
            digitList.append(i)

#asks and stores numbers that must be in list
def requiredNums(comboList):
    reqOnlyList = []

    #gets known numbers
    num = int(input('How many numbers do you know: '))
    knownLst = []
    for i in range(0,num):
        ele = int(input())
        knownLst.append(ele)
    
    #checks for items
    for set in comboList:
        if(all(ele in set for ele in knownLst)):
            reqOnlyList.append(set)
    print(reqOnlyList)
    
def again():
    #resets values
    sumGoal = int(input('Please enter the sum you are looking for: '))
    digits = int(input('Enter the number of digits for this sum: '))
    reqNumQuestion = input('Do you know any of the numbers? y or n: ')
    
    
    digitFinder(initRange,sumGoal,digits)
    #print(digitList)

    if reqNumQuestion == 'n'or reqNumQuestion == 'N':
        print(digitList)
    else:
        requiredNums(digitList)

    contQ = str(input('Do you wish to continue? y or n: '))
    if contQ == 'y' or contQ == 'Y':
        digitList.clear()
        again()

digitList = []
initRange = [1,2,3,4,5,6,7,8,9]
again()

contQ = str(input('Do you wish to continue? y or n: '))
if contQ == 'y' or contQ == 'Y' or contQ == "\n" or contQ == "":
    digitList.clear()
    again()