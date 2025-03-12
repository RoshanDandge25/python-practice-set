# 5) Define a function overlapping() that takes two lists and returns True if they
# have at least one member in common, False otherwise.

def overlapping():
    list1 = input("Enter elements of first list = ").split()
    list2 = input("Enter elements of second list = ").split()

    repeated_values = []
    # Check if any element of list1 is in list2
    for item in list1:
        if item in list2:
            repeated_values.append(item)
    if repeated_values:
        print(f"The repeated values are: {', '.join(repeated_values)}")
        return True
    return false


# Example usage
if overlapping():
    print("The lists have  common element.")
else:
    print("The lists have no common elements.")
