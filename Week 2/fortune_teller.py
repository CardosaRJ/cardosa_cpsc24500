import random

def welcome_banner():
    # Prints a decorative welcome banner
    print("-" * 50)
    print("|" + " " * 15 + "The Fortune Teller" + " " * 15 + "|")
    print("|" + " " * 6 + "What fate do the stars hold for you!" + " " * 6 + "|")
    print("-" * 50)
    print()

def age_int(age):
    # Age validation with try/except check
    while True:
        try:
            value = int(input(age))
            if value > 0:
                return value
            else:
                print("Invalid input. Please enter a proper age.")
        except ValueError:
            print("Invalid input. Please enter a proper age.")

def fortune_category(lucky_number):
    """Simple fortune category using if/elif/else (no color here)"""
    if lucky_number == 1:
        return "Critical Bad Luck!"
    elif lucky_number <= 5:
        return "Mid Tier Luck Draw."    
    elif lucky_number <= 9:
        return "Top Tier Luck Draw."
    else:
        return "Critical Great Luck!"
    
def random_fortune(favorite_color):
    # Returns one random fortune with favorite color customization 
    color = favorite_color.lower()

    fortunes = [
        f"A bright burst of {color} will spark new ideas this week.",
        f"Wearing {color} will bring unexpected good luck your way.",
        f"Trust the calm energy of {color} to guide your decisions.",
        f"An exciting adventure awaits you — look for hints of {color}.",
        f"Prosperity flows easily when you surround yourself with {color}.",
        f"Your next big opportunity will have a strong {color} theme.",
        f"Balance and harmony come from embracing more {color} in your life.",
        f"A message from the universe will arrive in shades of {color}."
    ]

    return random.choice(fortunes)

def save_fortune(name, category, fortune):
    # Saves results to fortune_output.txt
    with open("fortune_output.txt", "w") as f:
        f.write(f"Name: {name}\n")
        f.write(f"Fortune Category: {category}\n")
        f.write(f"Fortune: {fortune}\n")
    print("Your fortune has been saved to fortune_output.txt")

def main():
    welcome_banner()

    # Collect inputs
    full_name = input("Enter your full name: ").strip()
    age = age_int("Enter your age: ")
    favorite_color = input("Enter your favorite color: ").strip()

    # Fortune Generation Functions
    lucky_number = random.randint(1, 10)
    category = fortune_category(lucky_number)
    fortune = random_fortune(favorite_color)

    # Display Fortune
    print("\n" + "*" * 50)
    print("WHAT YOUR FORTUNE HOLDS!")
    print("*" * 50)
    print(f"Name:             {full_name.upper()}")
    print(f"Name length:      {len(full_name)} characters")
    print(f"Age:              {age}")
    print(f"Favorite color:   {favorite_color.lower()}")
    print(f"Lucky number:     {lucky_number}")
    print(f"Fortune category: {category}")
    lucky_percent = (lucky_number / age) * 100
    print(f"Lucky percentage: {lucky_percent:.3f}%")
    print("\nYour fortune:")
    print(f'"{fortune}"')
    print("*" * 50)

    # Save to file
    save_fortune(full_name, category, fortune)

    # Send off
    first_name = full_name.split()[0]
    print(f"\nFarewell, {first_name}. May the odds be ever in your favor!")
    print("*" * 50)

if __name__ == "__main__":
    main()