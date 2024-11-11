# Main function
def main():
    '''
    Main function that contains a menu and calls to helper functions to complete tasks
    '''
    # Display introduction
    print("Welcome to the grade calculation program. This program allows you to enter scores ", 
        "you received and view the cumulative average grade.")
    # Start menu
    while True:
        print("Please select an option: ")
        print("1. Enter new scores\n2. Calculate average")
        choice = input()

        # Navigate choice
        if choice == "1":
            get_scores()
        elif choice == "2":
            calculate_grade()
        else:
            print("That is not a valid choice.")
        

def get_scores():
    '''
    Void function that gets points earned and total points from the user and stores them into a file.
    '''
    pass


def calculate_grade():
    '''
    Void function that reads a file of points earned and total points and calcualtes a cumulative average.
    '''
    pass


if __name__ == "__main__":
    main()
