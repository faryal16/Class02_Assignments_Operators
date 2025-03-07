print("\tIdentity Operators")
print("Identity Operators are used to compare the memory location of objects, not just their values.")

# Assign values
x = 10
y = x  # y references the same object as x
z = 10  # z is a separate object with the same value

print("\nAssign values:")
print(f"x = {x}, y = {y}, z = {z}")

# IS Operator (Returns True if both variables refer to the same object)
same_object = x is y
print("\nReturns True if both variables refer to the same object (is)")
print(f"x is y -> {x} is {y} = {same_object}")

# IS NOT Operator (Returns True if variables do not refer to the same object)
different_object = x is not z
print("\nReturns True if variables do not refer to the same object (is not)")
print(f"x is not z -> {x} is not {z} = {different_object}")
# False because x and z might refer to the same memory location for small integers (Python optimizes this).

# Changing variable reference
z = 20
updated_check = x is z
print("\nAfter changing z:")
print(f"x is z -> {x} is {z} = {updated_check}")
