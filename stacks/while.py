while True:
    name = input("Enter your name (or type 'exit' to stop): ")
    if name == "exit":
        break  # This stops the loop when 'exit' is typed.
    print(f"Hello, {name}!")


def ask_yes_no(question):
    while True:
        response = input(question + " (yes/no): ").strip().lower()
        if response in ["yes", "no"]:
            return response
        else:
            print("Please answer with 'yes' or 'no'.")
ask_yes_no("yes or no")