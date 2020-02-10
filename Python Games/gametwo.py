# Building The Car Game
command = ""
started = False
while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("Car is already started!")
        else:
            started = True
        print("Car has started....")
    elif command == "stop":
        if not started:
            print("Car is already stopped!")
        else:
            started = False
        print("Car has stopped.")
    elif command == "help":
        print("""
start - starts the car
stop - stops the car
quit - to quit
        """)
    elif command == "quit":
        break
    else:
        print('I am not sure what you mean by that')