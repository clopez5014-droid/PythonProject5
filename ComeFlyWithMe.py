# Come Fly With Me - Airplane Seat Purchase Simulation

NUM_SEATS = 20

# Track which seats are taken
taken = [False] * NUM_SEATS


def get_seat_type(seat_num: int) -> str:
    """
    Return seat type:
    F = First-Class (1-4)
    E = Emergency Exit (6-9)
    R = Regular (everything else)
    """
    if 1 <= seat_num <= 4:
        return "F"
    elif 6 <= seat_num <= 9:
        return "E"
    else:
        return "R"


def show_seats():
    print("\nCurrent Seating Chart:")
    print("Legend: O = Open, X = Taken, F = First-Class, E = Emergency Exit\n")

    for i in range(NUM_SEATS):
        seat_num = i + 1
        status = "X" if taken[i] else "O"
        label = get_seat_type(seat_num)
        print(f"{seat_num:2d}[{status} {label}] ", end="")
        if seat_num % 5 == 0:
            print()
    print()


def purchase_seat() -> bool:
    """Return False to stop, True to continue."""
    try:
        seat_num = int(input("Enter a seat number to purchase (1–20), or 0 to finish: "))
    except ValueError:
        print("Invalid entry, please enter a number.")
        return True

    if seat_num == 0:
        print("Thank you for choosing Come Fly With Me!")
        return False

    if not 1 <= seat_num <= 20:
        print("That seat does not exist.")
        return True

    index = seat_num - 1

    if taken[index]:
        print(f"Seat {seat_num} is already taken.")
        return True

    seat_type = get_seat_type(seat_num)

    # FIRST-CLASS CHECK
    if seat_type == "F":
        print(f"\nSeat {seat_num} is a FIRST-CLASS seat.")
        print("It has an additional fee of $75.00.")
        while True:
            confirm = input("Do you still want to purchase this seat? (Y/N): ").strip().upper()
            if confirm in ("Y", "N"):
                break
            print("Please enter Y or N.")
        if confirm == "N":
            print("Purchase canceled.\n")
            return True

    # EMERGENCY EXIT CHECK
    if seat_type == "E":
        print(f"\nSeat {seat_num} is in an EMERGENCY EXIT ROW.")
        print("You must be willing and able to help in case of an emergency.")
        while True:
            confirm = input("Do you accept this responsibility? (Y/N): ").strip().upper()
            if confirm in ("Y", "N"):
                break
            print("Please enter Y or N.")
        if confirm == "N":
            print("You cannot sit in an emergency exit seat.\n")
            return True

    # PURCHASE SEAT
    taken[index] = True
    print(f"\nSeat {seat_num} successfully purchased!\n")
    return True


def main():
    print("Welcome to the 'Come Fly With Me' seat purchase system!")
    running = True
    while running:
        show_seats()
        running = purchase_seat()


if __name__ == "__main__":
    main()
