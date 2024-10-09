# Function to ask a yes/no question and handle response
def ask_yes_no(question):
    while True:
        response = input(question + " (yes/no): ").strip().lower()
        if response in ["yes", "no"]:
            return response
        else:
            print("Please answer with 'yes' or 'no'.")

# Main function that asks three questions


def main():
    # First yes/no question
    response1 = ask_yes_no("Do you want to attend a sports event?")

    if response1 == "yes":
        event_type = input(
            "Great! What type of sport are you interested in (e.g., football, basketball)? ")
        print(f"Awesome! You are interested in {event_type}.")

        # Second yes/no question based on the first response
        response2 = ask_yes_no("Do you want to buy a ticket for this event?")

        if response2 == "yes":
            ticket_quantity = input("How many tickets do you want to buy? ")
            print(f"You want to buy {ticket_quantity} ticket(s) for the {
                  event_type} event.")
        else:
            print("You chose not to buy a ticket.")

        # Third yes/no question based on the second response
        response3 = ask_yes_no(
            "Would you like to receive updates about future events?")

        if response3 == "yes":
            email = input(
                "Please enter your email address to receive updates: ")
            print(f"Thank you! We will send updates to {email}.")
        else:
            print("No problem! You won't receive any updates.")
    else:
        print("You chose not to attend the event.")


# Run the main function
main()
