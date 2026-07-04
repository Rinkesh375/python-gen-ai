seat_type = input("Enter seat type: ").lower()

match seat_type:
    case "sleeper":
        print("Features:")
        print("- Sleeping berth")
        print("- Fan")
        print("- Affordable fare")

    case "ac":
        print("Features:")
        print("- Air Conditioning")
        print("- Comfortable seats")
        print("- Bedding provided")

    case "general":
        print("Features:")
        print("- Basic seating")
        print("- Lowest fare")
        print("- No reservation")

    case "luxury":
        print("Features:")
        print("- Premium seats")
        print("- Meals included")
        print("- Wi-Fi")
        print("- Personal entertainment")

    case _:
        print("Invalid seat type")