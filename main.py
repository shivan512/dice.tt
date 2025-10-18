# dice_basic.py
import random

def roll_die(sides=6):
    return random.randint(1, sides)

if __name__ == "__main__":
    input("Press Enter to roll a 6-sided die...")
    result = roll_die()
    print(f"You rolled: {result}")
