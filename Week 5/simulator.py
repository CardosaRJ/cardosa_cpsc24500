"""
simulator.py - Week 5 Starter

Menu-driven Pet Simulator. Demonstrates polymorphism: the same methods
(feed, play, sleep) work on every pet type.

Menu:
1. Adopt a pet (cat / dog / fish)
2. Feed a pet
3. Play with a pet
4. Put a pet to sleep
5. View all pets
6. Quit
"""

from cat import Cat
from dog import Dog
from fish import Fish


def adopt_pet(pets):
    # TODO: ask which type, get name, create the right object, append to pets
    print("\nWhat type of pet would you like to adopt?")
    print("1. Cat")
    print("2. Dog")
    print("3. Fish")
    choice = input("Adopt a: ").strip()
    
    name = input("What will you name your new pet? ").strip()

    if choice == "1":
        pet = Cat(name)
    elif choice == "2":
        breed = input("What breed is the dog? ").strip()
        pet = Dog(name, breed)
    elif choice == "3":
        pet = Fish(name)
    else:
        print("Not a valid choice.")
        return
    
    pets.append(pet)
    print(f"Congratulations, you adopted {pet}!\n")

def select_pet(pets):
    """Show the list of pets and let the user pick one. Return the chosen pet."""
    # TODO: print numbered list of pets
    # TODO: get user choice and return that pet
    if not pets:
        print("You haven't adopted any pets yet!")
        return None
    print("\nYour pets:")
    for i, pet in enumerate(pets, 1):
        print(f"{i}. {pet}")
    while True:
        try:
            choice = int(input("\nChoose pet number: "))
            if 1 <= choice <= len(pets):
                return pets[choice - 1]
            print("Invalid number.")
        except ValueError:
            print("Please enter a number.")

def main():
    pets = []
    # TODO: loop showing the menu and dispatching to the right action
    #       remember: feed/play/sleep should work the same regardless of pet type
    print("Welcome to the Pet Sim!")

    while True:
        print("\nWhat would you like to do?")
        print("1. Adopt a pet")
        print("2. Feed a pet")
        print("3. Play with a pet")
        print("4. Put a pet to sleep")
        print("5. View all pets")
        print("6. Quit")
        choice = input("Make your choice: ").strip()

        if choice == "1":
            adopt_pet(pets)
        elif choice == "2":
            pet = select_pet(pets)
            if pet:
                pet.feed()
        elif choice == "3":
            pet = select_pet(pets)
            if pet:
                pet.play()
        elif choice == "4":
            pet = select_pet(pets)
            if pet:
                pet.sleep()
        elif choice == "5":
            if not pets:
                print("You haven't adopted any pets yet!")
            else:
                print("\nYour adopted pets:")
                for pet in pets:
                    print(pet.status())
        elif choice == "6":
            print("Until Next Time!")
            break
        else:
            print("Sorry, that is not an option.")


if __name__ == "__main__":
    main()
