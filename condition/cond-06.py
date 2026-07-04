input_seat = input("Enter Seat you want?")

match input_seat:
    case "sleeper":
        print("You will get sleeper")
    case "luxury":
        print("You will get luxury")
    case "general":
        print("You will get general")
    case "AC":
        print("You will get AC")
    case _:
        print(f"Invalid seat type {input_seat}")            
        
    


