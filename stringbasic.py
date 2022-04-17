# create a string in a variable

email = 'john@gmail.com'

full_name = "john doe"

# make the string uppercased, lowercase, title
print(full_name.upper())
print(full_name.title())

# escaping a single quote
text = 'i won\'t do that' 
quote = "He said \"No\" "

# contactinating / menggabungkan string
salutation = "Mr."

print(salutation + " " + full_name.title())
print("{0} {1}".format(salutation, full_name))

# find characters
print(email.find("@")) # return the index of the character @ or -1 if it didn't find it
# print(email.index("x"))

print(full_name.startswith("m"))

print(email.count("@"))