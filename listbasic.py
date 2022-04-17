# how to create a list

countries = []
cities = ['jakarta', 'surabaya', 'bandung']
scores = [3,8,6,4]

print(len(countries))

# add item to the list
countries.append("indonesia")
countries.append("malaysia")

print(len(countries))

print(countries)

countries.insert(1,"singapore")

print(countries)

countries.pop(1) # remove an item at specific index

print(countries)