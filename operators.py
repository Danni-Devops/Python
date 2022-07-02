# OPERATORS #
# types of operators:
    # 1. Arithmetic operators
    # 2. Comparison operators
    # 3. Assignment operators
    # 4. Logical operators
    # 5. Identity operators
    # 6. Membership operators
    # 7. Bitwise operators

num_1 = 10
num_2 = 3

# ARITHMETIC OPERATORS #
    # 1. +
    # 2. -
    # 3. *
    # 4. /
    # 5. %
    # 6. **
    # 7. //

print(num_1 + num_2)
print(num_1 - num_2)
print(num_1 * num_2)
print(num_1 / num_2)
print(num_1 % num_2)
print(num_1 ** num_2)
print(num_1 // num_2)

# ASSIGNMENT OPERATORS #
    # 1. =
    # 2. +=
    # 3. -=
    # 4. *=
    # 5. /=
    # 6. %=
    # 7. **=
    # 8. //=

num_1 += num_2
print(num_1)
num_1 -= num_2
print(num_1)
num_1 *= num_2
print(num_1)
num_1 /= num_2
print(num_1)
num_1 %= num_2
print(num_1)
num_1 **= num_2
print(num_1)
num_1 //= num_2
print(num_1)

# COMPARISON OPERATORS #
    # 1. ==
    # 2. !=
    # 3. >
    # 4. >=
    # 5. <
    # 6. <=

print(num_1 == num_2)
print(num_1 != num_2)
print(num_1 > num_2)
print(num_1 >= num_2)
print(num_1 < num_2)
print(num_1 <= num_2)

# LOGICALLY OPERATORS #
    # 1. and
    # 2. or
    # 3. not

print(num_1 == num_2 and num_1 != num_2)
print(num_1 < num_2 or num_1 <= num_2)
print(num_1 < num_2 or num_1 <= num_2 and num_1 < num_2)
print(num_1 < num_2 and num_1 <= num_2 and num_1 < num_2)
print(num_1 < num_2 or num_1 <= num_2 or num_1 < num_2)
print(not (num_1 < num_2 or num_1 <= num_2 or num_1 < num_2))

# IDENTITY OPERATORS #
    # 1. is
    # 2. is not

x = 12
y = 10

print(x is y)
print(y is x)
print(x is not y)

# IDENTITY OPERATORS #
    # 1. in
    # 2. not in

x = [12,10,4,2,6,20]
print(5 in x)
print(10 in x)
print(10 not in x)
print(5 not in x)
