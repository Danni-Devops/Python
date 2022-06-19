# VARIABLE DECLARATION AND USAGE #
integer = 10
double = 12.5
string = "Hello"
space = " "
name = "Daniel"
greet = string + space + name

print(integer + double)
print(string + " " + name)
print(greet)

# NUMBERS(datatype) #
x = 12
y = 20
d = 5.50
print(x / 5)
print(d / 2)

# OPERATION ON NUMBERS #

# arithmetic operators = + - * / ** ()
# precedence:
    # ()
    # **
    # * / (same precedence, left to right precedence)
    # + - (same precedence, left to right precedence)

x = 3 + 4 * 10
print(x)
x = (3 + 4) * 10
print(x)

x = 3 + 4 ** 2 * 10
print(x)
x = (3 + 4) ** 2 * 10
print(x)

x = 3 + 4 - 1
print(x)
x = 3 - 4 + 1
print(x)


# VARIABLE NAMING RULES #
 # a-z,  A-Z 0-9 _
 # cannot cannot contain special charaters like @ %
 # cannot begin with a number

# VARAIBLE CASTING #

x = 29
print(type(x))
print(float(x))
print(type(x))
x = float(29)
print(x)
print(type(x))


# STRINGS #
name = 'Danni-DevOps'
print(name)
print(type(name))
print(type('Hello World'))

# METHODS AND STRINGS #
# print(dir("string")) - to view all methods that can be applied to a particular string
role = 'devops'
print(role.upper())
print(role.title())
print(role.lower())
