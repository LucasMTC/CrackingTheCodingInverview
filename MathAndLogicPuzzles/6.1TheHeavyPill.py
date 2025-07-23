"""
You have 20 bottles of pills. 19 Bottles have pills that weigh exactly 1.0 gram. One of the bottles has pills
that weigh 1.1 grams. Given a scale that provides an exact measurment, how would you find the heavy bottle?
You can only use the scale once.
"""
import random

def findHeavyBottle(arr:list) -> int:
    total = 0
    expected = 210
    for i in range(1, len(arr)+1):
        total += arr[i-1] * i
    total -= expected
    return round(total * 10) - 1

if __name__ == "__main__":
    pills = [1] * 20
    index = random.randint(0, 19)
    pills[index] = 1.1
    assert findHeavyBottle(pills) == index