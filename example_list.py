# Skill Group 1
years = ["January 2023", "May 2025", "April 2023", "August 2024", "September 2025", "December 2023"]

updated_years = []

for year in years:
    if year.endswith("2023"):
        new = year.replace("2023", "2024")
        updated_years.append(new)
    else:
        updated_years.append(year)

print(updated_years)


# Skill Group 2
# Use a list comprehension to return values
def squares(start, end):
    return [n * n for n in range(start, end + 1)]


print(squares(2, 3))  # Should print [4, 9]
print(squares(1, 5))  # Should print [1, 4, 9, 16, 25]
print(squares(0, 10))  # Should print [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Skill Group 3
years = ["January 2023", "May 2025", "April 2023", "August 2024", "September 2025", "December 2023"]

updated_years = [year.replace("2023", "2024") if year[-4:] == "2023" else year for year in years]

print(updated_years)


# Sckill Group 4
def change_string(given_string):
    new_string = ""
    # Split the "given_string" into a "new_list", with each "element"
    # holding an individual word from the string.
    new_list = given_string.split()

    # The for loop iterates over each "element" in the "new_list".
    for element in new_list:
        # Convert the list into a "new_string" by using the assignment
        # operator += to concatenate the following items:
        # + Each list "element" (starting at index position [1:]),
        # + a dash "-",
        # + append the first character of the "element" (using the index
        # [0]) to the end of the "element", and finally,
        # + a space " " to separate each "element" in the "new_string".
        new_string += element[1:] + "-" + element[0] + " "

    # Return the list that has been converted back into a string.
    return new_string


print(change_string("1one 2two 3three 4four 5five"))

filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# Generate newfilenames as a list containing the new filenames
# using as many lines of code as your chosen method requires.
newfilenames = []
for name in filenames:
    if name.endswith("hpp"):
        name = name.replace("hpp", "h")
        newfilenames.append(name)
    else:
        newfilenames.append(name)

print(newfilenames)


# Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]

def group_list(group, users):
    members = ", ".join(users)
    return "{}: {}".format(group, members)


print(group_list("Marketing", ["Mike", "Karen", "Jake", "Tasha"]))  # Should be "Marketing: Mike, Karen, Jake, Tasha"
print(group_list("Engineering", ["Kim", "Jay", "Tom"]))  # Should be "Engineering: Kim, Jay, Tom"
print(group_list("Users", ""))  # Should be "Users:"


def guest_list(guests):
    for guest in guests:
        name, age, profession = guest
        print("{} is {} years old and works as {}".format(name, age, profession))


guest_list([('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")])

# Output:
# Ken is 30 years old and works as Chef
# Pat is 35 years old and works as Lawyer
# Amanda is 25 years old and works as Engineer
