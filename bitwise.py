print("\tBitwise Operators")
print("Bitwise Operators perform operations at the binary level.")

# Assign values
a = 5  # 0101 in binary
b = 3  # 0011 in binary

print("\nAssigned values:")
print(f"a = {a} (Binary: {bin(a)})")
print(f"b = {b} (Binary: {bin(b)})")

# Bitwise AND (&)
bitwise_and = a & b
print("\nBitwise AND (&) -> Performs AND operation on each bit")
print(f"{a} & {b} = {bitwise_and} (Binary: {bin(bitwise_and)})")

# Bitwise OR (|)
bitwise_or = a | b
print("\nBitwise OR (|) -> Performs OR operation on each bit")
print(f"{a} | {b} = {bitwise_or} (Binary: {bin(bitwise_or)})")

# Bitwise XOR (^)
bitwise_xor = a ^ b
print("\nBitwise XOR (^) -> Performs XOR operation on each bit")
print(f"{a} ^ {b} = {bitwise_xor} (Binary: {bin(bitwise_xor)})")

# Bitwise NOT (~)
bitwise_not_a = ~a
print("\nBitwise NOT (~) -> Inverts all bits")
print(f"~{a} = {bitwise_not_a} (Binary: {bin(bitwise_not_a)})")

# Left Shift (<<)
left_shift = a << 2
print("\nLeft Shift (<<) -> Shifts bits to the left, multiplying by 2^n")
print(f"{a} << 2 = {left_shift} (Binary: {bin(left_shift)})")

# Right Shift (>>)
right_shift = a >> 2
print("\nRight Shift (>>) -> Shifts bits to the right, dividing by 2^n")
print(f"{a} >> 2 = {right_shift} (Binary: {bin(right_shift)})")
