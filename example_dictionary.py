pet_dictionary = {"dogs": ["Yorkie", "Collie", "Bulldog"],
                  "cats": ["Persian", "Scottish Fold", "Siberian"],
                  "rabbits": ["Angora", "Holland Lop", "Harlequin"]}

print(pet_dictionary.get("dogs", 0))


# Should print ['Yorkie', 'Collie', 'Bulldog']

def sum_server_use_time(Server):
    # Initialize the variable as a float data type, which will be used
    # to hold the sum of the total hours and minutes of server usage by
    # end users in a day.
    total_use_time = 0.0

    # Iterate through the "Server" dictionary’s key and value items
    # using a for loop.
    for key, value in Server.items():
        # For each end user key, add the associated time value to the
        # total sum of all end user use time.
        total_use_time += Server[key]

    # Round the return value and limit to 2 decimal places.
    return round(total_use_time, 2)


FileServer = {"EndUser1": 2.25, "EndUser2": 4.5, "EndUser3": 1, "EndUser4": 3.75, "EndUser5": 0.6, "EndUser6": 8}

print(sum_server_use_time(FileServer))  # Should print 20.1


def list_full_names(employee_dictionary):
    # Initialize the "full_names" variable as a list data type using
    # empty [] square brackets.
    full_names = []

    # The outer for loop iterates through each "last_name" key and
    # associated "first_name" values, in the "employee_dictionary" items.
    for last_name, first_names in employee_dictionary.items():

        # The inner for loop iterates over each "first_name" value in
        # the list of "first_names" for one "last_name" key at a time.
        for first_name in first_names:
            # Append the new "full_names" list with the "first_name" value
            # concatenated with a space " ", and the key "last_name".
            full_names.append(first_name + " " + last_name)

    # Return the new "full_names" list once the outer for loop has
    # completed all iterations.
    return full_names


print(list_full_names({"Ali": ["Muhammad", "Amir", "Malik"], "Devi": ["Ram", "Amaira"], "Chen": ["Feng", "Li"]}))


# Should print ['Muhammad Ali', 'Amir Ali', 'Malik Ali', 'Ram Devi', 'Amaira Devi', 'Feng Chen', 'Li Chen']


def invert_resource_dict(resource_dictionary):
    # Initialize a "new_dictionary" variable as a dict data type using
    # empty {} curly brackets.
    new_dictionary = {}
    # The outer for loop iterates through each "resource_group" and
    # associated "resources" in the "resource_dictionary" items.
    for resource_group, resources in resource_dictionary.items():
        # The inner for loop iterates over each "resource" value in
        # the list of "resources" for one "resource_group" key at a time.
        for resource in resources:
            # The if-statement checks if the current "resource" value has
            # been appended as a key to the "new_dictionary" yet.
            if resource in new_dictionary:
                # If True, then append the "resource_group" as a value to the
                # "resource", which is now the key.
                new_dictionary[resource].append(resource_group)
            # If False (else), then add the "resource" as a new key with the
            # "resource_group" as a value for that key.
            else:
                new_dictionary[resource] = [resource_group]
    # Return the new dictionary once the outer for loop has completed
    # all iterations.
    return new_dictionary


print(invert_resource_dict({"Hard Drives": ["IDE HDDs", "SCSI HDDs"],
                            "PC Parts": ["IDE HDDs", "SCSI HDDs", "High-end video cards", "Basic video cards"],
                            "Video Cards": ["High-end video cards", "Basic video cards"]}))


# Should print {'IDE HDDs': ['Hard Drives', 'PC Parts'], 'SCSI HDDs': ['Hard Drives', 'PC Parts'], 'High-end video
# cards': ['PC Parts', 'Video Cards'], 'Basic video cards': ['PC Parts', 'Video Cards']}


def count_numbers(text):
    # Initialize a new dictionary.
    dictionary = {}
    # Complete the for loop to iterate through each "text" character.
    for char in text:
        # Complete the if-statement using a string method to check if the
        # character is a number.
        if char.isnumeric():
            # Complete the if-statement using a logical operator to check if
            # the number is not already in the dictionary.
            if char not in dictionary:
                # Use a dictionary operation to add the number as a key
                # and set the initial count value to zero.
                dictionary[char] = 0
            # Use a dictionary operation to increment the number count value
            # for the existing key.
            dictionary[char] += 1
    return dictionary


print(count_numbers("1001000111101"))
# Should be {'1': 7, '0': 6}
