# Building The Car Game
command = ""
started = False
while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("Car has already started!")
        else:
            started = True
        print("Car started...")
    elif command == "stop":
        if not started:
            print("Car has already stopped!")
        else:
            started = False
        print("Car stopped.")
    elif command == "help":
        print("""
start - starts the car
stop - stops the car
quit - to quit
        """)
    elif command == "quit":
        break
    else:
        print("I don't quite understand what you mean by that!")
