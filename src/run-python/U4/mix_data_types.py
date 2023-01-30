# Mixing data types
number_one = 3
number_two = 2
result = number_one + number_two
a_string = "hello"

message = str(result) + " " + a_string
# print(message)

# ---

# apples = "3"
# oranges = 2
# result = int(apples) + oranges
# print(result)

# ---
# apples = 3
# oranges = 2
# result = apples + oranges
# message = "there are " + str(result) + " fruits in the basket !"

# print(message)

# convert calculator function inputs
def add(a, b):
    return a + b


num_to_str = str(add(3, 7))
message = "The result is " + num_to_str
# print(type(num_to_str))
print(message)

# ---
def sub(a, b):
    message = "The result is "
    c = a - b
    return message + str(c)


print(sub(7, 5))
