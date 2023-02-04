# Multiconverter
# DONE: rename function snake_case style
# TODO: check for numbers only
# TODO: handle singular and plural msgs
# ---

# --- Main --- #
def main():
    while ask_cont():
        conv_type = ask_conv()
        conv_val = ask_val()
        if conv_type == "inches":
            cm_to_inches(conv_val)
        elif conv_type == "celsius":
            temp_convert(conv_val)
        elif conv_type == "liters":
            usg_to_ltrs(conv_val)
        else:
            print("Cannot convert this thing !")

    print("You don't want to convert things !")


# --- Utils --- #
# --- does one want to convert things ?
def ask_cont():
    answer = input("Do you want to convert a value? (yes/no) ")
    if answer == "yes":
        return True
    else:
        return False


# --- ask which conversion
def ask_conv():
    answer = input("Which conversion? (inches/celsius/liters) ")
    return answer


# --- ask for a value
def ask_val():
    answer = float(input("Which value do you want to convert? "))
    return answer


# --- cm to inches
def cm_to_inches(num):
    if num < 0:
        print("beware : negative values")

    formula = num / 2.54
    result = "{:.2f}".format(formula)
    print("the result is " + str(result))


# --- celsius to fahrenheit
def temp_convert(num):
    result = round(((num * 9 / 5) + 32), 2)
    print("the result is " + str(result))


# --- US Gallons to liters
def usg_to_ltrs(num):
    result = round((num / 0.26417), 2)
    print("the result is " + str(result))


main()
# --- END --- #
