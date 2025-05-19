# Kristina Chorna
# Chapter 1: Exercise 1
# This code will sell 20 tickets using an if statement and a loop. It will then determine the number of buyers once
# the tickets have been sold out.

# create a function to sell the tickets
def ticket_sale(tickets_left):
    while tickets_left > 0:
        try:
            print('There are ' , tickets_left, ' tickets remaining. ')
            # prompt the user to enter the number of tickets
            tickets_purchased = int(input('Enter the number of tickets you would like to purchase (up to 4): '))

            if tickets_purchased > 4:
                print('You cannot exceed 4 tickets.')
                continue

            if tickets_purchased > tickets_left:
                print('Only ' , tickets_left, ' tickets are left. Please enter a smaller number.')
                continue

            tickets_left -= tickets_purchased
            # determine a successful buyer
            return tickets_left, True

        except ValueError:
            print('Invalid input. Please enter a number.')

    return tickets_left, False


# create a function to determine that the tickets were sold out and calculate the number of buyers
def main():
    tickets = 20
    buyers = 0

    while tickets > 0:
        tickets, success = ticket_sale(tickets)
        if success:
            # set an accumulator to determine the number of buyers
            buyers += 1

    # display the results
    print('The tickets have been sold out. ')
    print('The total number of buyers is: ' , buyers)


main()
