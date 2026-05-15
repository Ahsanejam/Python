# def my_function():
#     print("Hello")
#     print("Bye")
def robot():
    robot_steps = 8
    block = 0
    print("Go outside the house ")
    print("Steps 2 blocks of right")
    block += 2
    if block == 2:
        print("Then see left side and walk 4 blocks ")
        block += 4
        if block == 6:
            print("Then see right and steps 2 blocks ")
            block += 2
            if block == robot_steps:
                print("Finally you reach the destination : ")
                print("Take milk and come back")
            else:
                print("You cannot reach the destination")

robot()
