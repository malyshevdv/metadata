mylist = [3,0,0,2,0,4]
mylist = [0,0,0,2,0,4]

water_total = 0
for height in range(1, max(mylist)+1):
    StartWall = False
    wall_position = -1
    print(f'Level {height}-th')
    for mystep in range(len(mylist)):
        if (mylist[mystep]-height)>=0:

            if not StartWall:
                StartWall = True
                wall_position = mystep

            else: # it is wall
                step_vater = mystep- wall_position -1
                water_total += step_vater
                print(f"{step_vater}")
                wall_position = mystep


print(f'Total water={water_total}')