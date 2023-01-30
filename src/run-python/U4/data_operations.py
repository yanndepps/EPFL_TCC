apples = 11
oranges = 7
fruits = apples + oranges
print(fruits)

# eat some apples, store the remaining amount of them
apples = apples - 1
fruits = apples + oranges
print(fruits)

# also eat an orange just because ...
oranges = oranges - 1

# and one more apple ...
apples = apples - 1

# again compute the new amount of fruits
fruits = apples + oranges
print("amount of fruits : ", fruits)
