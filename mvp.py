# Minimum Viable Product


def dollars_to_pounds(dollars):
    exchange_rate = 0.801344
    pounds = dollars * exchange_rate
    return round(pounds, 2)

def pounds_to_dollars(pounds):
    exchange_rate = 1.24821
    dollars = pounds * exchange_rate
    return round(dollars, 2)

# Further planning
while True:
    request = input("Choose option 1 or 2:\n1: dollar-to-pounds\n2: pounds-to-dollars)?")
    if request == "1":
        dollars = input("How many dollars would you like to convert to pounds? $")
        dollars = int(dollars)
        print("Value in pounds: £" + str(dollars_to_pounds(dollars)))
        if input("Quit(y/n)")=="y":
            break
    elif request == "2":
        pounds = input("How many pounds would you like to convert to dollars? £")
        pounds = int(pounds)
        print("Value in dollars: $" + str(pounds_to_dollars(pounds)))
        if input("Quit(y/n)")=="y":
            break
    else:
        print("Did not make a valid selection")
        if input("Quit(y/n)")=="y":
            break