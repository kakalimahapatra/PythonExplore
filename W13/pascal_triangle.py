# Name - Kakali Mahapatra
# Python Final exam
# Student ID - 84803
# pascal_84803.py


def main():
    triangle_r = int(input('Enter number from 1 to 15 for pascal triangle '))
    if(int(triangle_r) > 15 or int(triangle_r < 1)):
        print("Number should be between 1 and 15, try again")
        exit()
    if triangle_r==1:
        print(1)
        return

    displayPascalTriangle(createTriShape(triangle_r))

def displayPascalTriangle(triangleList):
    for rowNum in triangleList:
        space = int((spacing(rowNum, triangleList[len(triangleList)-1]))/2)
        for number in range(len(rowNum)):
            rowNum[number] = str(rowNum[number])
        print ((' ')*(space), ' '.join(rowNum))

def createTriShape(triangle_r):
    triangleList = [[1], [1, 1]]
    if triangle_r == 1:
        return triangleList[0]
    else:
        for triangle_r_num in range(2, triangle_r):
            triangleList.append([1]*triangle_r_num)
            for num in range(1, triangle_r_num):
                triangleList[triangle_r_num][num] = \
                    (triangleList[triangle_r_num-1][num-1]
                     +triangleList[triangle_r_num-1][num])
            triangleList[triangle_r_num].append(1)
        return triangleList

def spacing(num, nextNum):
    numlen = 0
    nextnumLen = 0
    for number in num:
        string_number = str(number)
        numlen += (len(string_number)+1)
    for number in nextNum:
        string_number = str(number)
        nextnumLen += (len(string_number)+1)
    return (nextnumLen-1) - (numlen-1)

main()
