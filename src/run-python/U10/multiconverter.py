# Multiconverter
# DONE: rename function snake_case style
# DONE: check for numbers only
# DONE: handle singular and plural msgs
# ---


# --- Main --- #
def main():
    while ask_cont():
        conv_type = ask_conv()
        conv_val = ask_val()
        # --- numbers only
        try:
            res = float(conv_val)
        except:
            print("Please enter a valid number !")
            quit()
        # --- logic
        if conv_type == "inches":
            cm_to_inches(res)
        elif conv_type == "celsius":
            temp_convert(res)
        elif conv_type == "liters":
            usg_to_ltrs(res)
        else:
            print("Cannot convert this thing !")
    # ---
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
    answer = input("Which value do you want to convert? ")
    return answer


# --- check for singular or plural messages
# --- most probably a plain stupid idea to write it like this ...
def singular_plural(num, result, fn):
    words = {
        "deg": " degree",
        "cel": " celsius",
        "fahr": " fahrenheit",
        "cm": " centimeter",
        "inch": " inch",
        "inches": " inches",
        "usg": " US Gallon",
        "ltr": " liter",
        "plural": "s",
        "is": " is ",
        "are": " are ",
    }
    msg = ""
    # check for celsius to fahrenheit function
    if fn == "temp_convert":
        if float(result) > -1.0 and float(result) < 1.0:
            msg = (
                str(num)
                + words["deg"]
                + words["cel"]
                + words["is"]
                + str(result)
                + words["deg"]
                + words["fahr"]
            )
        else:
            msg = (
                str(num)
                + words["deg"]
                + words["plural"]
                + words["cel"]
                + words["are"]
                + str(result)
                + words["deg"]
                + words["plural"]
                + words["fahr"]
                + words["plural"]
            )
    # check for cm to inches function
    elif fn == "cm_to_inches":
        if float(result) > -1.0 and float(result) < 1.0:
            msg = str(num) + words["cm"] + words["is"] + str(result) + words["inch"]
        else:
            msg = (
                str(num)
                + words["cm"]
                + words["plural"]
                + words["are"]
                + str(result)
                + words["inches"]
            )
    # check for US gallons to liters function
    elif fn == "usg_to_ltrs":
        if float(result) > -1.0 and float(result) < 1.0:
            msg = str(num) + words["usg"] + words["is"] + str(result) + words["ltr"]
        else:
            msg = (
                str(num)
                + words["usg"]
                + words["plural"]
                + words["are"]
                + str(result)
                + words["ltr"]
                + words["plural"]
            )

    return msg


# --- cm to inches
def cm_to_inches(num):
    # if neg value
    if num < 0:
        print("beware : negative values")

    formula = num / 2.54
    result = "{:.2f}".format(formula)
    res_msg = singular_plural(num, result, "cm_to_inches")
    print(str(res_msg))


# --- celsius to fahrenheit
def temp_convert(num):
    formula = (num * 9 / 5) + 32
    result = "{:.2f}".format(formula)
    res_msg = singular_plural(num, result, "temp_convert")
    print(str(res_msg))


# --- US Gallons to liters
def usg_to_ltrs(num):
    # if neg value
    if num < 0:
        print("beware : negative values")

    result = round((num / 0.26417), 2)
    res_msg = singular_plural(num, result, "usg_to_ltrs")
    print(str(res_msg))


main()
# --- END --- #
