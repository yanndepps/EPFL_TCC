def say_hello(name):
    print("hello " + name)


say_hello("Rick")
say_hello("Lory")
say_hello("Daryl")

# a simple calculator
def add(number_one, number_two):
    result = number_one + number_two
    print(result)


add(5, 3)

# use the return keyword in our functions
def sub(num_one, num_two):
    result = num_one - num_two
    return result


total = sub(30, 22)
print(total)


def mul(num_one, num_two):
    return num_one * num_two


print(mul(10, 10))

# another greetings example
# catch the output ( return value ) and assign it to a var
def greet(name, weather):
    message = "Hi " + name + ", it is a " + weather + " day!"
    return message


greetings = greet("Sasha", "rainy")
print(greetings)
greetings = greet("Carl", "sunny")
print(greetings)
