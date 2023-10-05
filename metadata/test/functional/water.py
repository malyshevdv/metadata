def printLevel(myList : list, level : int):
    if level < max(myList):
        printLevel(myList, level + 1)

    #for i in myList:
   #     res = ?((i-level)>0, 1, 2)
    #    print(f'{res}',end='')
    #print('')

def printList(myList):
    print(myList)
    printLevel(myList,0)
def makeDesision():
    mylist = [3, 0, 0, 2, 0, 4]
    # mylist = [0,0,0,2,0,4]
    printList(mylist)


    water_total = 0
    for height in range(1, max(mylist) + 1):
        StartWall = False
        wall_position = -1
        print('')
        print(f'Level {height}-th  :', end='')
        for mystep in range(len(mylist)):
            if (mylist[mystep] - height) >= 0:

                if not StartWall:
                    StartWall = True
                    wall_position = mystep

                else:  # it is wall
                    step_vater = mystep - wall_position - 1
                    water_total += step_vater
                    print(f"{step_vater}", end=' ')
                    wall_position = mystep

    print('')
    print(f'Total water={water_total}')

if __name__ == '__main__':
    makeDesision()
