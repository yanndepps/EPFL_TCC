# Ex : The friendly converter
# def temp_conv(c):
#     result = (c * 9 / 5) + 32
#     message = (
#         str(c)
#         + " "
#         + "degrees Celsius are"
#         + " "
#         + str(result)
#         + " "
#         + "degrees Farenheit !"
#     )
#     return message


# friendly_temp = temp_conv(21)
# print(friendly_temp)

# Ex : The friendly converter with user input
c = input("Please choose a temperature to convert : ")


def temp_conv(c):
    result = (float(c) * 9 / 5) + 32
    message = (
        str(c)
        + " "
        + "degrees Celsius are"
        + " "
        + str(result)
        + " "
        + "degrees Farenheit !"
    )
    return message


friendly_temp = temp_conv(c)
print(friendly_temp)
