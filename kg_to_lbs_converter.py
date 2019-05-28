import json
from datetime import datetime
from math import ceil, floor, trunc

now = datetime.now()
date_format = '%s/%s/%s' % (now.day, now.month, now.year)
name = input("Please enter the name of the child? ").capitalize()
current_weight = float(input("Enter the weight in kg: "))

# 1lb to grams
lbs_to_grams = 453.592

# 1oz to grams
oz = 28.3495

# 1g to pounds
g_to_lbs = 0.00220462

# 1g to ounces
g_to_oz = 0.035274

# kg to grams
kg_to_grams = current_weight * 1000

# 1 stone is = to 6.35029318kg
st_to_kg: float = 6.35029318


# Calculates lbs - current weight * 1000 / 453.592 then truncated so whole number without decimal.
def lbs():
    return trunc(kg_to_grams / lbs_to_grams)


# Calculates ounces - current weight * 1000 - lbs function output * 453.592 then / 28.3495
def ozs():
    return ceil((kg_to_grams - lbs() * lbs_to_grams) / oz)


def stone():
    return current_weight / st_to_kg


def printit():
    print("Today\'s date is: " + date_format)
    print(name + " is " + str(lbs()) + "lbs" + " and " + str(ozs()) + "ozs.")
    print("Stone: " + str(stone()))
    print("General output: " + str(output))


output = date_format, name, lbs(), ozs()
with open('weights.json', 'w') as f:
    json.dump(output, f, indent=4)
    print("All Saved!")
    f.close()


def main():
    printit()

if __name__ == "__main__":
    main()

