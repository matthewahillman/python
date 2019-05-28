import random
import time

print("Hello world")

hello = "Hello world"

print(hello)

first = 10
second = 20

if first + second == 30:
    print("yes")
else:
    print("no")

x = 10

while x > 0:
    print(x)
    x = x - 1
    time.sleep(0.5)

print(random.randint(1, 100))
