# updated converter
cm = input("enter a value: ")


def converter(cm):
    if float(cm) < 0:
        print("beware : negative value !")

    msg_1 = " centimeters are "
    msg_2 = " inches !"
    result = float(cm) / 2.54
    return str(cm) + msg_1 + str(result) + msg_2


print(converter(cm))
