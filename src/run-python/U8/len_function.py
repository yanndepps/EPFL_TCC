# How many people are in our company at different points in time,
# after adding and removing people
# The len() function
# ---

employees = ["Richard Swift", "Marie-Anne Petrie"]
num_employees = len(employees)
mess = "At the beginning, there are " + str(num_employees) + " employees"
print(mess)

employees.append("Cody Lightfoot")
employees.append("Laure Simmons")

num_employees = len(employees)
mess = "The company grows and now has " + str(num_employees) + " employees"
print(mess)

employees.pop(1)

num_employees = len(employees)
mess = "Marie-Anne left the company. There are now " + str(num_employees) + " employees"
print(mess)

# sort in reverse alphabetical order
employees.sort()
employees.reverse()
print(employees)

# ---
