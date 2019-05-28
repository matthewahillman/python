colours = ['purple', 'red', 'blue', 'green', 'yellow']
colours_2 = ['white', 'cyan']
numbers = [1, 3, 5, 6, 7, 8, 9, 2, 4, 10]

print("The original colours list")
print(colours)


# apend - adding an item to the end of the list
colours.append('orange')
print("\nAdding in the colour Orange")
print(colours)

# insert - adding an item to the list in selected location (2 arguments - location, property)
colours.insert(0, 'black')
print("\nInserting the colour Black at point 0")
print(colours)

# Entend - adding a list (each item) to another list - adds to the end of the list
colours.extend(colours_2)
print("\nExtending colours list with colours_2")
print(colours)

# remove - removing an item from a list by property
colours.remove('white')
print("\nRemoving white from list")
print(colours)

# Pop - removing the last item from a list
colours.pop()
print("\nPop off the item on the end of the list")
print(colours)

# Pop - seeing what property was removed from the popping
popped = colours.pop()
print("\nWhat was popped off the list?")
print(popped)
print(colours)
print("Shouldn\'t this be 'Cyan?'")

# # Ordering list items without loops

# reverse the list
colours.reverse()
print("\nReverse the list")
print(colours)

# Sort - sort by Alphabetical
colours.sort()
print("\nSort in Alphabetical order")
print(colours)

# Sort - sort by numerical border
numbers.sort()
print("\nSort in Numerical order - number list")
print(numbers)

# Sort - reversed Ordering
colours.sort(reverse=True)
numbers.sort(reverse=True)
print("\nSort in reversed alphabetical order")
print(colours)
print("\nSort in reversed numerical order - number list")
print(numbers)

# Sorted - sorting the list without changing the list iteself
sorted_colours = sorted(colours)
print("\nSorting colours using a sorted function")
print(sorted_colours)

# Min - finding the smallest number in the list
print("\nThe smallest number is the list is: ")
print(min(numbers))

# Max - finding the largest number in the list
print("\nThe largest number is the list is: ")
print(max(numbers))

# Sum - finding the sum of all the numbers in the list
print("\nThe sum of all the numbers in the list is: ")
print(sum(numbers))

# Index - finding the index of a list item
print("\nFinding what index the item is in a list")
print(colours.index('purple'))

# In - True or False check if item is in the list
print("\nIs (x) in the list? ")
print('Maroon' in colours)
