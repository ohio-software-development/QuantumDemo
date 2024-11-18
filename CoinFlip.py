import time
import random

def coin_flip():
    print("Flipping the coin...", end="", flush=True)
    for _ in range(10):
        print(".", end="", flush=True)
        time.sleep(1)
    
    print()  
    result = random.choice(["Heads", "Tails"])
    print(f"The result is: {result}")

coin_flip()