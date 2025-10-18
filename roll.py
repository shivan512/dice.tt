# dice_roller.py
import random

def roll_die(sides):
    return random.randint(1, sides)

def roll_many(num, sides):
    rolls = [roll_die(sides) for _ in range(num)]
    return rolls, sum(rolls)

def parse_notation(notation):
    # accepts forms like "3d6" or "d20" or "2D10"
    notation = notation.lower().strip()
    if 'd' not in notation:
        raise ValueError("Use NdS notation, e.g., 2d6 or d20")
    parts = notation.split('d')
    num = int(parts[0]) if parts[0] != '' else 1
    sides = int(parts[1])
    return num, sides

def main():
    print("Dice Roller (type 'quit' to exit)")
    while True:
        s = input("Enter dice (NdS), e.g., 2d6 or d20: ").strip()
        if s.lower() in ('quit', 'q', 'exit'):
            break
        try:
            num, sides = parse_notation(s)
        except Exception as e:
            print("Invalid input:", e)
            continue
        rolls, total = roll_many(num, sides)
        print("Rolls:", rolls)
        print("Total:", total)
        print("-" * 20)

if __name__ == "__main__":
    main()
