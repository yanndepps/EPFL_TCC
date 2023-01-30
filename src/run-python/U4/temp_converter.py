# Ex : Temperature converter
# a Celsius to Farenheit converter
celsius = 21
farenheit = (celsius * 9 / 5) + 32
print(farenheit)


# update the temp converter into a function
def temp_convert(celsius):
    result = (celsius * 9 / 5) + 32
    return result


print(temp_convert(21.5))
print(temp_convert(-7))
print(temp_convert(11))
print(temp_convert(45))
