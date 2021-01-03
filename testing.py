set1 = { 1, 2, 33}
set2 = {23,4,2,33,5}

# print(set1.union(set2))
# print("------------")
# print(set1.intersection(set2))

# print("--------------")
# print(type(set1))

list = [ 1,2,3,4,5,4,66,6,4,5,6]
print(set(list))

hundred_meters = ['Vikay','John','Kumar','Rajesh','Malar','Vaihai']
two_hundred_meters = ['Vetry','Petter','Priyanka','Kumar','Malar']

# Find the answer for below question from above lists (using set and Boolean Operators) a. Find the athletes who participated only in 100m race
# b. Find the athletes who participated only in 200m race
# c. Find the athletes who participated both 100m and 200m race
# d. Find the athletes who participated only one race

print(set(two_hundred_meters)-set(hundred_meters))

print(set(two_hundred_meters).union(set(hundred_meters)))

print(set(two_hundred_meters).intersection(set(hundred_meters)))