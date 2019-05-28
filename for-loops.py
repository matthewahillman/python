

colours = ['purple', 'red', 'blue', 'green', 'yellow']
name = ['matthew', 'sarah', 'ethan', 'oliver', 'heather']

# looping over a range of numbers
for i in range(6):
    print(i)

# looping over a collection
for colour in colours:
    print(colour)

# looping backwards over a collection
for colour in reversed(colours):
    print(colour)

# Looping over a collection and indices - returns the index and the value
for index, colour in enumerate(colours):
    print(index, colours[index])

# looping over two collections
for name, colour in zip(name, colours):
    print(name, colour)

# looping over in sorted order
for colour in sorted(colours):
    print(colour)

# looking backwards in sorted order
for colour in sorted(colours, reverse=True):
    print(colour)

# custom sort order


def compare_length(c1, c2):
    if len(c1) < len(c20):
        return -1
    if len(c1) > len(c2):
        return 1
    return 0


print(sorted(colours, key=len))
