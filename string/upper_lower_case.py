# Python script that takes input from the user and displays that input back in upper and lower cases.


def display_input_cases():
    user_input = input("Enter your input: ")

    upper_case = user_input.upper()
    lower_case = user_input.lower()

    print("Input in Upper Case:", upper_case)
    print("Input in Lower Case:", lower_case)


display_input_cases()
