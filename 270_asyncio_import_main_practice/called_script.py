# This file is meant to help understand how the python works for importing
# one file's functions with an import statment from another.

def welcome_message() :
    """Prints welcome message for asyncio script."""
    print("Initializing asyncio script")
    print("Please await the random number generation.")
    print("The numbers will wait their length asynchronously")

if __name__ == '__main__':
    print("This script is meant to be called from another script")
