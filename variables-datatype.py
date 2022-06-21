# VARIABLE DECLARATION AND USAGE #
integer = 10
double = 12.5
string = "Hello"
space = " "
name = "meek"
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
name = 'Meek-DevOps'
print(name)
print(type(name))
print(type('Hello World'))

# METHODS AND STRINGS #
# print(dir("string")) - to view all methods that can be applied to a particular string
role = 'devops'
print(role.upper())
print(role.title())
print(role.lower())


# INDEXING AND SLICING #
# indexing:
work = 'IT-solutions'
print(work[0])
print(work[0].upper())

# slicing:
print(work[0:7])
print(work[:7])
print(work[3:6])
print(work[-3:-1])


# STRING FORMATTING #
name = 'meek'
age = 29
statement = 'my name is ' + name + ' ' + 'and my age is ' + str(age)
print(statement)
print('my name is {} and my age is {}'.format(name, age))
print('my name is {1} and my age is {0}'.format(age, name))

me = ['meek', 29]
print(f'my name is {me[0]} and my age is {me[1]}')


# LIST #
myList = []
myList = ["devops", "it-solutions", 2022, "february", 22, 28]
print(myList)
print(len(myList))
print(myList[0])
print(myList[0:3])
print(dir(list))
print(myList.pop())
print(myList)
myList.append(91)
print(myList)
myList.remove(2021)
print(myList)
del myList
myList = ["devops", "it-solutions",["work",12,"SQL"]] # nested list
print(myList)
print(myList[2])
print(myList[2][2])
myList = ["devops", "it-solutions",["work",12,"SQL"],{"work":"it-solutions", "role":"DevOps"}]
print(myList)
print(myList[3]["work"])
print(myList[3]["role"])


# TUPLES #
myList = ()
myList = ("devops", "it-solutions", 2020, "May", 22, 28, "socs")
print(myList)
print(myList[0])
print(myList[-2])
print(dir(tuple))
print(len(myList))


# DICTIONARY #
myList = {}
myList = {"company":"it-solutions", "role":"DevOps", "employmentDate":"2nd May, 2022"}
print(myList["company"])
myList = {"company":"it-solutions", "role":"DevOps", "client":["metdev","netdev"]}
print(myList["client"][0])
myList = {"company":"it-solutions", "role":"DevOps", "client":{"client1":"metdev", "client2":"netdev"}}
print(myList["client"]["client1"])
print(myList["client"]["client2"])
print(len(myList))
print(len(myList["client"]))
print(myList)
myList["company"] = "Meek Solutions"
print(myList)
myList["client"]["client2"] = "secdev"
print(myList)
myList["client"]["client3"] = "netdev"
print(myList)
myList["client"]["client2"] = myList["client"]["client2"].lower()
print(myList)
myList.pop("role")
print(myList)
myList["client"].popitem()
print(myList)


# BOOLEAN #
# True or False
num_1 = 12
num_2 = 20
print(num_1 > num_2)
print(num_1 < num_2)
