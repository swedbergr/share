# Define constants for auditorium
MAX_SEATS = 500  # Maximum seats for each show
TICKET_PRICE = 5.0  # Price per ticket

def main():
  # Assign starting values for available seats
  perform1_available = MAX_SEATS
  perform2_available = MAX_SEATS

  # Loop for decisions to run
  while True:
    # Display Main Menu given performance
    menu()
    action = input()
    # Validate selection
    while action != "1" and action != "2" and action != "3":
      print("That is not a valid choice. Please select 1, 2, or 3")
      action = input()

    # Exit program if selected
    if action == "3":
      print("Thank you for your interest in the show!")
      break
    
    # Display main menu and get desired perfomance
    choose_performance()
    performance = input()
    # Validate performance date
    while performance != "Friday" and performance != "Saturday":
      print("That is not an option for a performance date.")
      print("Please select either Friday or Saturday.")
      performance = input()

    # Complete action
    if action == "1":
      # Iterate for complete validation
      while True:
        # Get number of tickets from user
        tickets = input("How many tickets would you like? ")
        # Validate tickets for digit
        if not tickets.isdigit():
          print("That is not a valid number.")
          # Restart loop
          continue

        # Cast tickets to int
        tickets = int(tickets)
      
        # Validate availability
        if performance == "Friday":
          if tickets > perform1_available:
            print(f"There are only {perform1_available} tickets remaining. Please select a number that is less than {perform1_available}.")
            # Restart loop
            continue

          # Update availability and break loop validation
          perform1_available -= tickets
          break

        else: 
          if tickets > perform2_available:
            print(f"There are only {perform2_available} tickets remaining. Please select a number that is less than {perform2_available}.")
            # Restart loop
            continue

          # Update availability and break loop validation
          perform2_available -= tickets
          break

      # Display
      book_tickets(performance, tickets)

    else:
      # Determine performance
      if performance == "Friday":
        display_availability(performance, perform1_available)
      else:
        display_availability(performance, perform2_available)


# Function to display the main menu
def menu():
  print("Main Menu")
  print("Select option for the UNK musical performance.")
  print("1. Book Tickets")
  print("2. View Availability")
  print("3. Exit")

# Function to choose a performance
def choose_performance():
  print("Main Menu")
  print("There are two performances for the musical.")
  print("Please choose the Friday or Saturday performance.")

main()
  