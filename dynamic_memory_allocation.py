# Create an empty list (dynamically allocated)
my_list = []

# Dynamically add elements using append()
for i in range(1, 6):
    my_list.append(i)
print(f"List after dynamic allocation of elements: {my_list}")

# Dynamically remove an element using remove()
my_list.remove(3)
print(f"List after removing an element: {my_list}")

# You can also use list() constructor
new_list = list()
new_list.append('a')
print(f"New list: {new_list}")
