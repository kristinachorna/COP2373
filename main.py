def main():
    tickets_purchased = int(input('Enter the number of tickets you wish to purchase: '))
    tickets = 20
    tickets_left = tickets - tickets_purchased


    while tickets_purchased > 0:
        try:
            print('You have purchased ', tickets_purchased, 'tickets')
            print('There are ', tickets_left, 'tickets remaining')

            if tickets_purchased > 4:
                print('You cannot exceed 4 tickets per person. ')
            tickets_left = tickets - tickets_purchased
            input('Enter the number of tickets you wish to purchase: ')
main()

# def sale(tickets_left):


