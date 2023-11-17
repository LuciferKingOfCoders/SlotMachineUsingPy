MAX_LINES =3        # global var

def deposit():
    while True:
        amount = input ("How much would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amouont must be greater than 0.")
        else:
            print("Pls enter a number: ")
    return amount

def get_number_of_lines():
     while True:
        lines = input ("Enter the number of lines to bet on (1-" +str(MAX_LINES) + ")?")
        if lines.isdigit():        # Check if input is a digit
            lines = int(lines)
            if 1<= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print("Pls enter a number: ")
        return lines


def main():
    balance = deposit()
    lines = get_number_of_lines()
    print(balance, lines)


main()
f
