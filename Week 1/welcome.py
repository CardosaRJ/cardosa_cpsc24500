from datetime import datetime

def main():
    # Ask the user for their name
    name = input("What is your name? ")

    # Three required different variable types
    current_year = 2026 # int
    temperature = 68.5 # float
    is_input_name_good = len(name.strip()) > 0  # boolean

    # Get current date and time
    now = datetime.now()

    # Simple personalized welcome banner (3 lines with your name)
    print("*" * 40)
    print(f"~~~~WELCOME TO CPSC 24500, {name}!~~~~")
    print("*" * 40)
    print(f"Today is {now.strftime('%B %d, %Y')} at {now.strftime('%I:%M %p')}")

    # Two extra f-strings (required)
    print(f"\nHi {name}, great to be in OOP with you!")
    print(f"Current year: {current_year} | Temp: {temperature}°F | Name entered correctly: {is_input_name_good}")

main()