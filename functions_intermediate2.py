#1 Change array within array value
x = [[5,2,3], [10,8,9]]
x[1][0] = 15
print(x)

# Change last name of first student from 'Jordan' to 'Bryant'
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
students[0]['last_name'] = 'Bryant'
print(students)

# In the sports_directory, change 'Messi' to 'Andres'
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
sports_directory['soccer'][0] = 'Andres'
print(sports_directory)

# Change value 20 in z to 30
z = [ {'x': 10, 'y': 20} ]
z[0]['y'] = 30
print(z)

#####################################################

# Given a list of dictionaries, create function to loop through each and print each key and value
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
def iterateDictionary(lis):
    for x in range(len(lis)):
        fn = lis[x]['first_name']
        ln = lis[x]['last_name']
        print("first_name - " + fn + ", last_name - "+ ln)
    return
iterateDictionary(students)

######################################################

# Given a list of dictionaries and a key name, print the value stored in that key for each dict
def iterateDictionary2(key_name, some_list):
    for x in range(len(some_list)):
        val = some_list[x][key_name]
        print(val)
iterateDictionary2('first_name', students)
iterateDictionary2('last_name', students)

#######################################################

# Given a dictionary with values in the form of lists, print the name of each key along with the list size; then print the values from each key's list
dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def printInfo(some_dict):
    for i in some_dict:                         # iterate through the dictionary (2x)
        print(len(some_dict[i]), i.upper())     # print the number of values (some_dict[i]) and the key name
        for x in some_dict[i]:                  # iterate through the values to print the list
            print(x)
        print('\n')
printInfo(dojo)