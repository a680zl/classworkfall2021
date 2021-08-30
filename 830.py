def interface():
    print('blood calculator')
    keep_running = True
    while keep_running:
        print('make a choice')
        print("9 - Quit")
        choice = int(input("Enter your choice: "))
        print(type(choice))
        if choice == 9:
            keep_running = False
    print(choice)
    return choice


solution = interface()
print(solution)
