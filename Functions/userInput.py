def user_input():
    acceptable_range = range(0,10)
    user_choice = 'WRONG!'
    range_check = False
    while user_choice.isdigit() == False or range_check == False:
        user_choice = input("Please enter a number (0-10): ")

        if user_choice.isdigit() == False:
            print("oops! that is not a digit. Please enter a number (0-10)")

        if user_choice.isdigit() == True:
            if int(user_choice) in acceptable_range:
                range_check = True
            else:
                print("Sorry you are out of acceptable range (0-10)")
                range_check = False
    return int(user_choice)

user_input()