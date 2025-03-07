print("\tMembership Operators")
print("Membership Operators check if a value exists in a sequence (list, tuple, string, etc.).")

# Sample sequences
string_example = "apple"
list_example = [1, 2, 3, 4, 5]
tuple_example = ('a', 'b', 'c', 'd')

print("\nDefined sequences:")
print(f"String: {string_example}")
print(f"List: {list_example}")
print(f"Tuple: {tuple_example}")

# IN Operator (Returns True if value is in the sequence)
in_string = 'a' in string_example
print("\nChecking if 'a' is in the string 'apple' (in)")
print(f"'a' in '{string_example}' = {in_string}")

in_list = 3 in list_example
print("\nChecking if 3 is in the list [1, 2, 3, 4, 5] (in)")
print(f"3 in {list_example} = {in_list}")

in_tuple = 'c' in tuple_example
print("\nChecking if 'c' is in the tuple ('a', 'b', 'c', 'd') (in)")
print(f"'c' in {tuple_example} = {in_tuple}")

# NOT IN Operator (Returns True if value is NOT in the sequence)
not_in_string = 'z' not in string_example
print("\nChecking if 'z' is NOT in the string 'apple' (not in)")
print(f"'z' not in '{string_example}' = {not_in_string}")

not_in_list = 10 not in list_example
print("\nChecking if 10 is NOT in the list [1, 2, 3, 4, 5] (not in)")
print(f"10 not in {list_example} = {not_in_list}")

not_in_tuple = 'x' not in tuple_example
print("\nChecking if 'x' is NOT in the tuple ('a', 'b', 'c', 'd') (not in)")
print(f"'x' not in {tuple_example} = {not_in_tuple}")
