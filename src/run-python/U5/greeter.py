mal_greet = "Hello Sir! Welcome back !"
fem_greet = "Hello Madam! Welcome back !"
nos_greet = "Hello! Welcome back !"

gen_ins = ["male", "Male", "female", "Female"]

gender = input("choose a gender : ")


def greeter(gender):
    for val in gen_ins:
        if gender == gen_ins[0] or gender == gen_ins[1]:
            return mal_greet
        elif gender == gen_ins[2] or gender == gen_ins[3]:
            return fem_greet
        else:
            return nos_greet


print(greeter(gender))
