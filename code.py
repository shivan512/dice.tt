# dice_simulation.py
import random
from collections import Counter

def simulate(num_dice=2, sides=6, trials=100000):
    counts = Counter()
    for _ in range(trials):
        total = sum(random.randint(1, sides) for _ in range(num_dice))
        counts[total] += 1
    # convert to probabilities
    probs = {total: count / trials for total, count in sorted(counts.items())}
    return probs

if __name__ == "__main__":
    probs = simulate(num_dice=2, sides=6, trials=100000)
    for total, p in probs.items():
        print(f"{total}: {p:.4f}")
