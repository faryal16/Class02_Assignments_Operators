print("\tLogical Operators")
print("Logical Operators are those operators that work with boolean values (True or False).")

x = 7
print("\nAssign value:")
print(f"x = {x}")

# AND Operator (Returns True if both conditions are True)
aur = x > 5 and x < 10
print("\nReturns True if both conditions are True (and)")
print(f"{x} > 5 and {x} < 10 = {aur}")

# OR Operator (Returns True if at least one condition is True)
nahe = x > 5 or x < 3
print("\nReturns True if at least one condition is True (or)")
print(f"{x} > 5 or {x} < 3 = {nahe}")

# NOT Operator (Reverses the result)
print("\nReverses the result (not)")
not_aur = not aur
print(f"not ({aur}) = {not_aur}")

not_nahe = not nahe
print(f"not ({nahe}) = {not_nahe}")
